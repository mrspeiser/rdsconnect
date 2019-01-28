from binascii import hexlify
import os, random, string, random

def configureKey(length=20):
    key = generate_key(length)

def generate_key(length=30):
    return hexlify(os.urandom(length))
    # return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_token(length=79):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))

def checkKey(key):
    de_coded=decoded(key)
    if has_match(de_coded):
        return True
    else:
        return False

def has_match(de_crypted):
    pass

def decoded(key):
    # remove encryption layer
    # now call decode
    de_coded = key.decode()
    return de_coded