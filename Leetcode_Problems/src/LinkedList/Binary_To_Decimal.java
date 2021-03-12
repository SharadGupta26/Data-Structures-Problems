package LinkedList;

/**
 * Definition for singly-linked list. public class ListNode { int val; ListNode
 * next; ListNode() {} ListNode(int val) { this.val = val; } ListNode(int val,
 * ListNode next) { this.val = val; this.next = next; } }
 */
class Binary_To_Decimal {
	public int getDecimalValue(ListNode head) {
		int count = 0;
		ListNode n = head;
		while (n.next != null) {
			count++;
			n = n.next;
		}
		n = head;
		int sum = 0;
		while (n != null) {
			sum = sum + (int) Math.pow(2, count) * n.val;
			n = n.next;
			count--;
		}
		return sum;
	}

	
	/**
	 * Using binary left shift operator
	 * @param head
	 * @return
	 */
	public int getDecimalValue_Approach_2(ListNode head) {
		int sum = 0;

		while (head != null) {
			sum = (sum << 1) | head.val;
			head = head.next;
		}
		return sum;
	}
}