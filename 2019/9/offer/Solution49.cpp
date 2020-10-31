/**
 * 礼物的最大价值
 * 在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
 * 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格直到到达棋盘的右下角。
 * 给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？
 * 注意：m, n > 0
 * 
 * 输入：
[
  [2,3,1],
  [1,7,1],
  [4,6,1]
]

输出：19

解释：沿着路径 2→3→7→6→1 可以得到拿到最大价值礼物。
 */

#include<iostream>
#include<vector>
#include<cstring>
using namespace std;
class Solution {
public:
    int result = 0, max = 0, m, n;
	// 右下
	int dy[2] = {0, 1};
	int dx[2] = {1, 0};

	// 回溯
    int getMaxValue(vector<vector<int>>& grid) {
		m = grid.size();
		n = grid[0].size();

		core(grid, 0 , 0);	
		return max;
    }

	void core(vector<vector<int>>& grid, int y, int x){
		result += grid[y][x];
		if(y == m - 1 && x == n - 1) {
		    max = result > max ? result : max;
			return;
		}

		for(int i = 0; i < 2; ++i){
			int a = y + dy[i];
			int b = x + dx[i];
			if(a >= 0 && a < m && b >= 0 && b < n){
				core(grid, a, b);
				result -= grid[a][b];
			}
		}
	}

	// dp：1.状态表示 2.状态转移(计算) 3.边界情况
	int getMaxValueByDp(vector<vector<int>>& grid) {
		m = grid.size();
		n = grid[0].size();

		int dp[m][n];
        memset(dp,0,sizeof(dp));

		// 将 y = 0 和 x = 0 的两行价值初始化
		dp[0][0] = grid[0][0];
		for(int i=1;i<n;i++){
            dp[0][i] = dp[0][i-1] + grid[0][i];
        }
		for(int i=1;i<m;i++){
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }

		// x，y格子的最大价值为 x-1, y 和 x, y-1 之间较大者 + x, y 的价值。
		for(int i = 1 ; i < m; ++i){
			for(int j=1 ; j < n; ++j){
                dp[i][j] = ( dp[i-1][j] > dp[i][j-1] ? dp[i-1][j] : dp[i][j-1]) + grid[i][j];
            }
		}
		
		return dp[m - 1][n - 1];
    }

	int dp(vector<vector<int>>& grid){
		m = grid.size();
		n = grid[0].size();

		// 将大小+1，可不需考虑边界问题
		vector<vector<int>> f(m + 1, vector<int>(n + 1));

		for(int i = 1; i <= m; ++ i)
			for(int j = 1; j <= n; ++j)
				f[i][j] = f[i - 1][j] > f[i][j - 1] ? f[i - 1][j] : f[i][j - 1] + grid[i - 1][j - 1];

		return f[m][n];
	}
};
