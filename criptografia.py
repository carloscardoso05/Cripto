from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

def criar_chave_256_bits(string: str, tamanho_bytes: int = 32) -> bytes:
    """Cria uma chave de 256 bits (32 bytes) a partir de uma string qualquer

    Args:
        string (str): String para servir de base para a criação da chave
        tamanho_bytes (int, optional): Tamanho da chave em bytes. Padrão é 32.

    Returns:
        bytes: Chave criada em bytes
    """
    return SHA256.new(string.encode('utf-8')).digest()


def cifrar_mensagem(texto: str, chave: str) -> str:
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


def decifrar_mensagem(texto_cifrado: str, chave: str) -> str:
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

def cifrar_arquivo(nome_arquivo: str, senha: str):
    """Cifra um arquivo usando o algoritmo AES e salva o resultado em outro arquivo.

    Parâmetros:
    - input_file: O caminho do arquivo de entrada.
    - output_file: O caminho do arquivo de saída cifrado.
    - key: A chave AES para cifragem (deve ter 16, 24 ou 32 bytes).
    """
    chave = criar_chave_256_bits(senha)
    iv = get_random_bytes(16)
    cifra = AES.new(chave, AES.MODE_CBC, iv)


    with open(nome_arquivo, 'rb') as file:
        arquivo_original = file.read()

    padded_text = pad(arquivo_original, AES.block_size)
    texto_cifrado = cifra.encrypt(padded_text)

    # Obtém a extensão do arquivo original
    caminho, extensao = os.path.splitext(nome_arquivo)
    extensao_bytes = extensao.encode('utf-8')
    arquivo_cifrado = caminho + ".cripto"

    with open(arquivo_cifrado, 'wb') as file:
        file.write(len(extensao_bytes).to_bytes(2, byteorder='big'))
        file.write(extensao_bytes)

        file.write(len(cifra.iv).to_bytes(2, byteorder='big'))
        file.write(cifra.iv)

        file.write(len(texto_cifrado).to_bytes(4, byteorder='big'))
        file.write(texto_cifrado)

    return arquivo_cifrado

def decifrar_arquivo(nome_arquivo: str, senha: str):
    """
    Decifra um arquivo cifrado usando o algoritmo AES e salva o resultado em outro arquivo.

    Parâmetros:
    - input_file: O caminho do arquivo de entrada cifrado.
    - output_file: O caminho do arquivo de saída decifrado.
    - key: A chave AES para decifragem (deve ter 16, 24 ou 32 bytes).
    """
    chave = criar_chave_256_bits(senha)
    with open(nome_arquivo, 'rb') as arquivo:
        extensao_tamanho = int.from_bytes(arquivo.read(2), byteorder='big')
        extensao_bytes = arquivo.read(extensao_tamanho)

        iv_tamanho = int.from_bytes(arquivo.read(2), byteorder='big')
        iv = arquivo.read(iv_tamanho)

        texto_cifrado_tamanho = int.from_bytes(arquivo.read(4), byteorder='big')
        texto_cifrado = arquivo.read(texto_cifrado_tamanho)

    cifra = AES.new(chave, AES.MODE_CBC, iv)
    texto_decifrado = unpad(cifra.decrypt(texto_cifrado), AES.block_size)

    caminho, _ = os.path.splitext(nome_arquivo)
    arquivo_decifrado = caminho + "_decifrado" + extensao_bytes.decode('utf-8')

    with open(arquivo_decifrado, 'wb') as arquivo:
        arquivo.write(texto_decifrado)

    return arquivo_decifrado