#Given an array of positive numbers and a positive number ‘S,’ 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

def smallest_subarray_with_given_sum(s, arr):
  sum = 0
  start = 0
  min_length = len(arr)
  for end in range(len(arr)) :
    sum += arr[end]
    if sum >= s :
      while sum >= s :
        min_length = min(min_length, end-start+1)
        sum -= arr[start]
        start += 1
  return min_length
