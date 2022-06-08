import sys
sys.path.append('../')

from task_2.PRF import prf
import random
import re

keysize = 16

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

def generate_tag(bmsg, key):
	blocksize = keysize
	blocks = [(i//blocksize, str(bmsg[i:i+blocksize]).zfill(blocksize)) for i in range(0, len(bmsg), blocksize)]
	l = len(bmsg)
	tag = prf(key, bin(l)[2:].zfill(blocksize))
	for block in blocks:
		tag = prf(tag, block[1])
	return tag

def verify(bmsg, tag, key):
	blocksize = keysize
	blocks = [(i//blocksize, str(bmsg[i:i+blocksize]).zfill(blocksize)) for i in range(0, len(bmsg), blocksize)]
	temp = generate_tag(bmsg, key)
	return temp == tag

if __name__ == "__main__":
    msg = "Hello MAC"
    bmsg = string_to_binary(msg)
    key = randombinary(keysize)
    tag = generate_tag(bmsg, key)
    print("TAG: " + tag)
    print("Authentication: " + str(verify(bmsg, tag, key)))