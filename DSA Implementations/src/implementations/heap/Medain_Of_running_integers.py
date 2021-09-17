import heapq

'''
Note : We don't have max heap in python heapq module. So solution to it is to insert -1 * i in min heap to convert it into max heap.

Simple logic
If i < last median, then insert in to max heap else insert into min heap
then rebalance heaps such that lenght of both heaps differs by max one element.
Then whichever heap has more elements, top of it will be median.
If both heap has same no of elements, avg of top of both will be median.    
'''

'''
In this approch we check i with median.
If smaller than median, insert in max heap else insert in min heap.
We keep heap balanced and leep calculating median at same time
'''
def median_of_running_integers_SOLUTION_1(i, minHeap, maxHeap, median) :
    
    if i < median :
        if len(maxHeap) > len(minHeap) :
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))
            heapq.heappush(maxHeap, -i)
            median = (minHeap[0] - maxHeap[0]) / 2
        elif len(maxHeap) < len(minHeap) :
            heapq.heappush(maxHeap, -i)
            median = (minHeap[0] - maxHeap[0]) / 2
        else :
            heapq.heappush(maxHeap, -i)
            median = -maxHeap[0]
    elif i > median :
        if len(minHeap) > len(maxHeap) :
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))
            heapq.heappush(minHeap, i)
            median = (minHeap[0] - maxHeap[0]) / 2
        elif len(minHeap) < len(maxHeap) :
            heapq.heappush(minHeap, i)
            median = (minHeap[0] - maxHeap[0]) / 2
        else :
            heapq.heappush(minHeap,i)
            median = minHeap[0]
    return median

'''
In this approcah we simply insert i
if i < median then insert in max heap else insert in min heap.
After inserting , we rebalance the heap and then finally calculate median.

'''
def median_of_running_integers_SOLUTION_2(i, minHeap, maxHeap, median) :
    #push in correct heap
    if i < median :
        heapq.heappush(maxHeap, -i)
    else :
        heapq.heappush(minHeap, i)

    #rebalancing heap
    if len(minHeap) > len(maxHeap) + 1 :
        heapq.heappush(maxHeap, -heapq.heappop(minHeap))
    elif len(maxHeap) > len(minHeap) + 1 :
        heapq.heappush(minHeap, -heapq.heappop(maxHeap))
    
    #calculating median
    if len(minHeap) == len(maxHeap) :
        median = (minHeap[0] - maxHeap[0]) / 2
    elif len(minHeap) > len(maxHeap) :
        median = minHeap[0]
    else :
        median = -maxHeap[0]
    return median

__name__=='__main__'
global minHeap
global maxHeap
global median
minHeap = []
maxHeap = []
median = -1
for _ in range(10) :
    i = int(input())
    median = median_of_running_integers_SOLUTION_2(i, minHeap, maxHeap, median);
    print("median = ", median)
       

