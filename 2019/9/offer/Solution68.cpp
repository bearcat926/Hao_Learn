/**
 * 滑动窗口的最大值
 * 给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。
 * 例如，如果输入数组[2, 3, 4, 2, 6, 2, 5, 1]及滑动窗口的大小3,那么一共存在6个滑动窗口，它们的最大值分别为[4, 4, 6, 6, 6, 5]。
 * 注意：数据保证k大于0，且k小于等于数组长度。
 */
#include<iostream>
#include<vector>
#include<queue>
using namespace std;

class Solution {
public:
    vector<int> maxInWindows(vector<int>& nums, int k) {
		std::queue<int> queue;
		vector<int> res;
		int i = 0, size = nums.size();
		while(i <= size) 
		{
			if(queue.size() < k) {
				if(i == size) break;
				queue.push(nums[i++]);
			}else{
				int max = queue.front();
				queue.pop();
				int j = k - 1;
				while(j--){
					int t = queue.front();
					max = max > t ? max : t;
					queue.pop();
					queue.push(t);
				}
				res.push_back(max);
			}
		}
		return res;
    }

	// 优化
	vector<int> maxInWindows(vector<int>& nums, int k) {
		deque<int> q;
		vector<int> res;
		// 使用队列存放数组下标
		for(int i = 0; i < nums.size(); ++ i)
		{
			// 当前下标值 超过 对头的数组下标+窗口大小时 -> 移除对头
			while(q.size() && q.front() + k <= i) q.pop_front();
			// 当前下标的数组元素 大于 队尾元素时 -> 替换
			while(q.size() && nums[q.back()] <= nums[i]) q.pop_back();
			q.push_back(i);
			// 当前下标 等于 窗口大小 - 1 时，可以开始添加最大值
			if(i >= k - 1) res.push_back(nums[q.front()]);
		}
		return res;
    }
};