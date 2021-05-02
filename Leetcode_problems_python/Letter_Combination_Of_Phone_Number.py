"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2':'abc', '3':'def', '4' : 'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        data = [phone[c] for c in digits]
        print(data)
        return self.conbinations(data)
        
    def conbinations(self, data) :
        if len(data) == 0 :
            return []
        if len(data) == 1 :
            return list(data[0])
        res = []
        w = data[0]
        arr = self.conbinations(data[1:])
        for c in w :
            for a in arr :
                res.append(c+a)
        return res