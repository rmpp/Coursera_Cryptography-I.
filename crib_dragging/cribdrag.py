from binascii import unhexlify
import sys

f = open('cripto','r')
c1 = f.readline()
c2 =f.readline()
f.close

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def main():
		
	# Unhexlify:convert hex in ascii
	
	# C1 xor C2 = xor = m1 xor m2
	
	xor1 = strxor(unhexlify(str(c1.strip())),unhexlify(str(c2.strip())))
	
	word = raw_input("Enter the word:>")
	
	#incvec=[0,1,2,3,4,5....,len(x)]
	incvec = range(0,len(xor1),1)
	
	# search
	for i in incvec:
		z = xor1[i:]
		#  If word is in m1 -> (m1 xor mt) xor word  = mt 
		print "[i-%d] - %s"% (i,strxor(z,word)),

main()	
while 1:
	print
	print "-------Repeat----- write english expressions and discover part of the secret message----"
	main()	
	
