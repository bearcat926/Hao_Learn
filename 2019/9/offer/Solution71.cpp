/**
 * 圆圈中最后剩下的数字
 * 0, 1, …, n-1这n个数字(n>0)排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字。
 * 求出这个圆圈里剩下的最后一个数字。
 * 
 * 即约瑟芬环问题
 */
#include<iostream>
using namespace std;

class Solution {
public:
	/**
	 * 递推做法
	 * 
	 * 原始：0 1 2 ... n-1
	 * 杀死第m个人
	 * 结果：0 1 2 ... (m-1) m m+1 ...  n-1
	 * 
	 * 旧：m m+1 ... m-2
	 * 新：0   1 ... n-2
	 * 
	 * 新(0) + m = 旧(m)
	 * 新(n-2) + m = m - 2 + n = 旧(m-2)
	 * 所以：(新 + m) % n = 旧
	 * 递推关系是 f(n,m) = (f(n-1,m) + m) % n
	 * 
	 * 边界为 f(1,n) = 0
	 */
    int lastRemaining(int n, int m){
        if(n == 1) return 0;
		return (lastRemaining(n-1,m) + m) % n;
    }
};