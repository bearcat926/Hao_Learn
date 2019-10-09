import java.util.*;

/**
 * 二叉树中和为某一值的路径
 * 输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
 * 从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
 */

class TreeNode36 {
    int val;
    TreeNode36 left;
    TreeNode36 right;
    TreeNode36(int x) { val = x; }
}

class Solution36 {
	static List<List<Integer>> list = new ArrayList<>();
	static 

	public List<List<Integer>> findPath(TreeNode36 root, int sum) {
		List<Integer> path = new ArrayList<>();
		TreeNode36 p = root;
		int i = 0;
		Core(p, path, i, sum);
		return list;
	}

	// 回溯方法是先加上该值，在该节点及其以下节点完成操作后，在数组中减去该位置的值
	public static void Core(TreeNode36 p, List<Integer> path, int i, int sum){
		if(p == null) return;
		path.add(p.val);
		sum -= p.val;
		if(sum == 0 && p.left == null && p.right == null ) list.add(new ArrayList<>(path));
		Core(p.left, path, i+1, sum);
		Core(p.right, path, i+1, sum);
		path.remove(i);
	}
}