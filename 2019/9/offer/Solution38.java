/**
 * 二叉搜索树与双向链表
 * 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
 * 要求不能创建任何新的结点，只能调整树中结点指针的指向。
 * 注意：需要返回双向链表最左侧的节点。
 * 
 */

class Solution38 {
    public TreeNode convert(TreeNode root) {
		if (root == null) return null;
		TreeNodePair result = Core(root);
		return result.start;
	}
	
	public TreeNodePair Core(TreeNode node) {
		TreeNodePair pair = new TreeNodePair();

		// 左子树为空则返回将start置为自身
		if(node.left == null) pair.start = node;
		else{
			TreeNodePair lPair = Core(node.left);
			node.left = lPair.end;
			lPair.end.right = node;
			pair.start = lPair.start;
		}

		// 左子树为空则返回将end置为自身
		if(node.right == null) pair.end = node;
		else{
			TreeNodePair rPair = Core(node.right);
			node.right = rPair.start;
			rPair.start.left = node;
			pair.end = rPair.end;
		}
		
		return pair;
	} 
}

class TreeNodePair{
	TreeNode start;
    TreeNode end;
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}