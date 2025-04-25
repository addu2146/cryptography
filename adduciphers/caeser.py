def Caeser(plaintext: str,key: int ,mode:str)->str:
    result = []
    shift =key if mode == "encrypt" else -key
    for c in plaintext:
        if 'A'<=c<='Z':
            result.append(chr((ord(c)-65+shift)%26+65))
        elif 'a'<=c<='z':
            result.append(chr((ord(c)-97+shift)%26+97))
        else: result.append(c)
    return ''.join(result)
plaintext = 'Micheal'
key = 2
enc = Caeser(plaintext,key,"encrypt")
dec = Caeser(enc,key,"decrypt")
print("encrypted: ",enc)
print("Decrypted: ",dec)
