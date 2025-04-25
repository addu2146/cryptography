import numpy as np

def char2num(ch: str) -> int:
    return ord(ch) - ord('A')

def num2char(n: int) -> str:
    return chr(n + ord('A'))

def hillenc(plaintext: str, key: np.ndarray) -> str:
    text = plaintext.upper().replace(' ', '')
    m = key.shape[0]
    while len(text) % m:
        text += 'X'

    ciphertext = ''
    for i in range(0, len(text), m):
        block = text[i:i+m]
        vec   = np.array([char2num(c) for c in block])       # 1×m row
        cvec  = np.dot(vec, key) % 26                        # row·key mod 26
        ciphertext += ''.join(num2char(int(x)) for x in cvec)
    return ciphertext

def invmod(key: np.ndarray) -> np.ndarray:
    det   = int(round(np.linalg.det(key)))
    dmod  = det % 26
    d_inv = pow(dmod, -1, 26)
    # adjugate: det * inv(key), then round to ints
    adj   = (np.linalg.inv(key) * det).round().astype(int) % 26
    return (d_inv * adj) % 26

def hilldec(ciphertext: str, key: np.ndarray) -> str:
    m      = key.shape[0]
    keyinv = invmod(key)
    plaintext = ''

    for i in range(0, len(ciphertext), m):
        block = ciphertext[i:i+m]
        vec   = np.array([char2num(c) for c in block])
        pvec  = np.dot(vec, keyinv) % 26
        plaintext += ''.join(num2char(int(x)) for x in pvec)

    return plaintext.rstrip('X')


if __name__ == '__main__':
    keym      = np.array([[17, 17, 5],
                          [21, 18, 21],
                          [ 2,  2, 19]])
    plaintext = 'pay more money'
    ciphertext = hillenc(plaintext, keym)
    print('Encrypted:', ciphertext)      # e.g. LPQCIIZGGPYV
    print('Decrypted:', hilldec(ciphertext, keym))  # PAYMOREMONEY
