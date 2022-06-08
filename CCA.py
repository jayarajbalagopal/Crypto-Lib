import sys
sys.path.append('../')

from task_3.CPA import encrypt_output_feedback, decrypt_output_feedback, string_to_binary
from task_4.CBC_MAC import generate_tag, verify, keysize
import random

def randombinary(l):
    out = str()
    for i in range(l):
        out += str(random.randint(0,1))
    return out

def encrypt(msg, key1, key2, blocksize):
	cipher = encrypt_output_feedback(msg, key1, blocksize)
	mac = generate_tag(cipher[0], key2)
	return (cipher, mac)

def decrypt(cipher_text, key1, r1, tag, key2, r2):
	authenticated = verify(cipher_text, tag, key2)
	if authenticated:
		msg = decrypt_output_feedback(cipher_text, key1, r1)
		return (msg, authenticated)
	else:
		return (cipher_text, authenticated)

if __name__ == "__main__":
	msg = "Hello!"
	blocksize = keysize
	key1 = randombinary(blocksize)
	key2 = randombinary(keysize)
	print("Key 1: ", key1)
	print("Key 2: ", key2)
	enc = encrypt(msg, key1, key2, blocksize)
	print("ENCRYPITON: ", enc[0][0])
	print("R: ", enc[0][1])
	print("MAC: ", enc[1])
	dec = decrypt(enc[0][0], key1, enc[0][1], enc[1], key2, enc[1][0])
	print("DECRYPTION: ", dec)