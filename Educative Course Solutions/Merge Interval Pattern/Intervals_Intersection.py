"""
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
"""

def merge(intervals_a, intervals_b):
  result = []
  i,j = 0,0
  while i  < len(intervals_a) and  j < len(intervals_b) :
    s1,e1 = intervals_a[i][0], intervals_a[i][1]
    s2,e2 = intervals_b[j][0], intervals_b[j][1]
    if overlap(s1,e1,s2,e2) :
      result.append([max(s1,s2), min(e1,e2)])
    if e1 == e2 : 
      i += 1
      j += 1
    elif e1 < e2 : 
      i += 1
    else :
      j += 1
  return result

def overlap(s1,e1,s2,e2) :
  if s1 > e2 or s2 > e1 :
    return False
  return True

def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
