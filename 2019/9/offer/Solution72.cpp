/**
 * 股票的最大利润
 * 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖 一次 该股票可能获得的利润是多少？
 * 例如一只股票在某些时间节点的价格为[9, 11, 8, 5, 7, 12, 16, 14]。
 * 如果我们能在价格为5的时候买入并在价格为16时卖出，则能收获最大的利润11。
 */
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxDiff(vector<int>& nums) {
        if(!nums.size()) return 0;
        int min = nums[0], profit = 0;
		for(int i = 1; i < nums.size(); ++ i){
			// 当前值大于之前的最小值，才有利润
		    int t = nums[i] - min;
			if(t > 0) profit = profit > t ? profit : t;
			// 否则利润为0
			else min = nums[i];
		}
		return profit;
    }
};