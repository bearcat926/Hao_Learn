/**
 * 把字符串转换成整数
 * 请你写一个函数StrToInt，实现把字符串转换成整数这个功能。
 * 当然，不能使用atoi或者其他类似的库函数。
 * 
 * 你的函数应满足下列条件：
 * 忽略所有行首空格，找到第一个非空格字符，可以是 ‘+/−’ 表示是正数或者负数，紧随其后找到最长的一串连续数字，将其解析成一个整数；
 * 整数后可能有任意非数字字符，请将其忽略；
 * 如果整数长度为0，则返回0；
 * 如果整数大于INT_MAX(2^31 − 1)，请返回INT_MAX；如果整数小于INT_MIN(−2^31) ，请返回INT_MIN；
 */
#include<iostream>
#include<cstring>
using namespace std;

class Solution {
public:
    int strToInt(string str) {
		//int 48 = 字符'0'
		long long num = 0, p = 1;;
		int positive = 1, i = 0;
		// 判断正负
		while(str[i] - '0' < 0 || str[i] - '9' > 0){
			if(str[i] == '-') positive = -1;
			++ i;
		}

		for(int j = str.size() - 1; j >= i; -- j){
			if(str[j] < '0' || str[j] > '9') continue;
			num += (str[j] - '0') * p;
			p *= 10;
			if(num > INT_MAX) return positive * INT_MAX;
		}

		return positive * num;
    }
};

int main(int argc, char const *argv[])
{
	Solution *s = new Solution();
	s->strToInt("   +123465");
	return 0;
}
