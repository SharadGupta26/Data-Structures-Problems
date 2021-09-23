from LinkedListUtil import  *
def swap(list) :
    node1 = list.head
    node2 = node1.next

    while node1 and node2:
       node1.val, node2.val = node2.val, node1.val
       node1 = node2.next
       if node1 :
           node2 = node1.next

__name__ = '__main__'
arr = createLinkedList(map(int, input().split()))
swap(arr)
printLinkedList(arr)

