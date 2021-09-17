"""
You are given N elements and your task is to Implement a Stack in which you can get minimum element in O(1) time.

https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
"""

class stack:
    def __init__(self):
        self.s=[]
        self.mins=[]

    def push(self,x):
        if len(self.mins) == 0 or x <= self.mins[-1] :
            self.mins.append(x)
        self.s.append(x)

    def pop(self):
        if(len(self.s) == 0) :
            return -1
        x = self.s.pop()
        if len(self.mins) > 0  and x == self.mins[-1] :
            self.mins.pop()
        return x
        

    def getMin(self):
        if len(self.mins) == 0 :
            return -1
        return self.mins[-1]