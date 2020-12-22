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

/**
 * Reference : https://www.programiz.com/dsa/balanced-binary-tree
 */

class Check_Balanced_Binary_Tree {
    public boolean isBalanced(TreeNode root) {
        if(root == null) {
            return true;
        }
        
        int df = Math.abs(height(root.left) - height(root.right));
        if(df > 1) {
            return false;
        }
        return isBalanced(root.left) && isBalanced(root.right);
    }
    
    private int height(TreeNode n) {
        if(n == null) {
            return 0;
        }
        return Integer.max(height(n.left), height(n.right)) + 1;
    }
}