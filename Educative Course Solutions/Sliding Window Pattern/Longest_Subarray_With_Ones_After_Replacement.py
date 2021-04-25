#Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
# find the length of the longest contiguous subarray having all 1s.

def length_of_longest_substring(arr, k):
  count = 0
  start = 0
  zeros = 0
  for end in range(len(arr)) :
     if arr[end] == 0 :
       zeros += 1
     count = max(count, end-start + 1)
     while zeros > k :
       if arr[start] == 0 :
         zeros -= 1
       start += 1
  return count
