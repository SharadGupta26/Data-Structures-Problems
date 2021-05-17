"""
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.
"""
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = deque()
  elements = deque([root])
  while elements :
    size = len(elements)
    data = []
    while size > 0 :
      size -= 1
      n = elements.popleft()
      data.append(n.val)
      if n.left :
        elements.append(n.left)
      if n.right :
        elements.append(n.right)
    result.appendleft(data)
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()
