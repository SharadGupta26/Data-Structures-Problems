"""
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have 
O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false

"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

middle = None
def is_palindromic_linked_list(head):
  i,j = head, head
  while j is not None and j.next is not None :
    j = j.next.next
    i = i.next
  middle = reverse(i)
  copy = middle
  while middle is not None and head is not None:
    if head.value != middle.value :
      break
    head = head.next
    middle = middle.next
  
  reverse(copy)
  if head is None or middle is None :
    return True

  return False
 
def reverse(head) :
  prev = None 
  while head is not None :
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()







