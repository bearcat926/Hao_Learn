/**
 * 把数组排成最小的数
 * 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
 * 例如输入数组[3, 32, 321]，则打印出这3个数字能排成的最小数字321323。 
 */

#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
using namespace std;

class Solution {
public:
    static bool cmp(int &a, int &b) {
        auto as = to_string(a), bs = to_string(b);
		// true,则a < b，a排序在前
        return as + bs < bs + as;
    }
    string printMinNumber(vector<int>& nums) {
        string str;
        if(!nums.size()) return str;
		// 利用c++ 中的sort函数为数组进行排序，排序方式是自定义的cmp函数
        sort(nums.begin(), nums.end(), cmp);
        for(int i = 0 ; i < nums.size(); ++i) 
            str += to_string(nums[i]);

    	return str;    
    }
};

int main(int argc, char const *argv[])
{
	Solution *s = new Solution();
	vector<int> list;
	int array[] = {3, 32, 321};
	for(int i = 0; i < sizeof(array) / sizeof(int); ++i) list.push_back(array[i]);
	cout << s -> printMinNumber(list);
	return 0;
}
