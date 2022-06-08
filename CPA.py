import sys
sys.path.append('../')

import random
from task_2.PRF import prf

def randombinary(l):
    out = str()
    for i in range(l):
        out += str(random.randint(0,1))
    return out

def string_to_binary(msg):
    byte_array =  msg.encode()
    binary_int = int.from_bytes(byte_array, "big")
    binary_string = bin(binary_int)[2:]
    return binary_string

def binary_to_string(bmsg):
    binary_int = int(bmsg, 2)
    byte_number = binary_int.bit_length() + 7 // 8

    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    return ascii_text

def encrypt_output_feedback(msg, key, blocksize):
    r = randombinary(blocksize)
    pf = prf(r, key)
    bmsg = string_to_binary(msg)

    temp = pf
    while(len(temp)<len(bmsg)):
        pf = prf(pf, key)
        temp += pf
    temp = temp[:len(bmsg)]
    y = str()
    for i in range(len(bmsg)):
        y += str(int(bmsg[i])^int(temp[i]))
    return (y, r)

def decrypt_output_feedback(cipher, key, r):
    pf = prf(r, key)

    temp = pf
    while(len(temp)<len(cipher)):
        pf = prf(pf, key)
        temp += pf
    temp = temp[:len(cipher)]
    out = str()
    for i in range(len(cipher)):
        out += str(int(cipher[i])^int(temp[i]))
    return binary_to_string(out).lstrip('\x00')

if __name__ == "__main__":
    msg = "Hello, this is a CPA secure encryption!"
    key = randombinary(16)
    print("ENCRYPTING: " + msg)
    cipher, r = encrypt_output_feedback(msg, key, 16)
    print("CIPHER: " + cipher)
    print("R: " + r)
    print("DECRYPTING")
    print(decrypt_output_feedback(cipher, key, r))

