
"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.
"""
"""
This problem follows the Subsets pattern and we can follow a similar Breadth First Search (BFS) approach. The only additional thing we need to do is handle duplicates. Since the given set can have duplicate numbers, if we follow the same approach discussed in Subsets, we will end up with duplicate subsets, which is not acceptable. To handle this, we will do two extra things:

Sort all numbers of the given set. This will ensure that all duplicate numbers are next to each other.
Follow the same BFS approach but whenever we are about to process a duplicate (i.e., when the current and the previous numbers are same), instead of adding the current number (which is a duplicate) to all the existing subsets, only add it to the subsets which were created in the previous step.
Let’s take Example-2 mentioned above to go through each step of our algorithm:

Given set: [1, 5, 3, 3]  
Sorted set: [1, 3, 3, 5]
Start with an empty set: [[]]
Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
Add the second number (3) to all the existing subsets: [[], [1], [3], [1,3]].
The next number (3) is a duplicate. If we add it to all existing subsets we will get:
    [[], [1], [3], [1,3], [3], [1,3], [3,3], [1,3,3]]
We got two duplicate subsets: [3], [1,3]  
Whereas we only needed the new subsets: [3,3], [1,3,3]  
To handle this instead of adding (3) to all the existing subsets, we only add it to the new subsets which were created in the previous (3rd) step:

    [[], [1], [3], [1,3], [3,3], [1,3,3]]
Finally, add the forth number (5) to all the existing subsets: [[], [1], [3], [1,3], [3,3], [1,3,3], [5], [1,5], [3,5], [1,3,5], [3,3,5], [1,3,3,5]]
"""

def find_subsets(nums):
  nums.sort()
  subsets = []
  start, end = 0,0
  subsets.append([])
  for i in range(len(nums)) :
    val = nums[i]
    start = 0
    if i > 0 and nums[i-1] == val :
      start = end + 1
    end = len(subsets) -1
    for j in range(start, end+1) :
      set1 = []
      set1.extend(subsets[j])
      set1.append(val)
      subsets.append(set1)

  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()

