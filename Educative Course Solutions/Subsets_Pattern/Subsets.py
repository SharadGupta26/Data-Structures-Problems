'''
Given a set with distinct elements, find all of its distinct subsets.

To generate all subsets of the given set, we can use the Breadth First Search (BFS) approach. We can start with an empty set, 
iterate through all numbers one-by-one, and add them to existing sets to create new subsets.

Let’s take the example-2 mentioned above to go through each step of our algorithm:

Given set: [1, 5, 3]

Start with an empty set: [[]]
Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];
Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].

'''

def find_subsets(nums):
  subsets = []
  subsets.append([])
  for i in nums :
    for j in range(len(subsets)):
      sets = subsets[j]
      temp = []
      temp.extend(sets)
      temp.append(i)
      subsets.append(temp)
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
