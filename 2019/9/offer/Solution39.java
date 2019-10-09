import java.util.LinkedList;
import java.util.Queue;

/**
 * 序列化二叉树
 * 请实现两个函数，分别用来序列化和反序列化二叉树。
 * 您需要确保二叉树可以序列化为字符串，并且可以将此字符串反序列化为原始树结构。
 */

class Solution39 {

    // Encodes a tree to a single string.
    String serialize(TreeNode root) {
		// 非空
		if(root == null) return null;
		// 构造字符串
		StringBuilder str = new StringBuilder("[");

		Queue<TreeNode> queue = new LinkedList<>();
		queue.add(root);
		// 处理头结点
		str.append(root.val +"");

		while(queue.size() > 0){
			TreeNode node = queue.poll();

			if(node == null)str.append(", null");
			// 头结点和空节点不做该操作
			else if(node != root) str.append(", " + node.val);

			// 空节点不添加左右节点
			if(node != null){
				// 孩子为空添加空
				if(node.left == null) queue.add(null);
				else queue.add(node.left);

				if(node.right == null) queue.add(null);
				else queue.add(node.right);
			}
		}
		// 末尾括号
		str.append("]");
		return str.toString();
	}
	
    // Decodes your encoded data to tree.
    TreeNode deserialize(String data) {
		// 非空
		if(data == null || "".equals(data)) return null; 
		char[] cA = data.toCharArray();
		// 新字符串去除前后括号
		String s = new String(cA, 1, cA.length - 2);
		// 根据 ", " 分割为字符串数组
		String[] sA = s.split(", ");

		int i = 0;
		TreeNode root = StringConvertTreeNode(sA[i++]);

		Queue<TreeNode> queue = new LinkedList<>();
		queue.add(root);

		while(queue.size() > 0){
			TreeNode node = queue.poll();
			if(node != null){
				// 左孩子
				TreeNode left = StringConvertTreeNode(sA[i++]);
				node.left = left;
				queue.add(left);
				// 右孩子
				TreeNode right = StringConvertTreeNode(sA[i++]);
				node.right = right;
				queue.add(right);
			}
		}

		return root;
	}

	// 字符串转换为TreeNode
	public TreeNode StringConvertTreeNode(String s){
		Integer val = "null".equals(s) ? null : new Integer(s);
		return val == null ? null : new TreeNode(val); 
	}
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}