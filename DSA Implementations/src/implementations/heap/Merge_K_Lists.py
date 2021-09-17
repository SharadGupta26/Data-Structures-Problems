import heapq
import math

def insert(x) :
    global heap
    heapq.heappush(heap, x)

def pop() :
    global size
    x = heapq.heappop(heap)
    return x

"""
for merging k sorted lists
create min heap. Insert first element of each row in heap.
now untill heap is empty, pop element from heap, store it in resutl array. and insert next elemnt from same row again.
 
So this way, min of all arrays will be on top of heap always.
"""
__name__ =='__main__'
global heap
heap = []
size = 0

arr = []
for i in range(5) :
    arr.append(sorted(list(map(int, input().split()))))

for i in range(len(arr)) :
    x = arr[i]
    insert((x[0], i, 1))
#print(heap)
res = []
while len(heap) > 0 :
    x = pop()
    res.append(x[0])
    row = x[1]
    col = x[2]
    if col < len(arr[row]) :
        insert((arr[row][col], row, col+1))
    #elif math.inf != x[0]:
        #insert((math.inf, row, col+1))

print(res)
    


