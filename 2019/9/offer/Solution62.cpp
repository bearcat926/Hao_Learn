/**
 * 数组中只出现一次的两个数字
 * 一个整型数组里除了两个数字之外，其他的数字都出现了两次。
 * 请写程序找出这两个只出现一次的数字。
 * 你可以假设这两个数字一定存在。
 * 
 * 解法：
 * 1. 利用异或操作 -> 两个相同的数异或结果为0，任何数和 0 异或的结果都为其本身
 * 2. 若求数组中只出现一次的一个数字，使用一次异或即可得出结论
 * 3. 求两个数字时，需要利用两个数字二进制不同的某位来将数组分成两个集合 -> 两个数字必定在不同的集合中
 * 4. 由此在分别进行一次异或即可得到两个数字
 * 5. 简便写法：声明一个数，将二进制某位为0（或1）的数与其作异或操作，由此得到第一个数；将sum与该数进行异或操作，得到第二个数
 */


#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> findNumsAppearOnce(vector<int>& nums) {
		int sum = 0;
		for(auto num : nums) sum ^= num;
		// 移动k位 
		int k = 0;
		while(!((sum >> k) & 1)) ++ k;
		int first = 0;
		for(auto num : nums)
			if((num >> k) & 1)
				first ^= num;
		return vector<int>{first, sum ^ first};
    }
};