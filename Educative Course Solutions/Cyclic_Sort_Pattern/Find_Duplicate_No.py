"""
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4
"""

def find_duplicate(nums):
  i = 0
  while i < len(nums) :
    j = nums[i] - 1
    if nums[i] != nums[j] :
      nums[i], nums[j] = nums[j], nums[i]
    elif i != j :
      return nums[i]
    else :
      i += 1
  return -1


def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()


"""
Solve it using fast and slow pointer without modifying input array

Problem 1: Can we solve the above problem in 
O
(
1
)
O(1) space and without modifying the input array?

Solution: While doing the cyclic sort, we realized that the array will have a cycle due to the duplicate number
 and that the start of the cycle will always point to the duplicate number. 
 This means that we can use the fast & the slow pointer method to find the duplicate number or the start of the cycle 
 similar to Start of LinkedList Cycle.


"""
def find_duplicate_fast_slow_pointer(arr):
  slow, fast = arr[0], arr[arr[0]]
  while slow != fast:
    slow = arr[slow]
    fast = arr[arr[fast]]

  # find cycle length
  current = arr[arr[slow]]
  cycleLength = 1
  while current != arr[slow]:
    current = arr[current]
    cycleLength += 1

  return find_start(arr, cycleLength)


def find_start(arr, cycleLength):
  pointer1, pointer2 = arr[0], arr[0]
  # move pointer2 ahead 'cycleLength' steps
  while cycleLength > 0:
    pointer2 = arr[pointer2]
    cycleLength -= 1

  # increment both pointers until they meet at the start of the cycle
  while pointer1 != pointer2:
    pointer1 = arr[pointer1]
    pointer2 = arr[pointer2]

  return pointer1


def main2():
  print(find_duplicate_fast_slow_pointer([1, 4, 4, 3, 2]))
  print(find_duplicate_fast_slow_pointer([2, 1, 3, 3, 5, 4]))
  print(find_duplicate_fast_slow_pointer([2, 4, 1, 4, 4]))


main2()
