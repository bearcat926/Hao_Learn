/**
 * 二叉树的深度
 * 输入一棵二叉树的根结点，求该树的深度。
 * 从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
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
    int treeDepth(TreeNode* root) {
		int length = 0;
        dfs(root, length);
		return res;
    }
	void dfs(TreeNode* root, int &length){
		// root为空则判断当前长度是否超过最长深度
		if(!root) {
		    res = res > length ? res : length;
		    return;
		}
		++ length;
		dfs(root->left, length);
		dfs(root->right, length);
		-- length;
	}
};