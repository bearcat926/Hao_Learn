import java.util.Arrays;

/**
 * 二叉搜索树的后序遍历序列
 * 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
 * 如果是则返回true，否则返回false。
 * 假设输入的数组的任意两个数字都互不相同。
 */

class Solution35 {
	/** 
	 * 二叉搜索树中序遍历 = 数组排序
	 * 后序：左，右，中
	 * 利用中序和后序，当发现左子树有值比根节点大，或者右子树有值比根节点小，则证明不是二叉查找树
	 */

    public static boolean verifySequenceOfBST(int [] sequence) {
		// 后序遍历数组为空则返回true
		if(sequence == null || sequence.length == 0) return true;
		int length = sequence.length;
		// 获取中序遍历的结果
		int[] inorder = Arrays.copyOf(sequence, length);
		quickSort(inorder, 0, length - 1);
		// 验证是否为二叉搜索树
		return verifyCore(sequence, inorder, 0, length - 1, 0, length - 1);
	}
	
	public static boolean verifyCore(int[] postorder, int[] inorder, int startPostorder, int endPostorder,
	int startInorder, int endInorder){
		
		boolean flag = true;
		int root = postorder[endPostorder];
		// 在中序遍历中找到root位置，并得到左子树的长度
		int leftLength = 0;
		while(startInorder + leftLength <= endInorder && inorder[startInorder + leftLength] < root) ++leftLength;
		// 获取右子树长度
		int rightLength = endPostorder - leftLength - 1;
		// 获取右子树初始位置
		int rightstartPostorder = startPostorder + leftLength;

		// 结束条件是左子树有值比根节点大 或者 右子树有值比根节点小
		for(int i = startPostorder; i < leftLength; i++)
			if(postorder[i] > root) return false;
		for(int i = rightstartPostorder; i < rightLength; i++)
			if(postorder[i] > root) return false;	

		// 4, 6, 8, 10, 12, 14, 16 - 中序
	    // 4, 8, 6, 12, 16, 14, 10 - 后序
		if(leftLength > 0) flag &= verifyCore(postorder, inorder, startPostorder, rightstartPostorder - 1, startInorder, startInorder + leftLength - 1);
		if (rightLength > 0) flag &= verifyCore(postorder, inorder, rightstartPostorder, endPostorder - 1, startInorder + leftLength + 1, endInorder);
		
		return flag;
	}

	// 快排
	public static void quickSort(int[] sequence, int start, int end) {
		// 退出条件
		if(start >= end) return;
		int p = partition(sequence, start, end);
		// 递归处理子数组，因为是按中值p进行排序，所以范围中不需要有p
		quickSort(sequence, start, p - 1);
		quickSort(sequence, p + 1, end);
	}

	//找基准数，划分
	public static int partition(int[] sequence, int start, int end) {
		// 获取首位的值
		int p = sequence[start];
		while (start < end) {
			// 先从后找到一个小于p的值，将其换到start的位置
			while (start < end && sequence[end] > p) --end;
			sequence[start] = sequence[end];
			// 再从前找到一个大于p的值，将其换到end的位置
			while (start < end && sequence[start] < p) ++start;
			sequence[end] = sequence[start];
		}
		// 最后将p放置在start位置上
		sequence[start] = p;
		return start;
	}

	// public static void swap(int[] sequence, int start, int end) {
	// 	int temp = sequence[start];
	// 	sequence[start] = sequence[end];
	// 	sequence[end] = temp;
	// }

	/**
	 * 改进方法：只通过遍历后序进行判断，
	 * 通过找到第一个比root大的值将树分为左右子树，
	 * 当发现左子树有值比根节点大，或者右子树有值比根节点小，则证明不是二叉查找树
	 * 
	 */
	public static boolean verifySequenceOfBST2(int [] sequence) {
		// 后序遍历数组为空则返回true
		if(sequence == null || sequence.length == 0) return true;
		int length = sequence.length;
		// 验证是否为二叉搜索树
		return verifyCore2(sequence, 0, length - 1);
	}

	public static boolean verifyCore2(int[] postorder, int startPostorder, int endPostorder){
		
		boolean flag = true;
		int root = postorder[endPostorder];
		// 找到第一个比root大的值，其左为左子树，并得到左子树的长度
		int leftLength = 0;
		while(startPostorder + leftLength < endPostorder && postorder[startPostorder + leftLength] < root) leftLength++;
		// 获取右子树长度
		int rightLength = (endPostorder - startPostorder) - leftLength;
		// 获取右子树初始位置
		int rightstartPostorder = startPostorder + leftLength;

		// 结束条件是左子树有值比根节点大
		for(int i = startPostorder; i < leftLength; i++)
			if(postorder[i] > root) return false;
		// 或者 右子树有值比根节点小
		for(int j = rightstartPostorder; j < endPostorder; j++)
			if(postorder[j] < root) return false;	

		if(leftLength > 0) flag &= verifyCore2(postorder, startPostorder, rightstartPostorder - 1);
		if (rightLength > 0) flag &= verifyCore2(postorder, rightstartPostorder, endPostorder - 1);
		
		return flag;
	}
	
	public static void main(String[] args) {
		int[] sequence = {1, 2, 5, 4, 9, 10, 7, 3, 6, 8};
		System.out.println(verifySequenceOfBST2(sequence));
	}

}