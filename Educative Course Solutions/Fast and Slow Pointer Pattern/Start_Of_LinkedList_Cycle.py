'''
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
'''
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  i,j = head,head
  cycle = 0
  while j != None and j.next != None :
    i = i.next
    j = j.next.next
    if i == j :
      cycle = findLength(i)
      break
  i,j = head,head
  while cycle > 0 :
    i = i.next
    cycle -= 1
  
  while i != j :
    i = i.next
    j = j.next

  return i

def findLength(slow) :
  i=slow
  length = 0
  while True :
    i = i.next
    length += 1
    if i == slow :
      return length


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
