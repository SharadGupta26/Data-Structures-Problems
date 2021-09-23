
from LinkedListUtil import *

'''
using three pointers
'''
def reverse(node) :
    prev = None
    while node :
        tmp = node.next
        node.next = prev
        prev = node
        node = tmp
    return prev

def reverse_rec(node) :
    if node == None or node.next == None:
        return  node
    rest = reverse_rec(node.next)
    node.next.next = node
    node.next = None
    return rest

if __name__ == '__main__' : 
    arr = list(map(int, input().split()))
    lst = createLinkedList(arr)
    print('original')
    printLinkedList(lst)
    lst.head = reverse_rec(lst.head)
    print('reversed')
    printLinkedList(lst)

