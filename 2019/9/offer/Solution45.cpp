/**
 * 从1到n整数中1出现的次数
 * 输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。
 * 例如输入12，从1到12这些整数中包含“1”的数字有1，10，11和12，其中“1”一共出现了5次。 
 */
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int numberOf1Between1AndN_Solution(int n) {
		// 判断特值0
		if(!n) return n;
		
        int count = 0;
		// 从低到高位放置数的每一位
		vector<int> list;
		while(n) list.push_back(n % 10), n /= 10;

		// 从高位到低位
		vector<int> left(list.size());
		vector<int> right(list.size());
		vector<int> t(list.size(),1);

		// 初始化t
		for(int i = 0; i < list.size(); ++i)
			if(i != list.size() - 1) 
				t[list.size() - 2 - i] = t[list.size() - 1 - i] * 10;

		// 初始化 left 和 right
		for(int i = 0; i < list.size(); ++i)
		{
			// left 无首位
			for(int j = list.size() - 1; j > list.size() - 1 - i; --j) left[i] += list[2 * list.size() - 1 - i - j] * t[j];
			// 0
			// 1 = list[4] * t[4]
			// 12 = list[3] * t[4] + list[4] * t[3]
			// 123 = list[2] * t[4] + list[3] * t[3] + list[4] * t[2]
			// 1234 = list[1] * t[4] + list[2] * t[3] + list[3] * t[2] + list[4] * t[1]

			// 8 - 4
			// 7 - 4 , 7 - 3
			// 6 - 4 , 6 - 3 , 6 - 2
			// 5 - 4 , 5 - 3 , 5 - 2 , 5 - 1

			// 2 * list.size() - 1 - i - j
			
			// right 无末尾
			for(int j = list.size() - 1; j > i; --j) right[i] += list[list.size() - 1 - j] * t[j];
			// right[0] += list[j] * t[list.size() - 1 - j]
			// 2345 = list[0] * t[j] (j = list.size() - 1) + .. + list[3] * t[j] (j = 1) -> (j > i)
						
		}
		
		// 计算
		for(int i = 0; i < list.size(); ++i)
		{
			count += left[i] * t[i];
			if(list[list.size() - 1 - i] == 1) count += right[i] + 1;
			else if(list[list.size() - 1 - i] > 1) count += t[i];
		}

        return count; 
    }
};

int main(int argc, char const *argv[])
{
	Solution *s = new Solution();
	s->numberOf1Between1AndN_Solution(12);
	return 0;
}