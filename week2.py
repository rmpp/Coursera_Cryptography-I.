from binascii import hexlify, unhexlify
from Crypto.Cipher import AES


def main():
	
	ct1 = "28a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
	k1 = "140b41b22a29beb4061bda66b6747e14"
	iv1 = "4ca00ff4c898d61e1edbf1800618fb28"

	obj2 = AES.new(unhexlify(k1), AES.MODE_CBC, unhexlify(iv1))
	message = obj2.decrypt(unhexlify(ct1))
	print (message)
	
	
	#########################################
	ct2 = "b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
	k2 = "140b41b22a29beb4061bda66b6747e14"
	iv2 = "5b68629feb8606f9a6667670b75b38a5"

	obj2 = AES.new(unhexlify(k2), AES.MODE_CBC, unhexlify(iv2))
	message = obj2.decrypt(unhexlify(ct2))
	
	padding = int((hexlify(message[len(message)-1])), 16)
	print message[:(len(message)-padding)]

	#########################################
	ct3= "0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
	k3 = "36f18357be4dbd77f050515c73fcf9f2"
	iv3 ="69dda8455c7dd4254bf353b773304eec"
	
	message = ''

	for pointer in range(0, len(ct3) + len (iv3), 32):
		text = ct3[pointer:pointer + 32]
		
		obj3 = AES.new(unhexlify(k3), AES.MODE_CTR, counter=lambda: unhexlify(iv3))
		dt = obj3.decrypt(unhexlify(text))
		
		message = message + dt
		
		
		iv3 = hex(int(iv3[:32], 16)+1)[2:][:-1]	  

	print((message))
	#########################################

	ct4= "e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
	k4 = "36f18357be4dbd77f050515c73fcf9f2"
	iv4 ="770b80259ec33beb2561358a9f2dc617"
		  
	
	message = ''

	for pointer in range(0, len(ct4) + len (iv4), 32):
		text = ct4[pointer:pointer + 32]
		
		obj4 = AES.new(unhexlify(k4), AES.MODE_CTR, counter=lambda: unhexlify(iv4))
		dt = obj4.decrypt(unhexlify(text))
		
		message = message + dt
		
		iv4 = hex(int(iv4[:32], 16)+1)[2:][:-1]	  

	print((message))

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
