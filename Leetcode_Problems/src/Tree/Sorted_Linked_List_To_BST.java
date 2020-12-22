package Tree;
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
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Sorted_Linked_List_To_BST {
    public TreeNode sortedListToBST(ListNode head) {
        if(head == null) {
            return null;
        }
        return toBst(head, head, null);
    }
    
    private TreeNode toBst(ListNode head, ListNode left, ListNode right) {
        if(left == right) {
            return null;
        }
        
        ListNode mid = findMid(left, right);
        TreeNode n = new TreeNode(mid.val);
        n.left = toBst(head, left, mid);
        n.right = toBst(head, mid.next, right);
        return n;
    }
    
    private ListNode findMid(ListNode left, ListNode right) {
        if(left == right) {
            return left;
        }
        ListNode n = left;
        ListNode p = left;
        while(n.next != null && n.next != right && n.next.next != right) {
            n = n.next.next;
            p = p.next;
        }
        return p;
    }
}