class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        if n == 0 :
            return 0
        count = 1
        while True :
            if n & 1 == 1 :
                return count
            else :
                n = n >> 1
                count += 1
