"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
"""

def make_squares(arr):
  squares = [0]*len(arr)
  i=0
  j= len(arr) - 1
  k = len(arr) - 1
  while i < j :
    ls = arr[i] ** 2
    rs = arr[j] ** 2
    if ls > rs :
      squares[k] = ls
      k -= 1
      i += 1
    else :
      squares[k] = rs
      k -= 1
      j -= 1
  return squares
