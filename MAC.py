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
	blocksize = keysize//4
	blocks = [(i//blocksize, str(bmsg[i:i+blocksize]).zfill(blocksize)) for i in range(0, len(bmsg), blocksize)]
	r = randombinary(blocksize)
	tags = []
	for block in blocks:
		blk = block[1]
		seq = bin(block[0])[2:].zfill(blocksize)
		ln = bin(blocksize)[2:].zfill(blocksize)
		clt = r + blk + seq + ln
		tag = prf(clt, key)
		tags.append(tag)
	return (r, tags)

def verify_block(block, bs, r, seq,  key, tag):
	clt = r + block + seq + bs
	temptag = prf(clt, key)
	return temptag == tag

def verify(bmsg, r, tags, key):
	blocksize = keysize//4
	blocks = [(i//blocksize, str(bmsg[i:i+blocksize]).zfill(blocksize)) for i in range(0, len(bmsg), blocksize)]
	verified = True
	for i in range(len(tags)):
		blockinfo = blocks[i]
		seq = bin(blockinfo[0])[2:].zfill(blocksize)
		block = blockinfo[1]
		bs = bin(blocksize)[2:].zfill(blocksize)
		tag = tags[i]
		verified = verified and verify_block(block, bs, r, seq, key, tag)
	return verified

if __name__ == "__main__":
	msg = "Hello MAC"
	bmsg = string_to_binary(msg)
	key = randombinary(keysize)
	r, tags = generate_tag(bmsg, key)
	print("R: " + r)
	print("TAGS: " + str(tags))
	print("Authentication: " + str(verify(bmsg, r, tags, key)))