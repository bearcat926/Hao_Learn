import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

// 之字形打印二叉树
// 请实现一个函数按照之字形顺序从上向下打印二叉树。
// 即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

class TreeNode34 {
    int val;
    TreeNode34 left;
    TreeNode34 right;
    TreeNode34(int x) { val = x; }
}

class Solution34 {
    public List<List<Integer>> printFromTopToBottom(TreeNode34 root) {
		List<List<Integer>> list = new ArrayList<>();
		if(root == null) return list;
		Queue<TreeNode34> queue = new LinkedList<>();
		List<Integer> tempList = new ArrayList<>();
		TreeNode34 temp;
		
		queue.add(root);
		queue.add(null);
		boolean flag = false;	//第一次遇到空时，是对根节点的处理不需要反转
		while(queue.size() != 0) {
			temp = queue.poll();
			if(temp != null){
				tempList.add(temp.val);
				if(temp.left != null) queue.add(temp.left);
				if(temp.right != null) queue.add(temp.right);
			}else{
				/**
				 * queue只负责分行打印，通过隔行使tempList反转实现之字形打印
				 */
			    if(flag){
    				int length = tempList.size();
					int t = 0;
    				for(int i = 0, j = length - 1; i < j; ++i, --j){
    					t = tempList.get(j);
    					tempList.set(j, tempList.get(i));
    					tempList.set(i, t);
    				}
    			}
    			if(queue.size() > 0) queue.add(null); 
    			list.add(tempList);
    			tempList = new ArrayList<>();
    			flag = !flag;
			}
		}

		return list;
	}

}