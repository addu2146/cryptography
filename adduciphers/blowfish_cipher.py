from Crypto.Cipher    import Blowfish
from Crypto.Util.Padding import pad, unpad

def blowfish_encrypt(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    return cipher.encrypt(pad(plaintext, Blowfish.block_size))

def blowfish_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), Blowfish.block_size)
