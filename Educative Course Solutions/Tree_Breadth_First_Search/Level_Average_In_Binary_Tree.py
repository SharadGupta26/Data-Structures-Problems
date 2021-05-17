from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  elements = deque([root])
  while elements :
    size = len(elements)
    total = 0
    for _ in range(size) :
      n = elements.popleft()
      total += n.val
      if n.left :
        elements.append(n.left)
      if n.right :
        elements.append(n.right)
    result.append(total / size)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()







