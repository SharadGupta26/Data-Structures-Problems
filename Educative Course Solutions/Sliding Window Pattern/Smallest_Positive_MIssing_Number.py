def segregate(arr, size):
    j = 0
    for i in range(size):
        if (arr[i] <= 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1 # increment count of non-positive integers
    return j


''' Find the smallest positive missing number
in an array that contains all positive integers '''

"""
We are using abs() to retrieve value previously present at this index
"""
def findMissingPositive(arr, size):
    
    # Mark arr[i] as visited by
    # making arr[arr[i] - 1] negative.
    # Note that 1 is subtracted
    # because index start
    # from 0 and positive numbers start from 1
    print(arr)
    for i in range(size):
        if (abs(arr[i]) - 1 < size):
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        print(arr)
            
    # Return the first index value at which is positive
    for i in range(size):
        if (arr[i] > 0):
            
            # 1 is added because indexes start from 0
            return i + 1
    return size + 1

''' Find the smallest positive missing
number in an array that contains
both positive and negative integers '''
def findMissing(arr, size):
    
    # First separate positive and negative numbers
    shift = segregate(arr, size)
    
    # Shift the array and call findMissingPositive for
    # positive part
    return findMissingPositive(arr[shift:], size - shift)
    
# Driver code
arr = [2,1,3,7,6,8,15] 
arr_size = len(arr)
missing = findMissing(arr, arr_size)
print("The smallest positive missing number is ", missing)

# This code is contributed by Shubhamsingh10