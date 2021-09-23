import LinkedListUtil

def remove_duplicates(list) :
    tmp = list.head
    while tmp :
        while tmp.next and tmp.val == tmp.next.val :
            tmp.next = tmp.next.next
        tmp = tmp.next

def remove_duplicate_rec(node) :
    if not node or not node.next :
        return
    if node.val == node.next.val :
        node.next = node.next.next
        remove_duplicate_rec(node)
    else :
        remove_duplicate_rec(node.next)
    return node

__name__ = '__main__'
arr = list(map(int, input().split()))
list = LinkedListUtil.createLinkedList(arr)
LinkedListUtil.printLinkedList(list)
remove_duplicates(list)
print()
LinkedListUtil.printLinkedList(list)

print ('using recursion')
print()

list = LinkedListUtil.createLinkedList(arr)
LinkedListUtil.printLinkedList(list)
remove_duplicate_rec(list.head)
print()
LinkedListUtil.printLinkedList(list)
print()
