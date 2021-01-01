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

/**
 * Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
 * @author sharadgupta
 *
 */
class Add_Two_Numbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int cf = 0;
        int sum = l1.val + l2.val + cf;
        ListNode head = new ListNode(sum % 10);
        cf = sum / 10;
        ListNode n = head;
        while(l1.next != null && l2.next != null) {
            sum = l1.next.val + l2.next.val + cf;
            n.next = new ListNode(sum % 10);
            cf = sum / 10;
            n = n.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        
        while (l1.next != null) {
            sum = l1.next.val  + cf;
            n.next = new ListNode(sum % 10);
            cf = sum / 10;
            n = n.next;
            l1 = l1.next;
        }
        
        while (l2.next != null) {
            sum = l2.next.val + cf;
            n.next = new ListNode(sum % 10);
            cf = sum / 10;
            n = n.next;
            l2 = l2.next;
        }
        
        if(cf > 0) {
            n.next = new ListNode(cf);
        }
        
        return head;
    }
    
}