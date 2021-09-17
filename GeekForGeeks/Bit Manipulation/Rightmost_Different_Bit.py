class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        count = 1
        while True :
            if m & 1 != n & 1 :
                return count
            else :
                m = m >> 1
                n = n >> 1
                count += 1