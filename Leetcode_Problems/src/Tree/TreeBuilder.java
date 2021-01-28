package Tree;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;
import java.util.Scanner;

public class TreeBuilder {

	public static TreeNode build(int... items) {
		TreeNode root = null;
		Queue<TreeNode> queue = new LinkedList<>();
		if(items.length > 0) {
			root = new TreeNode(items[0]);
			queue.add(root);
			for(int i=1 ; i<items.length ; i++) {
				TreeNode n = queue.peek();
				if(n.left == null) {
					n.left = new TreeNode(items[i]);
					queue.add(n.left);
				} else {
					n.right = new TreeNode(items[i]);
					queue.add(n.right);
					queue.remove();
				}
			}
		}
		return root;
	}
	
	public static TreeNode build(int size) {
		return build(new Random().ints(size,1, 1000).toArray());
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int[] arr = new int[t];
		int i=0;
		while(t-- > 0) {
			arr[i++] = sc.nextInt();
		}
		TreePrinter.print(TreeBuilder.build(arr));
		
		TreePrinter.print(TreeBuilder.build(10));
		sc.close();
	}
}

