"""
https://leetcode.com/problems/generate-parentheses/
"""

from collections import deque
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        elements = deque()
        elements.append(('(',1,0)) #touple of (running string, open count, close count)
        res=[]
        while elements :
            size = len(elements)
            while size:
                size -= 1
                elem = elements.popleft()
                if elem[1] == n and elem[2] == n:
                    res.append(elem[0])
                else :
                    if elem[1] < n :
                        elements.append((elem[0]+'(', elem[1]+1, elem[2]))
                    if elem[1] > elem[2] :
                        elements.append((elem[0]+')',elem[1], elem[2]+1))
        return res
            