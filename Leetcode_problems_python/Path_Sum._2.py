"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.
https://leetcode.com/problems/path-sum-ii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, TreeNode
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.traverse(root, targetSum, [] , res)
        return res
    def traverse(self,root, target, currentPath, res) :
        if not root :
            return
        currentPath.append(root.val)
        if root.left is None and root.right is None and root.val == target :
            res.append(list(currentPath))
        if root.left :
            self.traverse(root.left, target- root.val, currentPath, res)
        if root.right :
            self.traverse(root.right, target - root.val, currentPath, res)
        del currentPath[-1]