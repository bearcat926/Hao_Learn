/**
 * 输入一棵二叉树的根结点，判断该树是不是平衡二叉树。
 * 如果某二叉树中任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
 * 规定空树也是一棵平衡二叉树。
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
	int res;
    int isBalanced(TreeNode* root) {
		int length = 0;
		return dfs(root, length);
    }
	bool dfs(TreeNode* root, int &length){
		// root为空则判断当前长度是否超过最长深度
		if(!root) {
		    if(!res) {
				res = length;
				return true;
			}
			else return(res - length > 1 || res - length < -1) ? false : true;
		}
		++ length;
		bool flag = dfs(root->left, length) && dfs(root->right, length);
		-- length;
		return flag;
	}
};

