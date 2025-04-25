from Crypto.Cipher    import Twofish
from Crypto.Util.Padding import pad, unpad

def twofish_encrypt(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Twofish.new(key, Twofish.MODE_CBC, iv)
    return cipher.encrypt(pad(plaintext, Twofish.block_size))

def twofish_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Twofish.new(key, Twofish.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), Twofish.block_size)
