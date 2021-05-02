"""
Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.
Example 2:

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
"""

def find_subarrays(arr, target):
  result = []
  start =0
  mul = 1
  for end in range(0, len(arr)) :
    if end > 0 and arr[end] < target : 
     result.append([arr[end]])
    mul *= arr[end]
    if mul < target :
      result.append(arr[start : end+1])
    while mul >= target:
      mul /= arr[start]
      start += 1
      if mul < target and start < end:
        result.append(arr[start : end+1])
  return result
