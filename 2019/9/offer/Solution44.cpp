/**
 * 连续子数组的最大和
 * 输入一个 非空 整型数组，数组里的数可能为正，也可能为负。
 * 数组中一个或连续的多个整数组成一个子数组。
 * 求所有子数组的和的最大值。
 * 要求时间复杂度为O(n)。
 */
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
	int maxSubArray(vector<int> &nums)
	{
		// 获取数组最大数
		int max = nums[0];
		for (int i = 1; i < nums.size(); ++i) 
			if (nums[i] > max) max = nums[i];
		
		// 应对数组无正整数的情况
		if (max <= 0) return max;

		// 累加获取子数组的和
		int sum = 0;
		for (int i = 0; i < nums.size(); ++i)
		{
			sum += nums[i];
			// sum大于max，则重新赋值max
			if (sum > max) max = sum;
			// sum小于0，则舍弃前面的子数组，重新计数
			if (sum < 0) sum = 0;
		}

		return max;
	}
};

int main(int argc, char const *argv[])
{
	Solution *s = new Solution();
	vector<int> list(8);
	int array[] = {1, -2, 3, 10, -4, 7, 2, -5};

	for(int i = 0; i < 8; ++i){
		list[i] = array[i];
	}

	cout << s->maxSubArray(list);
	return 0;
}
