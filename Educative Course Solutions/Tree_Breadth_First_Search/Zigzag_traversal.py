"""
Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.
"""

from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  elements = deque([root])
  flag = True
  while elements :
    size = len(elements)
    data = deque()
    toAppend = []
    while size > 0 :
      size -= 1
      n = elements.popleft()
      data.append(n.val) if flag else data.appendleft(n.val)
      if n.left :
        elements.append(n.left)
      if n.right :
        elements.append(n.right)
    result.append(list(data))
    flag = not flag
  return result

def pop(queue, flag) :
  return queue.popleft() if flag else queue.pop()
def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
