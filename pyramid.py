def pyramid(n, row=0, level= ''):

	"""
	Write a function that accepts a positive number N.
	The function should console log a pyramid shape
	with N levels using the # character. Make sure the
	pyramid has HYPHENS on both the left *and* right hand sides.
	
	>>> pyramid(1)
	'#'
	
	>>> pyramid(2)
	'-#-'
	'###'
	
	>>> pyramid(3)
	'--#--'
	'-###-'
	'#####'
	
	>>> pyramid(4)
	'---#---'
	'--###--'
	'-#####-'
	'#######'
	
	# NOTE: I added hyphens instead of spaces.
	"""

# SOLUTION 1:

if row == n:
	pass

if len(level) == 2*n - 1:
	print (level)
	pyramid(n, row + 1)

midpoint = math.floor((2 * n - 1) / 2)
add = ''

if (midpoint - row <= len(level) and midpoint + row >= len(level)):
	add = '#'
else:
	add = ' '
	pyramid(n, row, level + add)


# ---------------------------------
# TESTS:
# This runs tests based on the docstring of the function:
if __name__ == '__main__':
	import doctest
	doctest.testmod()



