"""
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example 1:

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.
Example 2:

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.
Example 3:

Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
"""

def find_first_k_missing_positive(arr, k):
  missingNumbers = []
  i,n = 0, len(arr)
  #placing all no in their crrect pos
  while i < n :
    j = arr[i] - 1
    if j > 0 and j <= len(arr) - 1 and arr[i] != arr[j] :
      arr[i], arr[j] = arr[j], arr[i]
    else :
      i += 1
  #print(arr)
 
  extras = set()
  for i in range(n) :
    if arr[i] != i + 1 :
      missingNumbers.append(i+1)
      extras.add(arr[i])
      if len(missingNumbers) == k :
        return missingNumbers
  j = len(arr)+1
  while len(missingNumbers) != k:
    if j not in extras :
      missingNumbers.append(j)
    j += 1
  return missingNumbers


def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))


main()