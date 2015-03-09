from gmpy2 import mpz
import gmpy2

p = "13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171"
g = "11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568"
h = "3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333"

p = mpz(p)
g = mpz(g)
h = mpz(h)


#Meet in the middle

table = {}
B = 2**20

#First build a hash table of all possible values of the left hand side h/gx1 for x1=0,1,…,2^20.
for x1 in range(B):
	val = gmpy2.divm(h, pow(g,x1,p), p)
	try:
		table[val] = table[val] + (x1,)
	except Exception as e:
		table[val] = x1

#Then for each value x0=0,1,2,…,2^20 check if the right hand side (g^B)^x0 is in this hash table.
#If so, then you have found a solution (x0,x1) from which you can compute the required x as x=x0B+x1.
		
for x0 in range(B):
	aux = pow(g,x0*(B),p)
	if aux in table:
		x1= table[aux]
		x = ((x0 * B) + x1)%p
		print ("x-", x)
		break
