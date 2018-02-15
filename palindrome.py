def palindrome(str):
	"""
	Given a string, return true if the string is a palindrome
	or false if it is not.  Palindromes are strings that
	form the same word if it is reversed. *Do* include spaces
	and punctuation in determining if the string is a palindrome.
	
	>>> palindrome("aba")
	True

	>>> palindrome(" aba")
	False

	>>> palindrome("aba ")
	False

	>>> palindrome("greetings")
	False

	>>> palindrome("1000000001")
	True

	>>> palindrome("Fish hsif")
	False

	>>> palindrome("pennep")
	True

	"""

	# SOLUTION 1:

	# In Python we need to use enumerate() instead of .every() in JS:
	for i, char in enumerate(str):
		return char == str[len(str) - i - 1]


	# SOLUTION 2:
	
	# reversed_word = str[::-1]
	# return reversed_word == str


# ---------------------------------
# TESTS:

# This runs tests based on the docstring of the function:
if __name__ == '__main__':
	import doctest
	doctest.testmod()