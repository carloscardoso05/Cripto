from Crypto.Cipher import AES
from Crypto.Hash import SHA256

tag = None
nonce = None

def criar_chave_256_bits(string: str, tamanho_bytes:int = 32) -> bytes:
    return SHA256.new(string.encode('latin-1')).digest()[:tamanho_bytes]

def cifrar(texto: str, chave: str) -> str:
    texto = bytes(texto.encode('latin-1'))
    chave:bytes = criar_chave_256_bits(chave)
    cifra = AES.new(chave, AES.MODE_EAX)
    global tag
    global nonce
    bytes_cifrados, tag = cifra.encrypt_and_digest(texto)
    nonce = cifra.nonce
    return bytes_cifrados.decode('latin-1')

def decifrar(texto_cifrado: str, chave: str):
    global nonce
    global tag
    texto_cifrado = bytes(texto_cifrado.encode('latin-1'))
    chave: bytes = criar_chave_256_bits(chave)
    decifra = AES.new(chave, AES.MODE_EAX, nonce)
    return decifra.decrypt_and_verify(texto_cifrado, tag).decode('latin-1')