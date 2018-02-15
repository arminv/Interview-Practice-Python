def maxChar(str):
	"""
	Given a string, return the character that is most
	commonly used in the string.

	>>> maxChar('abcdefghijklmnaaaaa')
	'a'
	
	>>> maxChar('ab1c1d1e1f1g1')
	'1'
	"""

	charMap = {}
	max = 0
	maxChar = ''

	for char in str:

		"""The key difference is here. In Python we need to
		explicitly access dictionary keys using the built-in
		function .keys() and check if there is one corresponding
		to the character: """

		if char in charMap.keys():
			charMap[char] += 1
		else:
			# If there is no corresponding key, we initialize
			# it to 1:
			charMap[char] = 1

	for char in charMap:

		if charMap[char] > max:
			max = charMap[char]
			maxChar = char

	return maxChar


# ---------------------------------
# TESTS:

# This runs tests based on the docstring of the function:
if __name__ == '__main__':
	import doctest
	doctest.testmod()