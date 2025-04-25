from Crypto.Cipher    import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    """
    DES is a 16-round Feistel cipher with 64-bit blocks.
    We're using PyCryptodome’s DES in CBC as a simple example.
    """
    cipher = DES.new(key, DES.MODE_CBC, iv)
    return cipher.encrypt(pad(plaintext, DES.block_size))

def des_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), DES.block_size)
