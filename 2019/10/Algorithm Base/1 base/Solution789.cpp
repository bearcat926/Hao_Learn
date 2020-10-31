/**
 * 数的范围
 * 给定一个按照升序排列的长度为n的整数数组，以及 q 个查询。
 * 对于每个查询，返回一个元素k的起始位置和终止位置（位置从0开始计数）。
 * 如果数组中不存在该元素，则返回“-1 -1”。
 * 
 * 输入格式
 * 第一行包含整数n和q，表示数组长度和询问个数。
 * 第二行包含n个整数（均在1~10000范围内），表示完整数组。
 * 接下来q行，每行包含一个整数k，表示一个询问元素。
 * 
 * 输出格式
 * 共q行，每行包含两个整数，表示所求元素的起始位置和终止位置。
 * 如果数组中不存在该元素，则返回“-1 -1”。
 * 
 * 数据范围
 * 1≤n≤100000
 * 1≤q≤10000
 * 1≤k≤10000
 * 
 * 输入样例：
 * 6 3
 * 1 2 2 3 3 4
 * 3
 * 4
 * 5
 * 
 * 输出样例：
 * 3 4
 * 5 5
 * -1 -1
 */

#include<iostream>
#include<vector>
using namespace std;

const int N = 100010;

int arr[N];
vector<vector<int>> res;

void binary_search(int l, int r, int k){
    int i = l, j = r, mid = 0;
    
    while(i >= l && j <= r && i <= j && arr[mid] != k){
        mid = i + j >> 1;
		// 小于k，去左边找
        if(arr[mid] < k) i = mid + 1;
		// 大于k，去右边找
        else if(arr[mid] > k) j = mid - 1;     
    }

	// 没找到的情况
    if(i > j) res.push_back(vector<int>{-1, -1}); 
	else{
		// 只有一个数字时
		if(i == j && arr[mid] == k) {
		    res.push_back(vector<int>{i, j}); 
		    return;
		}
		// 在区间中寻找
		i = mid - 1;
		j = mid + 1;
		while(i >= l || j <= r){
			// 左侧边界值：i >= l && arr[i] < k && arr[i + 1] == k
			if(i >= l && arr[i + 1] == k) {
				if(arr[i] < k) l = i + 1;
				else i --;
			}
			// 右侧边界值：j <= r && arr[j - 1] == k && arr[j] > k
			if(j <= r && arr[j - 1] == k) {
				if(arr[j] > k) r = j - 1;
				else j ++;
			}
		}
		// 找到了一个值
		res.push_back(vector<int>{l, r}); 
	}
}

int main(){
    int n, q, k;
    scanf("%d %d", &n, &q);

    for(int i = 0; i < n; ++ i) scanf("%d", &arr[i]);
    
    for(int i = 0; i < q; ++ i) {
        cin >> k;
        binary_search(0, n - 1, k);
    }
    
    for(auto x : res){
        for(auto y : x)
            cout << y << " ";
        cout << endl;
    }
            
    return 0;
}

/**
 * 整数二分模板
 * 注：二分的本质不是单调性，有单调性必定可以二分，但是二分不一定必须有单调性。
 */

bool check(int mid){
	//..
}

// 适用于区间[l, r]被划分为[l, mid]和[mid + 1, r]时使用
int binary_1(int l, int r){
	while(l < r){
		int mid = l + r >> 1;
		if(check(mid)) l = mid + 1;
		else r = mid;
	}
	return l;
}
// 适用于区间[l, r]被划分为[l, mid - 1]和[mid, r]时使用
int binary_2(int l, int r){
	while(l < r){
		int mid = l + r + 1 >> 1;
		if(check(mid)) l = mid;
		else r = mid - 1;
	}
	return l;
}


// 使用二分模板 - 分别找到左右边界
#include <iostream>
using namespace std;

const int N = 100010;

int n, m;
int q[N];

int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i ++ ) scanf("%d", &q[i]);

    while (m -- )
    {
        int x;
        scanf("%d", &x);

        int l = 0, r = n - 1;
        while (l < r)
        {
            int mid = l + r >> 1;
			// 小 | x + 大
			// 找到左边界
            if (q[mid] >= x) r = mid;
            else l = mid + 1;
        }

        if (q[l] != x) cout << "-1 -1" << endl;
        else
        {
            cout << l << ' ';

            int l = 0, r = n - 1;
            while (l < r)
            {
                int mid = l + r + 1 >> 1;
				// 小 + x | 大
				// 找到右边界
                if (q[mid] <= x) l = mid;
                else r = mid - 1;
            }

            cout << l << endl;
        }
    }

    return 0;
}