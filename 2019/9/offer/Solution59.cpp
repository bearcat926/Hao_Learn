/**
 * 二叉搜索树的第k个结点
 * 给定一棵二叉搜索树，请找出其中的第k小的结点。
 * 你可以假设树和k都存在，并且1≤k≤树的总结点数。
 */

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    // int res;
    // TreeNode* kthNode(TreeNode* root, int k) {
	// 	// 要第k小的数，不是第几个数
	// 	// 深度 + 计数
	// 	// 计算长度左子树长度
	// 	int leftLength = calcNum(root->left);
	// 	dfs(root, leftLength + 1, k);
	// 	return new TreeNode(res  );
    // }
	// int calcNum(TreeNode* root){
	//     if(root == NULL) return 0;
	// 	// 广度 + 计数
	// 	int n = 0;
	// 	std::queue<TreeNode*> queue;
	// 	queue.push(root);
	// 	while(queue.size()){
	// 		TreeNode* node = queue.front();
	// 	    queue.pop();
	// 	    if(node != NULL){
	// 	        ++n;
    // 			if(node->right == NULL) queue.push(NULL);
    // 			else queue.push(node->right);
    
    // 			if(node->left == NULL) queue.push(NULL);
    // 			else queue.push(node->left);
	// 	    }
	// 	}
	// 	return n;
	// }
	// void dfs(TreeNode* node, int n, int k){
	// 	if(node != NULL) {
	// 		if(n == k) res = node->val;
	// 		if(node->left != NULL) dfs(node->left, n - 1, k);
	// 		if(node->right != NULL) {
	// 			int rightOfLeftLength = calcNum(node->right->left);
	// 			dfs(node->right, n + rightOfLeftLength + 1, k);
	// 		}
	// 	}
	// }

	TreeNode *ans;
    void dfs(TreeNode* root, int &k){
		// 为空返回
        if(!root) return;
		// 深度搜索左子树
        dfs(root->left, k);
		// 减去当前节点
        -- k;
		// 当前节点匹配
        if(!k) ans = root;
		// k > 0，则深度搜索右子树
        if(k > 0) dfs(root->right, k);
    }
	
    TreeNode* kthNode(TreeNode* root, int k) {
        dfs(root, k);
        return ans;
    }
};

int main(int argc, char const *argv[])
{
	int array[] = {6, 5, 8, 4, 0, 7, 9, 0, 5, 0, 0, 0, 0, 0, 0};
	int length = sizeof(array)/sizeof(int);
	TreeNode* root = new TreeNode(array[0]);
	queue<TreeNode*> queue;
	queue.push(root);
	int i = 1;

	while(queue.size()){
		TreeNode* node = queue.front();
		queue.pop();
		// left
		if(node != NULL){
			if(i < length && array[i]){
				TreeNode* left = new TreeNode(array[i++]);
				node->left = left;
				queue.push(left);
			}else queue.push(NULL);

			// right
			if(i < length && array[i]){
				TreeNode* right = new TreeNode(array[i++]);
				node->right = right;
				queue.push(right);
			}else queue.push(NULL);
		}
	}
	Solution *s = new Solution();
	int k = 3;
	TreeNode *n = s->kthNode(root,1);
	cout << n->val;
	return 0;
}
