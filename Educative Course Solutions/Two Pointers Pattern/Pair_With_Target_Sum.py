"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
"""
def pair_with_targetsum(arr, target_sum):
  i=0
  j = len(arr) - 1
  while i < j :
    sum = arr[i] + arr[j] 
    if sum == target_sum :
      return [i,j]
    elif sum < target_sum :
      i += 1
    else :
      j -= 1
  return [-1, -1]
