package Tree;

public class Tree_Max_Depth {
	public int maxDepth(TreeNode root) {
	        return maxDepth(root, 1);
	    }
	    
	    private int maxDepth(TreeNode node, int depth) {
	        if(node == null) {
	            return depth - 1;
	        }
	        
	        int left = maxDepth(node.left, depth + 1);
	        int right = maxDepth(node.right, depth + 1);
	        return Integer.max(left, right);
	    }
}

