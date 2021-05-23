"""
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  return traverse(root, sequence, 0)  

def traverse(root, sequence, pos) :
  if not root :
    return False
  if pos >= len(sequence) :
    return False
  if sequence[pos] != root.val :
    return False
  if pos == len(sequence) - 1 and sequence[pos] == root.val and root.left is None and root.right is None :
    return True
  return traverse(root.left, sequence, pos + 1) or traverse(root.right, sequence, pos + 1)

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
