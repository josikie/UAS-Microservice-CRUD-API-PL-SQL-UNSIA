import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import os

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

SALT = os.environ.get("KEY")

def encrypt(raw, key):
    # private key stores byte string with 32 bytes (256 bits) 
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode("utf-8")))
 
 
def decrypt(enc, key):
    # private key stores byte string with 32 bytes (256 bits) 
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:])).decode("utf-8")
