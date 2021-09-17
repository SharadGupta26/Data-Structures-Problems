
def isHeap(arr, i ,n) :
    if i >= (n-2) /2 :
        return True
    return arr[i] >= arr[2*i+1] and arr[i] > arr[2*i+2] and isHeap(arr, 2*i+1, n) and isHeap(arr, 2*i+2, n)

__name__=='__main__'
#arr = list(map(int, input().split()))
x = isHeap([1,3,4,1,2], 0, 5)
print(x)