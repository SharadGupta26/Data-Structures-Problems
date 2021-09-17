from Node import *

'''
create a linked list from given array
'''
def createLinkedList(arr) :
    list = LinkedList()
    tmp = list.head
    for i in arr :
        node = Node(i)
        if not list.head :
            list.head = node
            tmp = node
        else :
            tmp.next = node
            tmp = tmp.next
    return list

'''
print given liked list
'''
def printLinkedList(list:LinkedList) :
    head = list.head
    if head :
        tmp = head
        while tmp :
            print(tmp.val, end =' ' )
            tmp = tmp.next

'''
insert element at beginning of given liked list
'''
def insertInBeginning(list:LinkedList, val:int) :
    node = Node(val)
    node.next = list.head
    list.head = node

'''
insert element at end of given linked list
'''
def insertInEnd(list:LinkedList, val:int) :
    node = Node(val)
    tmp = list.head
    while tmp.next :
        tmp = tmp.next
    tmp.next = node

'''
delete given key from linked list
'''
def deleteGivenKey(list, key) :
    tmp = list.head
    if not tmp :
        return
    if tmp.val == key :
        list.head = list.head.next
    prev = None
    while tmp and tmp.val != key :
        prev = tmp
        tmp = tmp.next
    if tmp :
        prev.next = tmp.next


'''
driver code
'''

__name__ = '__main__'
print('creating linked list')
arr = list(map(int, input().split()))
list = createLinkedList(arr)
printLinkedList(list)

print('adding in beginning')
insertInBeginning(list, int(input()))
printLinkedList(list)

print('inserting in end')
insertInEnd(list, int(input()))
printLinkedList(list)

print('deleitng a key')
deleteGivenKey(list, int(input()))
printLinkedList(list)



