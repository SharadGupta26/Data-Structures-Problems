package Tree;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

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
class Tree_Level_Order_Bottom {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        traverse(root, result, 0);
        Collections.reverse(result);
        return result;
    }
    
    private void traverse(TreeNode node, List<List<Integer>> levels, int level) {
        if(node == null) {
            return;
        }
        getLevel(levels, level).add(node.val);
        traverse(node.left, levels, level + 1);
        traverse(node.right, levels, level + 1);
    }
    
    private List<Integer> getLevel(List<List<Integer>> levels, int level) {
        try {
            return levels.get(level);
        } catch(Exception e) {
            List<Integer> n = new ArrayList<>();
            levels.add(n);
            return n;
        }
    }
}