"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

"""
"""
https://leetcode.com/problems/4sum/solution/
"""
#handeled duplicates with mem
class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        res = []
        arr = sorted(arr)
        mem = set()
        for k in range(len(arr)) :
            if arr[k] in mem :
                continue
            for l in range(k+1, len(arr)) :
                if arr[l] in mem :
                    continue
                i,j = l+1, len(arr) - 1
                while  i<j :
                    a,b,c,d = arr[k], arr[l], arr[i], arr[j]
                    if sum((a,b,c,d)) == target :
                        if c not in mem or d not in mem :
                            res.append([a,b,c,d])
                            mem.add(c)
                            mem.add(d)
                        i+=1
                        j-=1
                    elif sum((a,b,c,d)) < target :
                        i+=1
                    else :
                        j-=1
                mem.clear()
                mem.add(arr[l])
            mem.clear()
            mem.add(arr[k])
        return res

                    
                
        