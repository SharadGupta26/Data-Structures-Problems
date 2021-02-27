package LinkedList;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

/*
 * Keeps unique elements. Removes duplicacy of elements
 *  1->2->3->3->4->4->5 ===> 1->2->3->4->5
 */
class Remove_Duplicates_From_Sorted_List {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode temp = head;
        while(temp!= null && temp.next != null) {
            while(temp.next != null && temp.val == temp.next.val) {
                temp.next = temp.next.next;
            }
            temp = temp.next;
        }
        return head;
    }
}