from LinkedListUtil import *
def reverse (head, k) :
    if not head :
        return None
    node = head
    for _ in range(k-1):
        if node.next :
            node = node.next
    tmp = node.next
    node.next = None
    rhead, rtail = reverseUtil(head)
    rtail.next = reverse(tmp, k)
    return rhead


def reverse_alternate_k_nodes (head, k, flag) :
    if not head :
        return None
    node = head
    for _ in range(k-1):
        if node.next :
            node = node.next
    tmp = node.next
    node.next = None
    if flag :
        rhead, rtail = reverseUtil(head)
    else :
        rhead, rtail = head, node
    rtail.next = reverse_alternate_k_nodes(tmp, k, not flag)
    return rhead

def reverseUtil(node) :
    prev = None
    tmp = node
    while node :
        next = node.next
        node.next = prev
        prev = node
        node = next
    return (prev, tmp)

__name__ = '__main__'
data = list(map(int, input().split()))
arr = createLinkedList(data)
print('reversing in group of k nodes')
arr.head = reverse(arr.head, 3)
printLinkedList(arr)

print()
print('reversing alternate k nodes')
arr = createLinkedList(data)
arr.head = reverse_alternate_k_nodes(arr.head, 3, True)
printLinkedList(arr)
