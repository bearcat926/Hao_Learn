/**
 * 求1+2+…+n
 * 求1+2+…+n,要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
 */
#include<iostream>
using namespace std;

class Solution {
public:
    int getSum(int n) {
		int res = n;
		// 利用程序执行&& ，前半部分布尔计算为假时会短路的特性，作为递归终止条件。
		n > 0 && (n += getSum(n-1));
        return res;
    }
};