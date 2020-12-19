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
class Check_Symmetric_Tree {
    public boolean isSymmetric(TreeNode root) {
        if(root == null) {
            return true;
        }
        TreeNode left = root.left;
        TreeNode right = root.right;
        return isSymmetric(left, right);
    }
    
    public boolean isSymmetric(TreeNode left, TreeNode right) {
        if(left == null && right == null) {
            return true;
        }
        
        if(left == null || right == null) {
//        if((left == null && right != null ) || (left != null && right == null)) {
            return false;
        }
        
        if(left.val != right.val) {
            return false;
        }
        boolean b1 = isSymmetric(left.left, right.right);
        boolean b2 = isSymmetric(left.right, right.left);
        
        return b1 && b2;
    }
}