from functools import reduce

def reverse(str):
	"""
	Given a string, return a new string with the reversed
	order of characters.

	>>> reverse('apple')
	'elppa'

	>>> reverse('hello')
	'olleh'

	>>> reverse('Greetings!')
	'!sgniteerG'

	>>> reverse('abcd')
	'dcba'

	>>> reverse('  abcd')
	'dcba  '
	"""

	# SOLUTION 1:

	# Although reduce() is included as part of the standard library,
	# we still need to import it as it is part of the 'functools' module:

	reversed = reduce((lambda x , y: y + x), str)

	return reversed


	# SOLUTION 2:

	# return str[::-1] 


	# SOLUTION 3:

	# reversed = ''

	# for char in str:
	# 	reversed = char + reversed

	# return reversed


# ---------------------------------
# TESTS:

# This runs tests based on the docstring of the function:
if __name__ == '__main__':
	import doctest
	doctest.testmod()