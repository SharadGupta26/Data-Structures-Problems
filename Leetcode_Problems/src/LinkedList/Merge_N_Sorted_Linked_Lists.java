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
class Merge_N_Sorted_Linked_Lists {
    public ListNode mergeKLists(ListNode[] lists) {
        int n = lists.length;
        if(n==0) return null;
        int i = (n/2);
        int low = 0;
        int high = n-1;
        while (i-- >=0) {
            while(high > low) {
                lists[low] = merge(lists[low], lists[high]);
                low++;
                high--;
            }
            low=0;
        }
        return lists[0]; 
    }
    
   private ListNode merge(ListNode l1, ListNode l2) {
        
		ListNode dummy = new ListNode(0);
		ListNode temp = dummy;

		while (l1 != null && l2 != null) {
			if (l1.val < l2.val) {
				temp.next = l1;
				l1 = l1.next;
			} else {
				temp.next = l2;
				l2 = l2.next;
			}
			temp = temp.next;
		}

		while (l1 != null) {
			temp.next = l1;
			l1 = l1.next;
			temp = temp.next;
		}
		
		while (l2 != null) {
			temp.next = l2;
			l2 = l2.next;
			temp = temp.next;
		}
		return dummy.next;
	
    }
}