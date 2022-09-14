import os
from sys import argv
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

simple_key = get_random_bytes(32)
print(simple_key)

salt = b'\xc9\xff\xb9[i@\x97\xff\x1aj~\xeb\xe1\xba\x90\xfb\x1f\xe9\xf2\xc4\x161\x7f\x97\x8fx\xef\xcf\xcd\xf1s\xb7'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)



msg = b'test'


cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(msg, AES.block_size))

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)
    
with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()
    
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)

with open('key.bin', 'wb') as f:
    f.write(key)