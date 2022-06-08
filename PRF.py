import sys
sys.path.append('../')

from task_1.PRNG import prng

def prf(x, key):
	s = key
	for b in x:
		ns = prng(s)
		x = ns[:len(ns)//2]
		y = ns[len(ns)//2:]
		if b == "0":
			s = x
		else:
			s = y
	return s

if __name__ == "__main__":
	key = "101001"
	x = "100000"
	print("Key: " +  key)
	print("X: " + x)
	print("PRF: " + prf(x, key))