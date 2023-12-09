from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import re


def criar_chave_256_bits(string: str, tamanho_bytes: int = 32) -> bytes:
    return SHA256.new(string.encode('utf-8')).digest()[:tamanho_bytes]


def cifrar(texto, chave):
    chave = criar_chave_256_bits(chave)
    iv = get_random_bytes(AES.block_size)

    cifra = AES.new(chave, AES.MODE_CBC, iv)

    padded_text = pad(texto.encode('latin-1'), AES.block_size)
    texto_cifrado = cifra.encrypt(padded_text)

    texto_encriptado = iv + texto_cifrado
    texto_base64 = texto_encriptado.hex()

    return texto_base64


def decifrar(texto_cifrado, chave):
    chave = criar_chave_256_bits(chave)
    texto_encriptado = bytes.fromhex(texto_cifrado)

    iv = texto_encriptado[:AES.block_size]

    cipher = AES.new(chave, AES.MODE_CBC, iv)

    texto_decriptado = unpad(cipher.decrypt(
        texto_encriptado[AES.block_size:]), AES.block_size)

    texto_decodificado = texto_decriptado.decode('latin-1')

    return texto_decodificado


def cifrar_arquivo(nome_arquivo: str, chave):
    novo_nome = re.sub(r'\.[a-zA-Z]*$', '', nome_arquivo)+'.cripto'
    extensao = re.findall(r'\.[a-zA-Z]*$', nome_arquivo)[0]
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_original:
        with open(novo_nome, 'w', encoding='utf-8') as arquivo_cripto:
            arquivo_cripto.write(cifrar(extensao, chave)+'\n')
            for linha in arquivo_original:
                arquivo_cripto.write(cifrar(linha, chave)+'\n')


def decifrar_arquivo(nome_arquivo, chave):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_cripto:
        extensao = decifrar(arquivo_cripto.readline(), chave)
        print(extensao)
        # for linha in arquivo_cripto:
            # print(decifrar(linha, chave))
        # extensao = re.findall(r'\.[a-zA-Z]*\n$', extensao)
        nome_original = re.sub(r'\.cripto$', '', nome_arquivo)+'-decifrado'+extensao
        with open(nome_original, 'w', encoding='utf-8') as arquivo_originial:
            for linha in arquivo_cripto:
                arquivo_originial.write(decifrar(linha, chave))