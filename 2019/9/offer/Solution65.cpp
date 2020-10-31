/**
 * 和为S的连续正数序列
 * 输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
 * 例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、4～6和7～8。
 */

#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > findContinuousSequence(int sum) {
        vector<vector<int>> res;
		for(int i = 1, j = 1, s = 1; i < sum; ++ i){
		    // cout << i << " " << j << " " << s << endl;
			while(s < sum) s += (++j);
			// cout << i << " " << j << " " << s << endl << endl;
			if(s == sum && j > i){
				vector<int> temp;
				for(int k = i; k <= j; ++ k) temp.push_back(k);
				res.push_back(temp);
			}
			s -= i;
		}
		return res;
    }
};

/**
 * 解法：
 * 初始状态 i = 1（当前初始值）, j = 1（边界值）, s = i（累加结果）
 * 1.s累加++j，直到累加结果大于等于sum
 * 2.若累加结果等于sum，则将从 i 到 j 的序列加入结果集中
 * 3.若累加结果大于sum，则开始下一循环
 * 4.在做完2,3步骤后，需要减去i，这步相当于完成了从i++ 到 j 的累加，所以不需要再初始化j的值了
 */