/**
 * 不用加减乘除做加法
 * 写一个函数，求两个整数之和，要求在函数体内不得使用＋、－、×、÷ 四则运算符号。
 */
#include<iostream>
using namespace std;

class Solution {
public:
    int add(int num1, int num2){

		while(num1 != 0){
			int and_result = num1 & num2;	// 表示需要进位的二进制位
			int xor_result = num1 ^ num2;	// 表示二进制位中是1的部分
			and_result <<= 1;
			num1 = and_result;
			num2 = xor_result;
		}

		/**
		 * 用 & | ~ 实现 ^
		 * 1. (a|b)&(~a|~b)
		 * 2. ~(~a&~b)&~(a&b)
		 * 3. (a&~b)|(~a&b)
		 */
		return num2;
    }
};