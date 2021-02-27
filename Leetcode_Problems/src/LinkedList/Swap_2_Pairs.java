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
class Swap_2_Pairs {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode n = dummy;
        while(n.next != null && n.next.next != null) {
            ListNode temp = n.next.next; 
            n.next.next = temp.next;
             temp.next = n.next;
            n.next = temp;
            n =temp.next;
        }
        return dummy.next;
    }
}