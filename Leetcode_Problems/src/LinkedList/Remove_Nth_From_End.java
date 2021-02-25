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
class Remove_Nth_From_End {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode node1 = head;
        ListNode node2 = head;
        while(n-- > 0) {
            node1 = node1.next;
        }
        
        if(node1  == null) {
            return node2.next;
        }
        while(node1.next != null) {
            node1 = node1.next;
            node2 = node2.next;
        }
        
        node2.next = node2.next.next;
        return head;
    }
}