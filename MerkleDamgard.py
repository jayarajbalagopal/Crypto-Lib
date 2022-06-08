import sys
sys.path.append('../')

from task_6.HASH import fixed_hash, generate_group
import random

bl = 16

def randombinary(l):
    out = str()
    for i in range(l):
        out += str(random.randint(0,1))
    return out

def H(inp, IV, p, q, g, h):
	length = bin(len(inp))[2:].zfill(bl)

	blocks = [ inp[i:i+bl] for i in range(0, len(inp), bl) ]
	hsh = IV
	for block in blocks:
		block = block.zfill(bl)
		hsh = fixed_hash(block, hsh, p, q, g, h)
	hsh = fixed_hash(length, hsh, p, q, g, h)
	return hsh

if __name__ == "__main__":
	IV = randombinary(bl)
	p, q, g, h = generate_group(bl)
	inp = "101001101011101010101001101001001110010010010010010100101111"
	print("Input: ", inp)
	print("HASH: ", H(inp, IV, p, q, g, h))
