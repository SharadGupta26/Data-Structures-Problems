"""
Kth max element using min heap.
In this we create min heap for first k elements from given array.
Then for remaining k elements, we replace min element in heap (top element) with element of array.
finally top element would be kth max of given array.


Logic works as this
In a group of k distinct elemtns, smallest element is kth maximum of group

arr = [33,2,1,4, 55]
k = 3
min heap of k elements = [1,2,33]
kth max so far = 1

4 > 1 so replace 1 with 4 and heapify
min heap = [2,4,33]

55 > 2 so replace 4 with 55 and heapify
min heap = [4,33,55]

kth max = 4

"""

def buildHeap(arr) :
    global heap
    global size
    heap = arr
    size = len(arr)
    i = size //2
    while i >= 0 :
        heapify(i)
        i -= 1

def heapify(i) :
    l = i*2 + 1
    r = i*2 + 2
    x = i
    if l < size and heap[x] > heap[l] :
        x = l
    if r < size and heap[x] > heap[r] :
        x = r
    if x != i :
        heap[x], heap[i] = heap[i], heap[x]
        heapify(x)

def replaceMin(i) :
    heap[0] = i
    heapify(0)


#driver function
__name__ == '__main__'
arr = list(map(int, input().split()))
k = int(input())
buildHeap(arr[0:k])
print(heap)
for i in range(k, len(arr)) :
    if arr[i] > heap[0] :
        replaceMin(arr[i])
print(heap)
print("kth max is " , heap[0])

 
