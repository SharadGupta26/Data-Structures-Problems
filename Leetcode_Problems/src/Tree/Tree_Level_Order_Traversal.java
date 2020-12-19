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
public class Tree_Level_Order_Traversal {
	 public List<List<Integer>> levelOrder(TreeNode root) {
	        
	        List<List<Integer>> levels = new ArrayList<>();
	        traverse(root, levels, 0);
	        return levels;
	    }
	    
	    public void traverse(TreeNode node, List<List<Integer>> levels, int level) {
	        if(node == null) {
	            return;
	        }
	        getLevel(levels, level).add(node.val);
	        traverse(node.left, levels, level+1);
	        traverse(node.right, levels, level+1);
	        
	    }
	    
	    private List<Integer> getLevel(List<List<Integer>> levels, int level) {
	        try {
	            return levels.get(level);
	        } catch(IndexOutOfBoundsException e) {
	            List<Integer> newLevel = new ArrayList<>();
	            levels.add(newLevel);
	            return newLevel;
	        }
	    }
}
