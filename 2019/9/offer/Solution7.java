/**
 * 重建二叉树
 * 输入一棵二叉树前序遍历和中序遍历的结果，请重建该二叉树。
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}
class Solution7 {
    

    public static TreeNode buildTree(int[] preorder, int[] inorder) {
        

        TreeNode root = new TreeNode(preorder[0]);


        return root;
    }

    public static void main(String[] args) {
        
        int[] preorder = {3, 9, 20, 15, 7}; 
        int[] inorder = {9, 3, 15, 20, 7};
        long startTime = System.nanoTime();
        TreeNode node = buildTree(preorder, inorder);
        long endTime = System.nanoTime();
        System.out.println("time：" + (endTime - startTime));
        
    }
}