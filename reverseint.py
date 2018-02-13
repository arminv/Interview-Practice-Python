import math

def reverseInt(n):
	"""
	Given an integer, return an integer that is the reverse
	ordering of numbers.

	>>> reverseInt(15)
	51
	>>> reverseInt(981) 
	189
	>>> reverseInt(500) 
	5
	>>> reverseInt(-15) 
	-51
	>>> reverseInt(-90) 
	-9
	"""
	
	# We need to define our own integer parser because Python does not have a built-in one!
	# This returns -1 if the input is -ve and 1 if +ve:
	sign = lambda x: math.copysign(1, x)

	# No need to worry if number is +ve, simply reverse the string:
	if sign(n) == 1:
		print str(n)[::-1].lstrip("0")


	# Note: If -ve, we need to remove the sign from integer, reverse it and 
	# then add back the sign.

	# Note: In case we have leading zeros, we need to use .lstrip("0") to remove
	# them while the object has a string format.

	elif sign(n) == -1:
		print int( str(abs(n))[::-1].lstrip("0") ) * -1


# ---------------------------------
# TESTS:

# This runs tests based on the docstring of the function:
if __name__ == '__main__':
	import doctest
	doctest.testmod()