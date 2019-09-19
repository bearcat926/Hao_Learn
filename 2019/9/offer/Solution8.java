/**
 * 二叉树的下一个节点 
 * 给定一棵二叉树的其中一个节点，请找出中序遍历序列的下一个节点。
 */
class TreeNode8 {
	int val;
	TreeNode8 left;
	TreeNode8 right;
	TreeNode8 father;

	TreeNode8(int x) {
		val = x;
	}
}

class Solution8 {

	public static TreeNode8 inorderSuccessor(TreeNode8 p) {
		TreeNode8 nextNode = null, curNode = null;
		// 1.有右子树，则返回右子树的最左节点
		if (p.right != null) {
			curNode = p.right;
			while (curNode.left != null)
				curNode = curNode.left;
			nextNode = curNode;
		} else if (p.father != null) { // 2.无右节点，则要找父节点
			TreeNode8 fatherNode = p.father;
			curNode = p;
			// 2.1 p是父节点的左子节点则返回父节点
			if (p == fatherNode.left) {
				nextNode = fatherNode;
			} else {
				do {
					// 向上移动后判断
					curNode = fatherNode;
					fatherNode = fatherNode.father;
					// 2.2 当前节点是根节点但仍然没找到时返回null
					// 2.3 当前节点是父节点的左子节点时返回父节点
				} while (fatherNode != null && curNode == fatherNode.right);
				nextNode = fatherNode;
			}
		}
		return nextNode;
	}

	public static void main(String[] args) {

		TreeNode8 node1 = new TreeNode8(1);
		TreeNode8 node2 = new TreeNode8(2);
		TreeNode8 node3 = new TreeNode8(3);
		node1.left = node1.right = node2.father = node3.left = node3.right = null;
		node1.father = node3.father = node2;
		node2.left = node1;
		node2.right = node3;

		long startTime = System.nanoTime();
		TreeNode8 node = inorderSuccessor(node2);
		long endTime = System.nanoTime();
		System.out.println("time：" + (endTime - startTime));
		inOrderPrint(node);
	}

	public static void inOrderPrint(TreeNode8 node) {
		// 中序遍历
		if (node.left != null) {
			inOrderPrint(node.left);
		}
		if (node != null) {
			System.out.println(node.val);
		}
		if (node.right != null) {
			inOrderPrint(node.right);
		}
	}

	public static void preOrderPrint(TreeNode8 node) {
		// 前序遍历
		if (node != null) {
			System.out.println(node.val);
		}
		if (node.left != null) {
			preOrderPrint(node.left);
		}
		if (node.right != null) {
			preOrderPrint(node.right);
		}
	}

}