"""
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
"""

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
  node = head
  #find one node before p and one node after q 
  #so we can re append list in reversed list
  while node is not None and node.next.value != p :
    node = node.next
  p = node
  while node is not None and node.value != q :
    node = node.next
  q = node.next
  node.next = None

  curr, prev = p.next, q
  while curr is not None :
    node = curr.next
    curr.next = prev
    prev = curr
    curr = node
  
  p.next = prev

  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
