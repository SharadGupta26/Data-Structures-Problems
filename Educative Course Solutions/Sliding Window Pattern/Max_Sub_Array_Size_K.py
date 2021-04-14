# Given an array of positive numbers and a positive number ‘k,’ 
# find the maximum sum of any contiguous subarray of size ‘k’.


def max_sub_array_of_size_k(k, arr):
  max_sum = 0
  for i in range(len(arr) - k) :
    temp_sum = sum(arr[i:i+k])
    if temp_sum > max_sum :
      max_sum = temp_sum
  return max_sum
