"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

"""

def search_triplets(arr):
  triplets = []
  arr = sorted(arr) 
  for k in range(len(arr)) :
    val = arr[k]
    i,j = k+1, len(arr) - 1
    while i < j :
      sum = arr[i] + arr[j] 
      if sum == (-val) :
        triplets.append([val, arr[i], arr[j]])
        i += 1
        j -= 1
      elif sum < (-val) :
        i += 1
      else :
        j -= 1
      

  return triplets

"""
Handeled duplicates
https://leetcode.com/problems/3sum/
"""
from typing import List
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
      if len(nums) < 3 :
          return []
      res = []
      nums = sorted(nums)
      mem = set()
      for k in range(len(nums)-2) :
          if nums[k] in mem :
              continue
          start, end = k + 1, len(nums) - 1
          while start < end :
              sum = nums[k] + nums[start] + nums[end]
              if sum == 0 :
                  if nums[start]  not in mem or nums[end] not in mem :
                      res.append([nums[k] , nums[start] , nums[end]])
                      mem.add(nums[start])
                      mem.add(nums[end])
                  start += 1
                  end -= 1
              elif sum < 0 :
                  start += 1
              else :
                  end -= 1
          mem.clear()
          mem.add(nums[k])
      return res
        

"""
another approach to avoid duplicate
"""
def search_triplets2(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets


def search_pair(arr, target_sum, left, triplets):
  right = len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:  # found the triplet
      triplets.append([-target_sum, arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left - 1]:
        left += 1  # skip same element to avoid duplicate triplets
      while left < right and arr[right] == arr[right + 1]:
        right -= 1  # skip same element to avoid duplicate triplets
    elif target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum


def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()


print(search_triplets([-1,0,1,2,-1,-4]))

