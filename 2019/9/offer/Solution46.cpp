/**
 * 数字序列中某一位的数字
 * 数字以0123456789101112131415…的格式序列化到一个字符序列中。
 * 在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。
 * 请写一个函数求任意位对应的数字。 
 * 
 * 个位 0123456789 10
 * 十位 10 (2) * 10 * 9 = 180
 * 百位 100 (3) * 10 * 10 * 9 = 2700
 * ... 
 * 几位数 * 10 的 几次方 = 某位数的数字数量
 * 
 */
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int digitAtIndex(int n) {
		
		if(n < 9) return n;
		
		// 位数计数， 为位数， 量级，上次计数
        long long count = 10, bits = 2, t = 9, oldCount;
		
		while(count <= n) 
		{
			oldCount = count;
			// 位数量级
			t *= 10;
			// 累加
			count += bits * t;
			// 位数 + 1;
			++bits;
		}
		
		// 计算位数后等到范围了得到范围了
		--bits;
		count -= oldCount;
		n -= oldCount;

		// count / bits 是当前bit位数的总数，除以9 可以获得初始数字，n / bits 是需要获取的数在总数中的位置
		int num = count / (bits * 9) + n / bits;
		// cout << oldCount << " "<< count << " " << n << " " << num << " " << bits << " " << n % bits << endl;
		int result;
		for (int i = n % bits; i < bits; ++i) result = num % 10, num /= 10;
		return result; 
    }

	int digitAtIndex1(int n) {
        
        long long i = 1, s = 9, base = 1;//i表示是几位数，s表示位数共有多少个，base表示位数的起始值。
         while(n > i * s) {   // 9, 90, 900, 9000, 90000, i * s表示位数总共占多少位。
             n -= i * s;         // 1000 - 9 - 90 * 2 - 900 * 3 ,当i= 3 时不符合条件，说明是在三位数里面。
             i ++;                
             s *= 10;
             base *= 10;
         }
         int number = base + (n + i - 1) / i - 1; //求位数的第几个数， 1000 - 9 - 180 = n , n / 3 + base - 1（考虑0故减1）, 向上取整 n + i - 1。
         int r = n % i ? n % i : i;              // 除不尽就是第几位，除尽力了就是最后一位。
         for (int j = 0; j < i - r; j ++) number /= 10; //求数的第i - r位，取出第i - r位。

         return number % 10;
        
    }
};

int main(int argc, char const *argv[])
{
	Solution *s = new Solution();
	cout << s->digitAtIndex(2147483647) << endl;
	return 0;
}
