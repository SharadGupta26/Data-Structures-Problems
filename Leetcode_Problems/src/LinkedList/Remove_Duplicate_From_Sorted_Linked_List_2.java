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
 * Does not store element that is duplicated.
 * 
 * 1->2->3->3->4->4->5 ===> 1->2->5
 * 
 * @author sharadgupta
 *
 */
class Remove_Duplicate_From_Sorted_Linked_List_2 {
	public ListNode deleteDuplicates(ListNode head) {
		ListNode dummy = new ListNode(0);
		dummy.next = head;
		ListNode temp = dummy;

		while (head != null) {
			if (head.next != null && head.next.val == head.val) {
				while (head.next != null && head.val == head.next.val) {
					head = head.next;
				}
				temp.next = head.next;
			} else {
				temp = temp.next;
			}
			head = head.next;
		}
		return dummy.next;
	}
}