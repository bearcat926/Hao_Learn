import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

// 分行从上往下打印二叉树
// 从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印，每一层打印到一行。

class TreeNode33 {
    int val;
    TreeNode33 left;
    TreeNode33 right;
    TreeNode33(int x) { val = x; }
}

class Solution33 {
    public List<List<Integer>> printFromTopToBottom(TreeNode33 root) {
		List<List<Integer>> list = new ArrayList<>();
		if(root == null) return list;
		Queue<TreeNode33> queue = new LinkedList<>();
		List<Integer> tempList = new ArrayList<>();
		TreeNode33 temp;
		
		queue.add(root);
		queue.add(null);
		while(queue.size() != 0) {
			temp = queue.poll();
			if(temp != null){
				tempList.add(temp.val);
				if(temp.left != null) queue.add(temp.left);
				if(temp.right != null) queue.add(temp.right);
			}else{
				if(queue.size() > 0) queue.add(null); 
				list.add(tempList);
				tempList = new ArrayList<>();
			}
		}

		return list;
	}

}