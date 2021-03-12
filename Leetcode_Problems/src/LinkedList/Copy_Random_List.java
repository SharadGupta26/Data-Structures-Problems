package LinkedList;

import java.util.HashMap;
import java.util.Map;

// Definition for a Node.
class Node {
	int val;
	Node next;
	Node random;

	public Node(int val) {
		this.val = val;
		this.next = null;
		this.random = null;
	}
}

/**
 * A linked list of length n is given such that each node contains an additional
 * random pointer, which could point to any node in the list, or null.
 * 
 * Construct a deep copy with new nodes such that copied list represent the same
 * list state.
 * 
 * @author sharadgupta
 *
 */
class Copy_Random_List {
	public Node copyRandomList(Node head) {
		Map<Node, Node> map = new HashMap<>();
		Node dummy = new Node(0);
		Node ptr = dummy;
		Node temp = head;
		while (head != null) {
			Node newNode = new Node(head.val);
			map.put(head, newNode);
			ptr.next = newNode;
			head = head.next;
			ptr = ptr.next;
		}

		head = temp;
		ptr = dummy.next;
		while (head != null) {
			if (head.random != null) {
				ptr.random = map.get(head.random);
			}
			head = head.next;
			ptr = ptr.next;
		}
		return dummy.next;
	}
}