import sys
sys.path.append('../')

from task_6.HASH import fixed_hash, generate_group
from task_7.MerkleDamgard import randombinary, H
import random

bl = 16

def HMAC(K, msg):
	ip = bin(int("5c", 16))[2:]
	op= bin(int("36", 16))[2:]

	ipad = ip
	opad = op
	while(len(ipad)<bl):
		ipad += ip
	ipad = ipad[:bl]
	while(len(opad)<bl):
		opad += op
	opad = opad[:bl]

	IV = randombinary(bl)
	p, q, g, h = generate_group(bl)

	initial_pad_xor = bin(int(K, 2) ^ int(ipad, 2))[2:].zfill(bl)
	post_pad_xor = bin(int(K, 2) ^ int(opad, 2))[2:].zfill(bl)

	init = fixed_hash(initial_pad_xor, IV, p, q, g, h)
	hsh = H(msg, init , p, q, g, h)
	post = fixed_hash(post_pad_xor, IV, p, q, g, h)
	res = fixed_hash(hsh, post, p, q, g, h)
	return res

if __name__ == "__main__":
	K = randombinary(bl)
	msg = "1010010110101010010010101001001001010010010101010101111111111111111001111101110100100100101010101010101010101"
	print("Msg: ", msg)
	print("HMAC: ", HMAC(K,msg))