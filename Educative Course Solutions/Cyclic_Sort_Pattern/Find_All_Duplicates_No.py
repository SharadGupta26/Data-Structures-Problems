"""

We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""

def find_all_duplicates(nums):
  duplicateNumbers = []
  i = 0
  while i < len(nums) :
    if nums[i] == -1 :
      i += 1
      continue
    j = nums[i]-1
    if nums[i] != nums[j] :
      nums[i], nums[j] = nums[j], nums[i]
    elif i != j :
      duplicateNumbers.append(nums[i])
      nums[j] = -1
      #i += 1
    else :
      i += 1
  
  return duplicateNumbers
