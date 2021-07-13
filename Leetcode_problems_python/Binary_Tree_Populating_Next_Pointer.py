"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#O(n) space
from collections import deque
from typing import Node
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root :
            return None
        elements = deque([root])
        while elements :
            last = None
            size = len(elements) 
            while size :
                size-=1
                n = elements.popleft()
                if last :
                    last.next = n
                last = n
                if n.left :
                    elements.append(n.left)
                if n.right :
                    elements.append(n.right)
        return root
        

# my constant space solution 
# given tree is perfect binary tree and constraint says nodes are less than 4096 (2^12)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        arr = [None] * 12
        return self.traverse(root,0,arr)
        
    def traverse(self, root, level, arr) :
        if not root :
            return
        if arr[level] :
            arr[level].next = root
        arr[level] = root
        self.traverse(root.left, level+1, arr)
        self.traverse(root.right, level+1, arr)
        return root