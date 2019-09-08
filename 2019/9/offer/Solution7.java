/**
 * 重建二叉树 
 * 输入一棵二叉树前序遍历和中序遍历的结果，请重建该二叉树。
 */
class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode(int x) {
		val = x;
	}
}

class Solution7 {

	public static TreeNode buildTree(int[] preorder, int[] inorder) {
		// 非空监测
		if (preorder == null || preorder.length == 0 || inorder == null || inorder.length == 0)
			return null;
		return buildTree(preorder, inorder, 0, preorder.length - 1, 0, inorder.length - 1);
	}

	public static TreeNode buildTree(int[] preorder, int[] inorder, int startPreorder, int endPreorder,
			int startInorder, int endInorder) {
		// 创建子树的根节点
		int rootVal = preorder[startPreorder];
		TreeNode root = new TreeNode(rootVal);
		root.left = root.right = null;

		// 返回末尾节点
		if (startPreorder == endPreorder && startInorder == endInorder
				&& preorder[startPreorder] == inorder[startInorder])
			return root;

		// 进行根节点位置判断和左右子树分隔
		// Tip：注意对左子树长度的计算是从中序首位置开始
		int rootInorder = startInorder;
		while (rootVal != inorder[rootInorder])
			rootInorder++;

		// startInorder + leftLength = rootInorder
		// 左子树长
		int leftLength = rootInorder - startInorder;
		// 前序末位
		int leftEndPreorder = startPreorder + leftLength;

		// left
		// 根节点位置加1，即为前序左子树开始位置
		// int leftStartPreorder = startPreorder + 1;
		// 根节点位置加leftLength，即为前序左子树结束位置
		// int leftEndPreorder = startPreorder + leftLength;
		// 中序第一个节点位置为左子树开始位置
		// int leftStratInorder = startInorder;
		// 中序第一个节点位置加（leftLength - 1），即为左子树结束位置
		// int leftEndInorder = startInorder + leftLength - 1;

		// right
		// 前序左子树结束位置加1，即为前序右子树开始位置
		// int rightStartPreorder = startPreorder + leftLength + 1;
		// 前序结束位置为末尾
		// int rightEndPreorder = endPreorder;
		// 中序左子树结束位置加2（根节点和），即为中序右子树开始位置
		// int rightStratInorder = startInorder + leftLength + 1;
		// 中序结束位置为末尾
		// int rightEndInorder = endInorder;

		// 处理左子树
		if (leftLength > 0) {
			root.left = buildTree(preorder, inorder, startPreorder + 1, leftEndPreorder, startInorder, rootInorder - 1);
		}

		// 因为前序为末尾减首位等于左右子树长度和，大于零则存在右子树
		if (endPreorder - startPreorder > leftLength) {
			root.right = buildTree(preorder, inorder, leftEndPreorder + 1, endPreorder, rootInorder + 1, endInorder);
		}

		// 迭代处理完成，返回节点
		return root;
	}

	public static void main(String[] args) {

		int[] preorder = { 3, 9, 20, 15, 7 };
		int[] inorder = { 9, 3, 15, 20, 7 };
		long startTime = System.nanoTime();
		TreeNode node = buildTree(preorder, inorder);
		long endTime = System.nanoTime();
		System.out.println("time：" + (endTime - startTime));
		preOrderPrint(node);
	}

	public static void inOrderPrint(TreeNode node) {
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

	public static void preOrderPrint(TreeNode node) {
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