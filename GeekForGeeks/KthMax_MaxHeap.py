"""
Kth max using Max heap.
Build max heap using given input array.
Pop max elemnt k times.
Top element will be kth max for given array.
"""

def buildheap(arr) :
    global heap
    global size
    heap = arr
    size = len(arr)
    i = (size) // 2
    while i >= 0 :
        heapify(i)
        i-=1

def heapify(i) :
    l = 2*i+1
    r = 2*i+2
    x = i
    if l < size and heap[x] < heap[l] :
        x=l
    if r < size and heap[x] < heap[r] : 
        x = r
    
    if x != i :
        heap[i], heap[x] = heap[x], heap[i]
        heapify(x)

def pop() :
    global size
    x = heap[0]
    heap[0] = heap[size-1]
    size-= 1
    heapify(0)
    
    return x

__name__ == '__main__'
arr = list(map(int, input().split()))
k = int(input())
buildheap(arr)
print(heap)

for i in range(k-1) :
    pop()
print('kth largest is %{0}', heap[0])