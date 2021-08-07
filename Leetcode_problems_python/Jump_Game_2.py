
"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""
#https://leetcode.com/problems/jump-game-ii/
import math
class Solution:
   
    def jump(self, nums: List[int]) -> int:
        mem = [math.inf for i in range(len(nums))]
        if not nums :
            return 0
        def jump2(nums, pos, mem) :
            if pos >= len(nums) - 1:
                return 0
            if mem[pos] != math.inf :
                return mem[pos]
            val = nums[pos]
            for i in range(1,val + 1) :
                k = jump2(nums, pos + i, mem) +1
                mem[pos] =min(mem[pos], k)
            
            return mem[pos]
        res = jump2(nums,0, mem)
        #print(mem)
        return res
  