"""
Find the Smallest Missing Positive Number (medium) #
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:

Input: [3, 2, 5, 1]
Output: 4
"""

#my solution

def find_first_smallest_missing_positive(arr):
  i,j = 0,0
  for i in range(len(arr)) :
    #shifiting all negatives in starting
    if arr[i] <= 0 :
      arr[i], arr[j] = arr[j], arr[i]
      j += 1
    i += 1
  arr = arr[j:]
  i=0
  #placing all no in correct position
  while i < len(arr) :
    j = arr[i] - 1
    if j< len(arr) and arr[i] != arr[j] :
      arr[i], arr[j] = arr[j], arr[i]
    else :
      i+=1

  for i in range(len(arr)) :
    if arr[i] != i + 1 :
      return i+1
  return len(arr)+1


## their solution
#without shifting negatives, 
def find_first_smallest_missing_positive2(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  for i in range(n):
    if nums[i] != i + 1:
      return i + 1

  return len(nums) + 1


def main():
  print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
  print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
  print(find_first_smallest_missing_positive([3, 2, 5, 1]))


main()
