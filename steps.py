def steps(n, row = 0, stair = ''):
	"""
	Write a function that accepts a positive number N.
	The function should console log a step shape
	with N levels using the # character. Make sure the
	step has HYPHENS on the right hand side!

	>>> steps(2)
	#-
	##
	
	>>> steps(3)
	#--
	##-
	###

	>>> steps(4)
	#---
	##--
	###-
	####
	"""
	# NOTE: I added hyphens instead of spaces to the right side
	# of stair. It is easier to see what is going on (also better for testing!) 


	# SOLUTION 1:

	if n == row:
		return

	if n == len(stair):
		print(stair)
		return steps(n, row + 1)

	if len(stair) <= row:
		add = '#'

	else:
		# Original solution adds ' ', we add '-' instead for clarity:
		add = '-'

	steps(n, row, stair + add)



	# SOLUTION 2:

	# for row in range(0, n):
	# 	stair = ""

	# 	for column in range(0, n):
	# 		if column <= row:
	# 			stair += '#'
	# 		else:
	# 			stair += '-'

	# 	print stair


# ---------------------------------
# TESTS:

# This runs tests based on the docstring of the function:
if __name__ == '__main__':
	import doctest
	doctest.testmod()