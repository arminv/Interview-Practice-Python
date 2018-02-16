def anagrams(stringA, stringB):

	"""
	Check to see if two provided strings are anagrams of eachother.
	One string is an anagram of another if it uses the same characters
	in the same quantity. Only consider characters, not spaces
	or punctuation. Consider capital letters to be the same as lower case.

	>>> anagrams('rail safety', 'fairy tales')
	True

	>>> anagrams('RAIL SAFETY', 'fairy tales')
	True

	>>> anagrams('Hi there', 'Bye there')
	False

	>>> anagrams('hello', 'llohe')
	True

	>>> anagrams('Whoa! Hi!', 'Hi! Whoa!')
	True

	>>> anagrams('One One', 'Two two two')
	False

	>>> anagrams('One one', 'One one c')
	False

	>>> anagrams('A tree, a life, a bench', 'A tree, a fence, a yard')
	False
	"""

	# SOLUTION 1:

	# Note the use of ''.join() , sorted() and replace( , ) in Python 
	# vs .join(), .sort() and replace(regexp, ) in JS:

	def cleanString(str):
		return ''.join(sorted(str.replace(" ", "").lower()))


	return cleanString(stringA) == cleanString(stringB)




	# SOLUTION 2:

	# def buildCharMap(str):

	# 	charMap = {}

	# 	cleanStr = str.replace(" ", "").lower()

	# 	for char in cleanStr:

	# 		# Note how || from JS is implemented here:
	# 		if char not in charMap:
	# 			charMap[char] = 1
	# 		else:
	# 			charMap[char] += 1

	# 	return charMap


	# aCharMap = buildCharMap(stringA)
	# bCharMap = buildCharMap(stringB)


	# if len(aCharMap.keys()) != len(bCharMap.keys()):
	# 	return False

	# for char in aCharMap.keys():

	# 	# Note how (let - of - ) in JS is implemented in two steps here:
	# 	if char not in bCharMap:
	# 		return False
	# 	if aCharMap[char] != bCharMap[char]:
	# 		return False

	# return True


# ---------------------------------
# TESTS:

# This runs tests based on the docstring of the function:
if __name__ == '__main__':
	import doctest
	doctest.testmod()