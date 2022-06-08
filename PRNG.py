ge = 223
pr = 36389
sz = 32

def l(x):
    return 2*x

def xor(bits):
    bit = 1
    for i in range(len(bits)):
        bit = bit ^ int(bits[i])
    return bit

def h(bits):
    x = int(bits, 2)
    y = bin(pow(ge, x)%pr)[2:]
    bit = xor(bits)
    return [y, bit]

def prng(seed):
    bits = seed
    pseudorandom = str()
    for i in range(l(len(bits))):
        res = h(bits)
        pseudorandom += str(res[1])
        bits = res[0]
    return pseudorandom

if __name__ == "__main__":
    x = "1010001"
    print("X: " + x)
    print("PRNG: " + prng(x))