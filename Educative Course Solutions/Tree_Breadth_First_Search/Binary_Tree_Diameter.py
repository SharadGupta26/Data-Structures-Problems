"""
Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.

At every step, we need to find the height of both children of the current node.
For this, we will make two recursive calls similar to DFS.
The height of the current node will be equal to the maximum of the heights of its left or right children, plus ‘1’ for the current node.
The tree diameter at the current node will be equal to the height of the left child plus the height of the right child plus ‘1’ for the current node: diameter = leftTreeHeight + rightTreeHeight + 1. To find the overall tree diameter, we will use a class level variable. This variable will store the maximum diameter of all the nodes visited so far, hence, eventually, it will have the final tree diameter.



"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeDiameter:

  def __init__(self):
    self.treeDiameter = 0
  def find_diameter(self, root):
    if not root :
      return 0
    d = self.height(root.left) + self.height(root.right) + 1
    self.treeDiameter = max (d, self.treeDiameter)
    self.find_diameter(root.left)
    self.find_diameter(root.right)
    return self.treeDiameter

  def height(self,root) :
    if not root :
      return 0
    ans =  1 + max (self.height(root.left) , self.height(root.right))
    return ans
  

def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()







