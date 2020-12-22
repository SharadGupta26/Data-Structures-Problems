package Tree;
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
class Sorted_Array_To_BST {
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums.length == 0) {
            return null;
        }
        return toBST(nums, 0, nums.length - 1);
    }
    
    private TreeNode toBST(int[] num, int left, int right) {
        if(right < left) {
            return null;
        }
        int mid = (left + right) / 2;
        TreeNode n = new TreeNode(num[mid]);
        n.left = toBST(num, left, mid -1);
        n.right = toBST(num , mid + 1, right);
        return n;
    }
}