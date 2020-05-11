package solutions;

import java.util.concurrent.atomic.AtomicReference;

/**
 * Problem Statement :
 * https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/
 * 
 * @author sharadgupta
 *
 */
public class Cusions_In_Binary_Tree {
	public boolean isCousins(TreeNode root, int x, int y) {
		AtomicReference<TreeNode> p1 = new AtomicReference<>(null);
		AtomicReference<TreeNode> p2 = new AtomicReference<>(null);

		int d1 = findDepth(root, x, 0, p1);
		int d2 = findDepth(root, y, 0, p2);

		if (d1 == d2 && p1.get() != null && p2.get() != null && p1.get().val != p2.get().val) {
			return true;
		}

		return false;

	}

	public int findDepth(TreeNode root, int target, int depth, AtomicReference<TreeNode> parent) {
		if (root == null) {
			return 0;
		}
		if (root.val == target) {
			return depth;
		}

		int foundDepth = 0;
		if (root.left != null) {

			foundDepth = findDepth(root.left, target, depth + 1, parent);
		}

		if (foundDepth == 0 && root.right != null) {
			foundDepth = findDepth(root.right, target, depth + 1, parent);
		}
		if (foundDepth != 0 && parent.get() == null) {
			parent.set(root);
		}
		return foundDepth;
	}
}

// Definition for a binary tree node.
class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode() {
	}

	TreeNode(int val) {
		this.val = val;
	}

	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}
