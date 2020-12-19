package Tree;

import java.util.ArrayList;
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

public class Tree_Zig_Zag_Level_Order_Traversal {

	 public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
	        List<List<Integer>> result = new ArrayList<>();
	        traverseZigZag(root, result, 0);
	        return result;
	    }
	    
	    private void traverseZigZag(TreeNode node, List<List<Integer>> result, int level) {
	        if(node == null) {
	            return ;
	        }
	            if(level % 2 == 0) {
	                getLevel(result, level).add(node.val);
	            } else {
	                getLevel(result, level).add(0, node.val);
	            }
	        traverseZigZag(node.left, result, level + 1);
	        traverseZigZag(node.right, result, level + 1);
	    }
	    
	    private List<Integer> getLevel(List<List<Integer>> levels, int level) {
	        try {
	            return levels.get(level);            
	        } catch(Exception e) {
	            List<Integer> newLevel = new ArrayList<>();
	            levels.add(newLevel);
	            return newLevel;
	        }
	    }
}
