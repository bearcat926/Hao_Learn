/**
 * 树中两个结点的最低公共祖先
 * 给出一个二叉树，输入两个树节点，求它们的最低公共祖先。
 * 一个树节点的祖先节点包括它本身。
 * 
 * 注意：
 * 输入的二叉树不为空；
 * 输入的两个节点一定不为空，且是二叉树中的节点；
 */
#include<iostream>
#include<vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
		// 边界
		if(!root) return NULL;
		if(root == p || root == q) return root;
		// 左右子树遍历结果
		auto left = lowestCommonAncestor(root->left, p, q);
		auto right = lowestCommonAncestor(root->right, p, q);
		// 左右子树遍历的结果都不为空，则返回根节点
		if(left && right) return root;
		// 否则返回有值的一方
		if(left) return left;
		else return right;
    }
};