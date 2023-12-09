from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import re


def criar_chave_256_bits(string: str, tamanho_bytes: int = 32) -> bytes:
    """Cria uma chave de 256 bits (32 bytes) a partir de uma string qualquer

    Args:
        string (str): String para servir de base para a criação da chave
        tamanho_bytes (int, optional): Tamanho da chave em bytes. Padrão é 32.

    Returns:
        bytes: Chave criada em bytes
    """
    return SHA256.new(string.encode('utf-8')).digest()[:tamanho_bytes]


def cifrar(texto: str, chave: str) -> str:
    """Criptografa um texto a partir de uma chave usando o algoritmo AES

    Args:
        texto (str): Texto a ser criptografado
        chave (str): Chave para criptografar o texto

    Returns:
        str: String criptografada
    """
    chave = criar_chave_256_bits(chave)
    iv = get_random_bytes(AES.block_size)

    cifra = AES.new(chave, AES.MODE_CBC, iv)

    padded_text = pad(texto.encode('latin-1'), AES.block_size)
    texto_cifrado = cifra.encrypt(padded_text)

    texto_encriptado = iv + texto_cifrado
    texto_base64 = texto_encriptado.hex()

    return texto_base64


def decifrar(texto_cifrado: str, chave: str) -> str:
    """Descriptografa um texto a partir de uma chave usando o algoritmo AES

    Args:
        texto_cifrado (str): Texto a ser descriptografado
        chave (str): Chave para descriptografar o texto

    Returns:
        str: String descriptografada
    """
    chave = criar_chave_256_bits(chave)
    texto_encriptado = bytes.fromhex(texto_cifrado)

    iv = texto_encriptado[:AES.block_size]

    cipher = AES.new(chave, AES.MODE_CBC, iv)

    try:
        texto_decriptado = unpad(cipher.decrypt(texto_encriptado[AES.block_size:]), AES.block_size)
    except:
        raise ValueError("Chave incorreta")

    texto_decodificado = texto_decriptado.decode('latin-1')

    return texto_decodificado


def cifrar_arquivo(nome_arquivo: str, chave: str):
    """Criptografa um arquivo qualquer a partir de uma chave usando o algoritmo AES

    Args:
        nome_arquivo (str): Nome do arquivo que se deseja criptografar
        chave (str): Chave para usar na criptografia
    """
    novo_nome = re.sub(r'\.[a-zA-Z]*$', '', nome_arquivo)+'.cripto'
    extensao = re.findall(r'\.[a-zA-Z]*$', nome_arquivo)[0]
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_original:
        with open(novo_nome, 'w', encoding='utf-8') as arquivo_cripto:
            arquivo_cripto.write(cifrar(extensao, chave)+'\n')
            for linha in arquivo_original:
                arquivo_cripto.write(cifrar(linha, chave)+'\n')


def decifrar_arquivo(nome_arquivo: str, chave: str):
    """Descriptografa um arquivo .cripto a partir de uma chave usando o algoritmo AES

    Args:
        nome_arquivo (str): Nome do arquivo que se deseja descriptografar
        chave (str): Chave para usar na descriptografia
    """
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_cripto:
        extensao = decifrar(arquivo_cripto.readline(), chave)
        print(extensao)
        nome_original = re.sub(r'\.cripto$', '', nome_arquivo)+'-decifrado'+extensao
        with open(nome_original, 'w', encoding='utf-8') as arquivo_originial:
            for linha in arquivo_cripto:
                arquivo_originial.write(decifrar(linha, chave))