"""
https://www.geeksforgeeks.org/find-number-pairs-xy-yx/

Given two arrays X[] and Y[] of positive integers, find a number of pairs such that x^y > y^x where x is an element from X[] and y is an element from Y[].

Examples:

Input: X[] = {2, 1, 6}, Y = {1, 5} 
Output: 3 
Explanation: There are total 3 pairs where pow(x, y) is greater than pow(y, x) Pairs are (2, 1), (2, 5) and (6, 1)

Input: X[] = {10, 19, 18}, Y[] = {11, 15, 9} 
Output: 2 
Explanation: There are total 2 pairs where pow(x, y) is greater than pow(y, x) Pairs are (10, 11) and (10, 15)


SOL

The problem can be solved in O(nLogn + mLogn) time. The trick here is if y > x then x^y > y^x with some exceptions. 

Following are simple steps based on this trick. 

Sort array Y[].
For every x in X[], find the index idx of the smallest number greater than x (also called ceil of x) in Y[] using binary search, or we can use the inbuilt function upper_bound() in algorithm library.
All the numbers after idx satisfy the relation so just add (n-idx) to the count.
Base Cases and Exceptions: 

Following are exceptions for x from X[] and y from Y[]   
If x = 0, then the count of pairs for this x is 0.
If x = 1, then the count of pairs for this x is equal to count of 0s in Y[].
x smaller than y means x^y is greater than y^x.
    x = 2, y = 3 or 4
    x = 3, y = 2

"""

# Python3 program to find the number
# of pairs (x, y) in an array
# such that x^y > y^x
import bisect

# Function to return count of pairs
# with x as one element of the pair.
# It mainly looks for all values in Y
# where x ^ Y[i] > Y[i] ^ x


def count(x, Y, n, NoOfY):

	# If x is 0, then there cannot be
	# any value in Y such that
	# x^Y[i] > Y[i]^x
	if x == 0:
		return 0

	# If x is 1, then the number of pairs
	# is equal to number of zeroes in Y
	if x == 1:
		return NoOfY[0]

	# Find number of elements in Y[] with
	# values greater than x, bisect.bisect_right
	# gets address of first greater element
	# in Y[0..n-1]
	idx = bisect.bisect_right(Y, x)
	ans = n - idx

	# If we have reached here, then x must be greater than 1,
	# increase number of pairs for y=0 and y=1
	ans += NoOfY[0] + NoOfY[1]

	# Decrease number of pairs
	# for x=2 and (y=4 or y=3)
	if x == 2:
		ans -= NoOfY[3] + NoOfY[4]

	# Increase number of pairs
	# for x=3 and y=2
	if x == 3:
		ans += NoOfY[2]

	return ans

# Function to return count of pairs (x, y)
# such that x belongs to X,
# y belongs to Y and x^y > y^x


def count_pairs(X, Y, m, n):

	# To store counts of 0, 1, 2, 3,
	# and 4 in array Y
	NoOfY = [0] * 5
	for i in range(n):
		if Y[i] < 5:
			NoOfY[Y[i]] += 1

	# Sort Y so that we can do binary search in it
	Y.sort()
	total_pairs = 0 # Initialize result

	# Take every element of X and
	# count pairs with it
	for x in X:
		total_pairs += count(x, Y, n, NoOfY)

	return total_pairs


# Driver Code
if __name__ == '__main__':

	X = [2, 1, 6]
	Y = [1, 5]
	print("Total pairs = ",
		count_pairs(X, Y, len(X), len(Y)))

# This code is contributed by shaswatd673

