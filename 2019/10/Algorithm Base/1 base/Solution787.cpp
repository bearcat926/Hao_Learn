/**
 * 归并排序
 * 给定你一个长度为n的整数数列。
 * 请你使用归并排序对这个数列按照从小到大进行排序。
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
 * 1≤n≤100000
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

void merge_sort(int array[], int temp[], int l, int r){
    // 边界
    if(l >= r) return ;
    
    // 取中间值
    int mid = (l + r) >> 1;
    
    // 分治
    merge_sort(array, temp, l, mid);
    merge_sort(array, temp, mid + 1, r);
    
    // 合并
    // 双指针指向左右两个子数组的首位
    int i = l, j = mid + 1, k = l;
    while(i <= mid && j <= r)
        if(array[i] <= array[j]) temp[k ++] = array[i ++];
        else temp[k ++] = array[j ++];
        
    // 处理未处理的数
    while(i <= mid) temp[k ++] = array[i ++];
    while(j <= r) temp[k ++] = array[j ++];
    
    // 将temp上的排序结果赋值到原数组上
    for(i = l, j = l; i <= r; i ++, j ++)
        array[i] = temp[j];
    
}

int main(){
    int n; 
    scanf("%d", &n);
    
    int array[n],temp[n];
    for(int i = 0; i < n; ++ i) scanf("%d", &array[i]);
    
    merge_sort(array, temp, 0, n-1);
    
    for(int i = 0; i < n; ++ i) printf("%d ", array[i]);
    
    return 0;
}

