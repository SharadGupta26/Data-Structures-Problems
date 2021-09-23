
from Node import *
from LinkedListUtil import *
'''
In this approach
    Find middle
    reverse second half
    check first half and second half
    reveser second half back

Another approach is to use stack.

'''
def checkPalindrome(list : LinkedList) :
    #find middle and node before middle
    prev_of_middle, middle = getMiddle(list)

    #reverse second half of list
    middle = reverse(middle)
    tmp1 = list.head
    tmp2 = middle
    palindrome = True
    while tmp2 :
        if tmp1.val != tmp2.val :
            palindrome = False
            break
        else :
            tmp1 = tmp1.next
            tmp2 = tmp2.next
    #reveser back second half
    middle = reverse(middle)

    #attach second half back to list
    prev_of_middle.next = middle
    return palindrome




def getMiddle(list: LinkedList) :
 tmp = list.head
 tmp2 = list.head
 prev = None
 while tmp2 and tmp2.next: 
     tmp2 = tmp2.next.next
     prev = tmp
     tmp = tmp.next
 return (prev, tmp)

def reverse(node) :
    prev = None
    tmp = node
    while tmp:
        next = tmp.next
        tmp.next = prev
        prev = tmp
        tmp = next
    return prev


__name__ = '__main__'
arr = list(map(int, input().split()))
list = createLinkedList(arr)
palindrome = checkPalindrome(list)
printLinkedList(list)
print()
print(palindrome)