package Tree;
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Detect_Cycle_In_Linked_List {
	public boolean hasCycle(ListNode head) {
		if (head == null) {
			return false;
		}
		ListNode temp1 = head;
		ListNode temp2 = head.next;
		while (temp2 != null && temp2.next != null) {
			if (temp1 == temp2) {
				return true;
			}
			temp1 = temp1.next;
			temp2 = temp2.next.next;
		}
		return false;
	}
}