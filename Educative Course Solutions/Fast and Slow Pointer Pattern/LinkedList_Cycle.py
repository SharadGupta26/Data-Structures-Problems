"""
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
  if head.next == None :
    return False
  p1  = head
  p2 = head.next.next
  while p2 != None and p2.next != None :
    if p1 == p2 :
      return True
    p1 = p1.next
    p2 = p2.next.next

  return False


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))


main()
