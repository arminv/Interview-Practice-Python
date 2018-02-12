# --- Directions
# Write a program that console logs the numbers
# from 1 to n. But for multiples of three print
# fizz instead of the number and for the multiples
# of five print buzz. For numbers which are multiples
# of both three and five print fizzbuzz.
# --- Example
#   fizzBuzz(5);
#   1
#   2
#   fizz
#   4
#   buzz


def fizzbuzz(n):
	for i in range(1, n+1):
		if i % 3 == 0 and i % 5 == 0:
			print "fizzbuzz"
			continue
		elif i % 3 == 0:
			print "fizz"
		elif i % 5 == 0:
			print "buzz"
		else:
			print str(i) + " (Not Fizzbuzz!)"

if __name__ == "__main__":
    print fizzbuzz(15)
