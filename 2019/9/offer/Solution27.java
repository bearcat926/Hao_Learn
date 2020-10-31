/**
 * 二叉树的镜像
 * 输入一个二叉树，将它变换为它的镜像。
 */

 /**
  * 左右子树交换
  */

class TreeNode27 {
    int val;
    TreeNode27 left;
    TreeNode27 right;
    TreeNode27(int x) { val = x; }
}

class Solution27 {
    public void mirror(TreeNode27 root) {
		if(root != null) {
		    exchange(root);
    		mirror(root.left);
    		mirror(root.right);
		}
	}
	
	public void exchange(TreeNode27 root){
		TreeNode27 temp = root.left;
		root.left = root.right;
		root.right = temp;
	}
}