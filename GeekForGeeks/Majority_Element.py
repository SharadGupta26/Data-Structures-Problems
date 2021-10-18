"""
Given an array of size n, one element is repeated by more than n/2 times. Find the element.

https://www.geeksforgeeks.org/majority-element/

Solution using Moore's Voting algorithm.
"""

def majorityElem(arr :list) :
    candidate = arr[0]
    count = 0
    #first loop to find candidate of majority element.
    #If majority element exist, it will definately return majority element
    for i in range(1,len(arr)) :
        if arr[i] == candidate :
            count += 1
        else :
            count -= 1
        
        if count == 0 :
            count = 1
            candidate = arr[i]

    #second loop to make sure candidate is majority element
    #meaing it must occur more than n/2 times
    majority = 0
    for i in range(len(arr)) :
        if arr[i] == candidate :
            majority += 1

    print('majority element is ', candidate) if majority > len(arr) / 2 else print('No majority element')

__name__ = '__main__'
arr = list(map(int, input().split()))
majorityElem(arr)

    
