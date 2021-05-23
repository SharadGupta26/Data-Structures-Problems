"""
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
  allPaths = []
  traverse(root, [], allPaths, sum)
  return allPaths

def traverse(root, currentPath, allPaths, sum) :
  if not root :
    return
  currentPath.append(root.val)
  if sum == root.val and root.left is None and root.right is None :
    allPaths.append(list(currentPath))
  else :
    traverse(root.left,currentPath, allPaths, sum - root.val)
    traverse(root.right, currentPath, allPaths, sum-root.val)
  del currentPath[-1]
def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()
