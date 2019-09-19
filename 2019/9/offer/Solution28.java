/**
 * 对称的二叉树
 * 请实现一个函数，用来判断一棵二叉树是不是对称的。
 * 如果一棵二叉树和它的镜像一样，那么它是对称的。
 */

 /**
  * 1. 从跟根节点开始，如果不为空，则比较值是否相同
  * 之后对左右子树进行比较:
  *     1. 对左子树进行翻转
  *     2. 递归比较结果，结果相同则对称
  */

class TreeNode28 {
    int val;
    TreeNode28 left;
    TreeNode28 right;
    TreeNode28(int x) { val = x; }
}

class Solution28 {
	public boolean isSymmetric(TreeNode28 root) {
		// 无节点也返回true
		if(root == null) return true;
		mirror(root.left); //n/2
		return isEqual(root.left, root.right); //n
	}

	public void mirror(TreeNode28 root) {
		if(root != null) {
		    exchange(root);
    		mirror(root.left);
    		mirror(root.right);
		}
	}
	
	public void exchange(TreeNode28 root){
		TreeNode28 temp = root.left;
		root.left = root.right;
		root.right = temp;
	}

	public boolean isEqual(TreeNode28 node1, TreeNode28 node2){
		// 共同到达末尾节点，则返回true
		if(node1 == null && node2 == null) return true;
		// 若其中一方为空或值不相同，则返回false
		if(node1 == null || node2 == null || node1.val != node2.val) return false;
		// 递归判断左右子树
		return isEqual(node1.left, node2.left) && isEqual(node1.right, node2.right);
	}

	/**
	 * 2. 递归判断两个子树是否互为镜像。
	 * 两个子树互为镜像当且仅当：
	 * 	   两个子树的根节点值相等；
	 * 	   第一棵子树的左子树和第二棵子树的右子树互为镜像，且第一棵子树的右子树和第二棵子树的左子树互为镜像；
	 */

	public boolean isSymmetric2(TreeNode28 root) {
		if(root == null) return true;
		return isEqual2(root.left, root.right); //n
	}

	public boolean isEqual2(TreeNode28 node1, TreeNode28 node2){
		// 共同到达末尾节点，则返回true
		if(node1 == null && node2 == null) return true;
		// 若其中一方为空或值不相同，则返回false
		if(node1 == null || node2 == null || node1.val != node2.val) return false;
		// 递归判断 前者的左子树和后者的右子树是否相同，前者的右子树和后者的左子树是否相同
		return isEqual2(node1.left, node2.right) && isEqual2(node1.right, node2.left);
	}
}