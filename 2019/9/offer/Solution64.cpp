/**
 * 和为S的两个数字
 * 输入一个数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
 * 如果有多对数字的和等于s，输出任意一对即可。
 * 你可以认为每组输入中都至少含有一组满足条件的输出。
 */
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	// 哈希表
    vector<int> findNumbersWithSum(vector<int>& nums, int target) {
        unordered_set<int> set;
        for(int i = 0; i < nums.size(); ++ i){
            if(set.count(target - nums[i])) return vector<int>{nums[i],target - nums[i]};
            set.insert(nums[i]);
        }
        return vector<int>();
    }

	// 暴力
	vector<int> findNumbersWithSum1(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size(); ++ i)
            for(int j = i; j < nums.size(); ++j)
				if(nums[i] + nums[j] == target) return vector<int>{nums[i], nums[j]};
        return vector<int>();
    }
};