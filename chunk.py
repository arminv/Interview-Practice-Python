def chunk(array, size):
	"""Given an array and chunk size, divide the array into many subarrays
	where each subarray is of length size.

    >>> chunk([1, 2, 3, 4], 2)
    [[1, 2], [3, 4]]
    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    >>> chunk([1, 2, 3, 4, 5, 6, 7, 8], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8]]
    >>> chunk([1, 2, 3, 4, 5], 4)
    [[1, 2, 3, 4], [5]]
    >>> chunk([1, 2, 3, 4, 5], 10)
    [[1, 2, 3, 4, 5]]
    """


	chunked = []
	index = 0

	# In Python we need the built-in len() as there is no attribute .length as in JS:
	while index < len(array):
		# List (i.e. array) slicing works different too:
		chunked.append(array[index : (index+size)])
		index += size

	return chunked


# ---------------------------------
# TESTS:

# This runs tests based on the docstring of the function:
if __name__ == '__main__':
	import doctest
	doctest.testmod()

