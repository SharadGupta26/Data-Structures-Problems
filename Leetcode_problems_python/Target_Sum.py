"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

https://leetcode.com/problems/target-sum/
"""

# my solution
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.findWays(nums, target, 0)
    def findWays(self,nums, target, pos) :
        #print(target, pos)
        if target == 0 and pos > len(nums)-1:
            return 1
        if pos >= len(nums) :
            return 0
        
        return self.findWays(nums, target - nums[pos], pos + 1) + self.findWays(nums, target + nums[pos], pos+1)

# using Memoization
import math
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = [[-math.inf for i in range(3000)] for i in range(len(nums))]
        return self.findWays(nums, target, 0, mem)
    def findWays(self,nums, target, pos, mem) :
        #print(target, pos)
        if target == 0 and pos == len(nums):
            return 1
        if pos >= len(nums) :
            return 0
        if mem[pos][target + 1000] != -math.inf :
            return mem[pos][target + 1000]
        a = self.findWays(nums, target - nums[pos], pos + 1, mem)
        b = self.findWays(nums, target + nums[pos], pos+1, mem)
        mem[pos][target + 1000] = a + b
        return  a+b 

"""
DP Solution

public class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        int[][] dp = new int[nums.length][2001];
        dp[0][nums[0] + 1000] = 1;
        dp[0][-nums[0] + 1000] += 1;
        for (int i = 1; i < nums.length; i++) {
            for (int sum = -1000; sum <= 1000; sum++) {
                if (dp[i - 1][sum + 1000] > 0) {
                    dp[i][sum + nums[i] + 1000] += dp[i - 1][sum + 1000];
                    dp[i][sum - nums[i] + 1000] += dp[i - 1][sum + 1000];
                }
            }
        }
        return S > 1000 ? 0 : dp[nums.length - 1][S + 1000];
    }
}"""