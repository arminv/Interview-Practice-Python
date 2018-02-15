def capitalize(str):
	"""
	Write a function that accepts a string.  The function should
	capitalize the first letter of each word in the string then
	return the capitalized string.

	>>> capitalize('a short sentence')
	'A Short Sentence'

	>>> capitalize('a lazy fox')
	'A Lazy Fox'

	>>> capitalize('look, it is working!')
	'Look, It Is Working!'

	>>> capitalize('hi there, how is it going?')
	'Hi There, How Is It Going?'

	>>> capitalize('i love breakfast at bill miller bbq')
	'I Love Breakfast At Bill Miller Bbq'

	"""

	# SOLUTION 1:

	# upper() is the Python equivalent of JS toUpperCase():
	result = str[0].upper()

	for i in range(1, len(str)):

		if str[i - 1] == ' ' :
			result += str[i].upper()

		else:
			result += str[i]

	return result



	# SOLUTION 2:

	# words = []

	# for word in str.split(' '):
	# 	words.append(word[0].upper() + word[1:])

	# # We need to join all the elements of the list (words)
	# # into a string, separated by a whitespace: 

	# return ' '.join(words)


# ---------------------------------
# TESTS:

# This runs tests based on the docstring of the function:
if __name__ == '__main__':
	import doctest
	doctest.testmod()