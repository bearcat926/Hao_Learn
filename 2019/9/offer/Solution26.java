/**
 * 树的子结构
 * 输入两棵二叉树A，B，判断B是不是A的子结构。
 * 我们规定空树不是任何树的子结构。
 */

 /**
  * 对于第一部分，我们直接递归遍历树A即可，遇到非空节点后，就进行第二部分的判断。
  * 对于第二部分，我们同时从根节点开始遍历两棵子树：
  *     
  * 	
  * 	
  */
class TreeNode26 {
    int val;
    TreeNode26 left;
    TreeNode26 right;
    TreeNode26(int x) { val = x; }
}
class Solution26 {
    public static boolean hasSubtree(TreeNode26 pRoot1, TreeNode26 pRoot2) {
		// 递归遍历树A即可，遇到非空节点后，就进行isEqual的判断。
		if (pRoot1 == null || pRoot2 == null) return false;
		if (isEqual(pRoot1, pRoot2)) return true;
		// 否则说明当前这个点是不匹配的，然后递归判断其左子树和右子树是否分别匹配即可
        return hasSubtree(pRoot1.left, pRoot2) || hasSubtree(pRoot1.right, pRoot2);
	}
	
	// 比较当前节点的结构与pRoot2是否相等
	public static boolean isEqual(TreeNode26 node, TreeNode26 pRoot2) {
		// 如果树B中的节点为空，则表示当前分支是匹配的，返回true
		if (pRoot2 == null) return true;
		// 如果树A中的节点为空，但树B中的节点不为空，则说明不匹配，返回false；或者两个节点都不为空，但数值不同，也返回false
		if (node == null || node.val != pRoot2.val) return false;
		// 否则说明当前这个点是匹配的，然后递归判断左子树和右子树是否分别匹配即可
        return isEqual(node.left, pRoot2.left) && isEqual(node.right, pRoot2.right);
	}	

	// 在c++中所有的非0值都认为是true, 0被认为是false
}