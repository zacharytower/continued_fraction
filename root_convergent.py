from fractions import Fraction
from root_period import root_period

def root_convergent(root, n, additive = 0):
	'''
	Function finds the nth convergent of root "root" as a typical python fraction.
	i.e. root_convergent(root = 2, n = 3) = Fraction(7/5)

	as root 2 = [1;(2)]. Thus, root_convergent(2,3) = Fraction(7,5)

	1 + 1 / (2 + 1 / (2)) = 7/5

	^		 ^        ^
	a0		 a1		  a2
	1		 2		  3
	'''

	rp = root_period(root)

	if n == 1: # base case
		return rp[0] + additive
	

	repeating_part = rp[1:] # part of continued fraction that repeats
	# i.e. [2;(1,1,1,4)] --> [1,1,1,4] is repeating.

	an = repeating_part[(n - 2) % len(repeating_part)] # determine which part of continued fraction is needed as the denominator

	new_denominator = an + additive

	return root_convergent(root = root, n = n - 1, additive = Fraction(1, new_denominator))



