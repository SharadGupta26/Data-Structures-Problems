"""
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""

"""
For maximum depth, keep traversing till last node
"""

from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  depth = 0
  elements = deque([root])
  while elements :
    size = len(elements)
    while size > 0 :
      size -= 1
      n = elements.popleft()
      if not n.left and not n.right :
        return depth + 1
      if n.left :
        elements.append(n.left)
      if n.right :
        elements.append(n.right)
    depth += 1  
  return -1


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
