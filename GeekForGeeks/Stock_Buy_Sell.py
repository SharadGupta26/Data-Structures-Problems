
"""
The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
Note: There may be multiple possible solutions. Return any one of them. Any correct solution will result in an output of 1, whereas wrong solutions will result in an output of 0.

Example 1:

Input:
N = 7
A[] = {100,180,260,310,40,535,695}
Output:
1
Explanation:
One possible solution is (0 3) (4 6)
We can buy stock on day 0,
and sell it on 3rd day, which will 
give us maximum profit. Now, we buy 
stock on day 4 and sell it on day 6.
Example 2:

Input:
N = 5
A[] = {4,2,2,2,4}
Output:
1
Explanation:
There are multiple possible solutions.
one of them is (3 4)
We can buy stock on day 3,
and sell it on 4th day, which will 
give us maximum profit.

https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/

P.S. If we are allowed to buy and sell only once, 
https://www.cdn.geeksforgeeks.org/maximum-difference-between-two-elements/
"""
class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, a, n):
	    i=1
	    res = []
	    while i < n :
	        if a[i] - a[i-1] > 0 :
	            res.append([i-1,i])
	        i += 1
	    #print(res)
	    return res




# Python3 Program to find 
# best buying and selling days

# This function finds the buy sell
# schedule for maximum profit
def stockBuySell(price, n):
    
    # Prices must be given for at least two days
    if (n == 1):
        return
    
    # Traverse through given price array
    i = 0
    while (i < (n - 1)):
        
        # Find Local Minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
        while ((i < (n - 1)) and 
                (price[i + 1] <= price[i])):
            i += 1
        
        # If we reached the end, break
        # as no further solution possible
        if (i == n - 1):
            break
        
        # Store the index of minima
        buy = i
        i += 1
        
        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1
            
        # Store the index of maxima
        sell = i - 1
        
        print("Buy on day: ",buy,"\t",
                "Sell on day: ",sell)
        
# Driver code

# Stock prices on consecutive days
price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)

# Function call
stockBuySell(price, n)

# This is code contributed by SHUBHAMSINGH10


