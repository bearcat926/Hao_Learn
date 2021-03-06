/**
 * 二进制中1的个数
 * 
 * 给定一个长度为n的数列，请你求出数列中每个数的二进制表示中1的个数。
 * 
 * 输入格式
 * 第一行包含整数n。
 * 第二行包含n个整数，表示整个数列。
 * 
 * 输出格式
 * 共一行，包含n个整数，其中的第 i 个数表示数列中的第 i 个数的二进制表示中1的个数。
 * 
 * 数据范围
 * 1 ≤ n ≤ 100000,
 * 0 ≤ 数列中元素的值 ≤ 10^9
 * 
 * 输入样例：
 * 5
 * 1 2 3 4 5
 * 
 * 输出样例：
 * 1 1 2 1 2
 */

/*
n   9 1001
n-1 8 1000
&     1000
n   8 1000
n-1 7 0111
&     0000  

当末尾为 01 时，n-1 的末尾为 00，& 操作会减少一位1
当末尾为 10（可以多个0） 时，n-1 的末尾为01（相应位数的多个1），因此 & 操作之后，末尾会全部变成0，因此也会减少一位1
*/
#include<iostream>
using namespace std;

const int N = 10e5 + 10;

int q[N], p[N];

int main(){

    int n;
    cin >> n;
    
    for(int i = 1; i <= n; ++ i) cin >> q[i];
    
    for(int i = 1; i <= n; ++ i){
        while (q[i] != 0) {
            q[i] &= (q[i] - 1);
            p[i] ++;
        }
    }
    
    for(int i = 1; i <= n; ++ i) cout << p[i] << " "; 
    
    return 0;
}

/**
 * n的二进制表示中，第 k 位是几
 * 
 * 1. 先把第k位移到最后一位：n >> k
 * 2. 看个位是几：x & 1
 * 
 * 取x的最后一位1及其后面的n个0所构成的一个数：x & (-x)
 */

#include<iostream>
using namespace std;

int lowbit(int x){
	return x & (-x);
}

int main(){

    int n;
    cin >> n;
    
    for(int i = 1; i <= n; ++ i){
		int x, res = 0;
		cin >> x;

		while(x) {
			x -= lowbit(x);
			res ++;
		}

		cout << res << " ";
    }
    
    return 0;
}