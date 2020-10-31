/**
 * 快速排序
 * 给定你一个长度为n的整数数列。
 * 请你使用快速排序对这个数列按照从小到大进行排序。
 * 并将排好序的数列按顺序输出。
 * 
 * 输入格式
 * 输入共两行，第一行包含整数 n。
 * 第二行包含 n 个整数（所有整数均在1~109范围内），表示整个数列。
 * 
 * 输出格式
 * 输出共一行，包含 n 个整数，表示排好序的数列。
 * 
 * 数据范围
 * 1 ≤ n ≤ 100000
 * 
 * 输入样例：
 * 5
 * 3 1 2 4 5
 * 
 * 输出样例：
 * 1 2 3 4 5
 */

#include<iostream>
using namespace std;

int partition(int array[], int i, int j){
    int p = array[i];
    while(i < j){
        while(i < j && array[j] >= p) -- j;
        array[i] = array[j];
        while(i < j && array[i] <= p) ++ i; 
        array[j] = array[i];
    }
    array[i] = p;
    return i;
}

void quick_sort(int array[], int i, int j){
    if(i >= j) return;
    int p = partition(array, i, j);
    quick_sort(array, i, p - 1);
    quick_sort(array, p + 1, j);
}

int main()
{
    int n;
    scanf("%d", &n);
    
    int array[n];
    for (int i = 0; i < n; i ++ ) scanf("%d", &array[i]);

    quick_sort(array, 0, n - 1);
    
    for (int i = 0; i < n; i ++ ) printf("%d ", array[i]);
    return 0;
}