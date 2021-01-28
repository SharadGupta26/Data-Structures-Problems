package Tree;

import java.util.LinkedList;
import java.util.Queue;

public class TreePrinter {

	public static void print(TreeNode root) {
		if(root != null) {
			Queue<TreeNode> queue = new LinkedList<TreeNode>();
			queue.add(root);
			while(!queue.isEmpty()) {
				TreeNode n = queue.poll();
				System.out.print(n.val + " ");
				if(n.left != null) {
					queue.add(n.left);
				}
				
				if(n.right != null) {
					queue.add(n.right);
				}
			}
		}
	}
}
