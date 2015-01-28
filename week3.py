from Crypto.Hash import SHA256
from binascii import hexlify, unhexlify
BLOCKSIZE = 1024

def main():
	
	f = open('6 - 1 - Introduction (11 min).mp4', 'rb')

	bytesArray = f.read()

	#f.tell() return the current, last in this case, position
	last_block_pos = f.tell()

	#blocks "pointers"
	blocks = range(0, last_block_pos, BLOCKSIZE)

	#Read video in the reverse order
	blocks.reverse()

	previousHash = ""

	for blockPosition in blocks:
		#set the read pointer
		f.seek(blockPosition, 0)
		
		#read current block
		block = f.read(BLOCKSIZE)
		
		#calculate hash using  block content and the last hash cumputed
		hashObj = SHA256.new()
		hashObj.update(block)
		hashObj.update(previousHash)

		previousHash = hashObj.digest()
		
	#print h0
	print hexlify(previousHash)

main()
