/**
 * 数字在排序数组中出现的次数 
 * 统计一个数字在排序数组中出现的次数。
 * 例如输入排序数组[1, 2, 3, 3, 3, 3, 4, 5]和数字3，由于3在这个数组中出现了4次，因此输出4。
 */
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
	// 遍历 -> O(n)
    int getNumberOfK(vector<int>& nums , int k) {
        int result = 0;
		for(int i = 0; i < nums.size(); ++ i)
			if(nums[i] == k) 
				++ result;
		
		return result;
    }

	// 二分思想 -> O(logn)
	int getNumberOfK1(vector<int>& nums , int k) {
        if(nums.empty()) return 0;
        int size = nums.size();
        int result = 0, l = 0, r = size - 1;
		int mid = 0;
		while(l < r){
			mid = (l + r) >> 1;
			if(nums[mid] < k) l = mid + 1;
			else if(nums[mid] > k) r = mid;
			else break;
		}

		if(nums[mid] == k){
			l = r = mid;
			while(nums[l] == k || nums[r] == k){
				if(l >= 0 && nums[l] == k) --l;
				if(r < size && nums[r] == k) ++r;
			}
			result = r - l - 1;
		}
		return result;
    }
};