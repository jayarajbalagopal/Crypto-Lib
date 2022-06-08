import random
import math

bl_h = 16

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False   
    return True

def generate_safe_prime(beg):
	q = beg
	while True:
		if isPrime(q) and isPrime(2*q+1):
			return 2*q+1,q
		q = q+1

def generate_group(mx=pow(2,bl_h)):
	p,q = generate_safe_prime(mx)
	h = random.randint(0, q-1)
	g = 4
	return p, q, g, h

# 32 -> 16 bit collision resistant hash function
def fixed_hash(x1, x2, p, q, g, h):
	x1_i = int(x1, 2)
	x2_i = int(x2, 2)

	hash_val = (pow(g, x1_i, p)*pow(h, x2_i, p))%pow(2,bl_h)
	return bin(hash_val)[2:].zfill(bl_h)

if __name__ == "__main__":
	p, q, g, h = generate_group()
	x1 = "101001110101"
	x2 = "101001001001"
	print("Input: ", x1.zfill(bl_h)+x2.zfill(bl_h))
	print("HASH: ", fixed_hash(x1, x2, p, q, g, h))