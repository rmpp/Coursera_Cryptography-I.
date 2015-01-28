import sys

MSGS =["This is the content of the secret message eavesdropped",
	   "And this is a sample message with common english expressions"] 

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(key, msg,f):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

def main():
	#get a random key
	key = random(1024)
	f = open('cripto','w')
	ciphertexts = [encrypt(key, msg,f) for msg in MSGS]
	#print ciphertexts[1].encode('hex')
	f.write(ciphertexts[0].encode('hex'))
	f.write('\n')
	f.write(ciphertexts[1].encode('hex'))
	f.close
	
main()


