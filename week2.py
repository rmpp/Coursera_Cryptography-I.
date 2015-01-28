from binascii import hexlify, unhexlify
from Crypto.Cipher import AES


def main():
	
	ct1 = "28a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
	k1 = "140b41b22a29beb4061bda66b6747e14"
	iv1 = "4ca00ff4c898d61e1edbf1800618fb28"

	obj2 = AES.new(unhexlify(k1), AES.MODE_CBC, unhexlify(iv1))
	message = obj2.decrypt(unhexlify(ct1))
	print (message)
	
	ct2 = "b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
	k2 = "140b41b22a29beb4061bda66b6747e14"
	iv2 = "5b68629feb8606f9a6667670b75b38a5"

	obj2 = AES.new(unhexlify(k2), AES.MODE_CBC, unhexlify(iv2))
	message = obj2.decrypt(unhexlify(ct2))
	
	padding = int((hexlify(message[len(message)-1])), 16)
	print message[:(len(message)-padding)]



def main2():
	

	ct1 ="this is just a simple secret sms"
	k1 = "140b41b22a29beb4061bda66b6747e14"
	iv1 = "4ca00ff4c898d61e1edbf1800618fb28"
 	
	print hexlify(ct1)

	obj2 = AES.new(unhexlify(k1), AES.MODE_CBC, unhexlify(iv1))
	message = obj2.encrypt(ct1)
	print hexlify(message)
	
	obj2 = AES.new(unhexlify(k1), AES.MODE_CBC, unhexlify(iv1))
	message = obj2.decrypt((message))
	print (message)



main()
