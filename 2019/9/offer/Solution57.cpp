/**
 * 0到n-1中缺失的数字
 * 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0到n-1之内。
 * 在范围0到n-1的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
 */
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int getMissingNumber(vector<int>& nums) {
        if (nums.empty()) return 0;
        int l = 0, r = nums.size() - 1;
		
		// 当数组下标与数组值相等，则缺失的是n
        if (nums[r] == r) return (++r);

		// 当数组下标与数组值不相等，则缺失的数在mid右边
		// 相等，则缺失的数在mid左边
        while (l < r)
        {
            int mid = l + r >> 1;
            if (nums[mid] != mid) r = mid;
            else l = mid + 1;
        }
        return r;
    }
};
// 0124
// 0234

int main(int argc, char const *argv[])
{
	int array[] = {0, 1, 2, 4, 5, 6, 7, 8, 9};
	vector<int> list;
	for(int i = 0; i < sizeof(array)/sizeof(int); i++) list.push_back(array[i]);

	Solution *s = new Solution();
	cout << s->getMissingNumber(list);
	return 0;
}