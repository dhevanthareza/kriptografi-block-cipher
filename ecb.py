from Crypto.Cipher import AES

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encrypt(key, plain):
    keyByte = pad(key).encode('ASCII')
    plainByte = pad(plain).encode('ASCII')
    aes = AES.new(keyByte,AES.MODE_ECB)
    cipherByte = aes.encrypt(plainByte)
    return cipherByte

def decrypt(key, cipher):
    keyByte = pad(key).encode('ASCII')
    cipherByte = cipher
    aes = AES.new(keyByte,AES.MODE_ECB)
    plainByte = aes.decrypt(cipherByte)
    return plainByte.decode('ASCII')

print("=========ENKRIPSI==============")
plain = input("Plain Text = ")
key = input("Kunci Enkripsi = ")
ciphertext = encrypt(key, plain)
print("Ciphertext = ", ciphertext)

print("=========DEKRIPSI==============")
plaintext = decrypt(key, ciphertext)
print("Plaintext = ", unpad(plaintext))


