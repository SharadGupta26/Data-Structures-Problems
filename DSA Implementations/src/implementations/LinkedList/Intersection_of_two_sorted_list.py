from LinkedListUtil import *
def intersection(list1, list2) :
    head1 = list1.head
    head2 = list2.head
    res = []
    while head1 and head2 :
        if head1.val == head2.val :
            res.append(head1.val)
            head1 = head1.next
            head2 = head2.next
        elif head1.val < head2.val :
            head1 = head1.next
        else :
            head2 = head2.next
    print('intersection ', res)


__name__ = '__main__'
arr1 = createLinkedList(list(map(int, input().split())))
arr2 = createLinkedList(list(map(int, input().split())))
intersection(arr1, arr2)
