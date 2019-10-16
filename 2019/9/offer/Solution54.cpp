/**
 * 数组中的逆序对
 * 在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
 * 输入一个数组，求出这个数组中的逆序对的总数。 
 */
#include<iostream>
#include<vector>
using namespace std;

/**
 * 1.每个数字之间都做比较的话，时间复杂度为 O(n!)
 * 2.将数组分成多个有序子序列，判断一个有序子序列的首位是否大于另一个的末尾，
 * 	大于则逆序对数量增加前者的序列长度，之后按照步骤1执行
 */
class Solution {
public:
    int inversePairs(vector<int>& nums) {
		// 放置子序列的前后位
		vector<int> list;
		int result = 0;
		int length = nums.size();
		// 放置首位位置
		list.push_back(0);
        for(int i = 1; i < length; ++ i){\
			// 当前数字是否大于之前数字，小于则为两个有序子序列中间位置
			if(nums[i] < nums[i - 1]){
				// 放置前子序列末位位置
				list.push_back(i - 1);
				// 放置后子序列前位位置
				list.push_back(i);
			}
		}
		// 放置最末子序列的末位
		list.push_back(length - 1);

		int size = list.size();
		// 开始比较
		for(int i = 0; i < size; ++(++i))
			for(int j = i + 3; j < size; ++(++j))
				// 首位大于另一个的末尾
				if(nums[list[i]] > nums[list[j]])
				    result += ((list[i + 1] - list[i] + 1) * (list[j] - list[j - 1] + 1));
				// 首位大于另一个的首位 或 末尾大于另一个的首位
				else
				    for(int a = list[i]; a <= list[i + 1]; ++a)
						for(int b = list[j - 1]; b <= list[j]; ++b)
							if(nums[a] > nums[b]) ++result;
							else break;
		return result;
	}
};