#! /usr/bin/env python
# author: vin

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096, backend=default_backend())
print(private_key)

public_key = private_key.public_key()
print(public_key)

# 使用公钥加密
message = b'more secrets go here'

encrypted = public_key.encrypt(message,
                               padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                            algorithm=hashes.SHA256(),
                                            label=None))

print(encrypted)

# 使用私钥解密
decrypted = private_key.decrypt(encrypted,
                                padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                             algorithm=hashes.SHA256(),
                                             label=None))
print(decrypted)
