import urllib2
import sys
from binascii import hexlify, unhexlify

TARGET = 'http://crypto-class.appspot.com/po?er='

#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


class PaddingOracle(object):
    def query(self, q):
		
        target = TARGET + urllib2.quote(q.encode("hex"))    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
            #return True
        except urllib2.HTTPError, e:          
            #print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding



if __name__ == '__main__':
	po=PaddingOracle()
	mOriginal = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'.decode('hex')
	msg = ""
	
	blocks = [mOriginal[:16], mOriginal[16:32], mOriginal[32:48], mOriginal[48:64]]
	
	for i in range(0, 3):
		currentBlock = blocks[i]
		print "current block-"+hexlify(currentBlock)
		bmsg = []
		for byte in reversed(range(16)):
			testBlock = list(currentBlock)
			for index, msgchar in enumerate(reversed(bmsg)):
				testBlock[16-(index+1)] = strxor(testBlock[16-(index+1)], msgchar)
			padding_num = 16 - byte
			padding = chr(padding_num)
			print "padding-" + hexlify(padding)
			#Xor padding
			for padInt in range(1, padding_num + 1):
				#print hexlify(testBlock[16-padInt])
				testBlock[16-padInt] = strxor(testBlock[16-padInt], padding)
			#Xor g
			for guess_num in range(2, 256):
				guess = chr(guess_num)
				guessBlock = list(testBlock)
				#m xor g xor pad
				guessBlock[byte] = strxor(guessBlock[byte], guess)
				#dont test using all msg, prevent from recev ok
				if po.query(''.join(blocks[i-1:i] + guessBlock + [blocks[i + 1]])):
					#pad ok, save guess
					bmsg.insert(0, guess)
					print bmsg
					print hexlify(guess)
					break
		msg += ''.join(bmsg)
	print msg

