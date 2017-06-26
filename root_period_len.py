import math

def root_period_len(n, b = 0, d = 1, original = 0, counter = 0):

	'''

	Returns the period of sqrt(n).
	i.e. cfp(7) = 4, as

	sqrt(7) = [2;(1,1,1,4)]

	b is what is added to n, and d is the denominator for both n and b.

	This recursive function is awkwardly written, but it works and is fairly fast.

	'''

	current_val = (math.sqrt(n) + b) / d

	a = math.floor(current_val)

	if current_val == original:
		return counter

	if original == 0:
		original = math.sqrt(n) + a

	if counter != 0: # we now have to take the reciprocal of the fraction:

		return root_period_len(n = n, b = d * a - b, d = (n - (b - d * a) ** 2) / d, original = original, counter = counter + 1)
	return root_period_len(n = n, b = a, d = n - a ** 2, original = original, counter = counter + 1)