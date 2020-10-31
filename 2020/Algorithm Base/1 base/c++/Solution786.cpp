/**
 * 第k个数
 * 给定一个长度为n的整数数列，以及一个整数k，请用快速选择算法求出数列的第k小的数是多少。
 * 
 * 输入格式
 * 第一行包含两个整数 n 和 k。
 * 第二行包含 n 个整数（所有整数均在1~109范围内），表示整数数列。
 * 
 * 输出格式
 * 输出一个整数，表示数列的第k小数。
 * 
 * 数据范围
 * 1≤n≤100000,
 * 1≤k≤n
 * 
 * 输入样例：
 * 5 3
 * 2 4 1 5 3
 * 
 * 输出样例：
 * 3
 * 
 * 快速选择时间复杂度为O(n)
 * 
 * 思想是利用快排，判断partition 和 k之间的关系
 * p >= k -> k在前一部分，否则k在后一部分
 * 循环判断，直到i == j，输出数组中的第k - 1个数
 */

#include<iostream>
using namespace std;

int partition(int array[], int i, int j){
	int p = array[i];
	while(i < j){
		while(i < j && p <= array[j]) -- j;
		array[i] = array[j];
		while(i < j && array[i] <= p) ++ i;
		array[j] = array[i];
	}
	array[i] = p;
	return i;
}

void quick_select(int array[], int i, int j, int k){ 
	int p = 0;
	while(i < j){
		p = partition(array, i, j);
		if(p >= k) j = p - 1;
		else i = p + 1;
	}
}

int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    
    int array[n];
    for (int i = 0; i < n; i ++ ) scanf("%d", &array[i]);

    quick_select(array, 0, n - 1, k);
    
	// 第1小 = array[0]
	// 第k小 = array[k - 1]
    printf("%d ", array[k - 1]);
    return 0;
}



