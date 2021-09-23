import LinkedListUtil
'''
 following cases to be handled. 

x and y may or may not be adjacent.
Either x or y may be a head node.
Either x or y may be the last node.
x and/or y may not be present in the linked list.
'''
def swap(list, x, y) :
    head = list.head
    prevx,prevy=None,None
    nodex, nodey = head, head
    while nodex and nodex.val != x: 
        prevx = nodex
        nodex = nodex.next
    while nodey and nodey.val != y :
        prevy = nodey
        nodey = nodey.next
    
    #node not found
    if not nodex or not nodey :
        return
    
    if prevx :
        prevx.next = nodey
    else :
        list.head = nodey

    if prevy :
        prevy.next = nodex
    else :
        list.head = nodex

    tmp = nodex.next
    nodex.next = nodey.next
    nodey.next = tmp

__name__ = '__main__' 
arr = list(map(int, input().split()))
list = LinkedListUtil.createLinkedList(arr)
swap(list, 5, 1)
LinkedListUtil.printLinkedList(list)