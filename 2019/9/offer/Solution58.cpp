/**
 * 数组中数值和下标相等的元素
 * 假设一个单调递增的数组里的每个元素都是整数并且是唯一的。
 * 请编程实现一个函数找出数组中任意一个数值等于其下标的元素。
 * 例如，在数组[-3, -1, 1, 3, 5]中，数字3和它的下标相等。
 * 如果不存在，则返回-1。
 */
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int getNumberSameAsIndex(vector<int>& nums) {
		if(nums.empty()) return -1;
		int size = nums.size();
		int l = 0, r = size - 1;
		while(l < r){
			int mid = (l + r) >> 1;
			if(nums[mid] > mid) r = mid;
			else if(nums[mid] < mid) l = mid + 1;
			else return mid;
		}

		return nums[l] == l ? l : -1;
    }
};

int main(int argc, char const *argv[])
{
	int array[] = {-5, -4, -3, 3, 7, 8, 9};
	vector<int> list;
	for(int i = 0; i < sizeof(array)/sizeof(int); i++) list.push_back(array[i]);

	Solution *s = new Solution();
	cout << s->getNumberSameAsIndex(list);
	return 0;
}
