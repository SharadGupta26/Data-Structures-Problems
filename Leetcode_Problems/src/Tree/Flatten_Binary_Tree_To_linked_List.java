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
class Flatten_Binary_Tree_To_linked_List {
    public void flatten(TreeNode root) {
        if(root == null || (root.left == null && root.right == null)) {
            return;
        }
        flatten(root.left);
        flatten(root.right);
        if(root.left != null) {
            TreeNode extreme = findExtreme(root.left);
            extreme.right = root.right;
            root.right = root.left;
            root.left = null;
        }
    }
    
    private TreeNode findExtreme(TreeNode node) {
        while(node.right != null) {
            node = node.right;
        }
        return node;
    }
}