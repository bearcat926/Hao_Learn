/**
 * 骰子的点数
 * 将一个骰子投掷n次，获得的总点数为s，s的可能范围为n~6n。
 * 掷出某一点数，可能有多种掷法，例如投掷2次，掷出3点，共有[1,2],[2,1]两种掷法。
 * 请求出投掷n次，掷出n~6n点分别有多少种掷法。
 */
#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

class Solution {
public:
	
	vector<int> numberOfDice(int n) {
		vector<int> res;
        for(int i = n ; i <= 6 * n; ++i){
			res.push_back(core(i, n));
		}
		return res;
    }

	// 暴力递归
	int core(int point, int n){
		int i = 1;
		int res = 0;
		if(n == 1){
			if(point <= 6) return 1;
			else return 0;
		}
		while(i < point && i <= 6){
			res += core(point - i, n - 1);
			i++;
		}
		return res;
	}

	// 动态规划：1.状态表示 2.状态转移(计算) 3.边界情况
	vector<int> numberOfDiceByDP(int n) {
		vector<vector<int>> dp(n + 1, vector<int>(6 * n + 1));
		dp[0][0] = 1;
		// i -> 投掷次数，j -> 投掷点数，k -> 色子点数
		// dp[i][j] -> 投掷 i 次，总和是 j 的方案数，对于最后一次扔的点数为 k 时对应的方案
        for(int i = 1 ; i <= n; ++ i)
			for(int j = 1; j <= 6 * i; ++ j)
				for(int k = 1; k <= min(j, 6); ++ k){
					cout << i << " " << j << " " << k <<" : " << i - 1 << " " << j - k << endl;
					dp[i][j] += dp[i - 1][j - k];
				}
		
		vector<int> res;
		for(int i = n; i <= 6 * n ;++ i) 
			res.push_back(dp[n][i]);
		return res;
    }
	// 1 0 0 0 0 0 0
	// 0 1 1 1 1 1 1 
	// 0 0 1 2 3 4 5  6  5  4  3  2  1
	// 0 0 0 1 3 6 10 15 21 25 27 27 25 21 15 10 6 3 1 

};

int main(int argc, char const *argv[])
{
	vector<int> res;
	Solution *s = new Solution();
	res = s->numberOfDiceByDP(2);
	for(auto x : res)
		cout << x << " ";
	return 0;
}
