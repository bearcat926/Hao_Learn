import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

// 不分行从上往下打印二叉树
// 从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。

class TreeNode32 {
    int val;
    TreeNode32 left;
    TreeNode32 right;
    TreeNode32(int x) { val = x; }
}

class Solution32 {
	// 广度优先遍历
    public List<Integer> printFromTopToBottom(TreeNode32 root) {
		List<Integer> list = new ArrayList<>();
		if(root == null) return list;
		Queue<TreeNode32> queue = new LinkedList<>();
		queue.add(root);
		TreeNode32 temp;

		while(queue.size() != 0) {
			temp = queue.poll();
			list.add(temp.val);
			if(temp.left != null) queue.add(temp.left);
			if(temp.right != null) queue.add(temp.right);
		}

		return list;
	}

}