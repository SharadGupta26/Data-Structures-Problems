
'''
Solution not working yet
'''
from LinkedListUtil import *
def alternate_odd_even(list) :
    x,y = Node(-1), Node(-1)
    even,odd = x,y
    head = list.head
    while head :
        if head.val % 2 == 0 :
            even.next = head
            even = even.next
           
        else :
            odd.next = head
            odd = odd.next
        head = head.next
    odd.next = None
    even.next = None
    odd = y.next
    even = x.next
    print(odd)
    print(even)
    head = even
    tmp = head
    flag = False
    while even and odd :
        if flag :
            tmp.next = odd
            odd = odd.next
        else :
            tmp.next = even
            even = even.next
        tmp = tmp.next
        flag = not flag
    return head

__name__ = '__main__'
list = createLinkedList(map(int, input().split()))
head = alternate_odd_even(list)
#printLinkedList(list)
print(head)
