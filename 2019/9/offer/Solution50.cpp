/**
 * 最长不含重复字符的子字符串
 * 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
 * 假设字符串中只包含从’a’到’z’的字符。
 * 
 * 样例:
 * 输入："abcabc"
 * 输出：3 
 */

#include<iostream>
#include<unordered_map>
#include<cstring>
using namespace std;

class Solution {
public:

    int longestSubstringWithoutDuplication(string s) {
		int max = 0, result = 0;
        unordered_map<char, int> map;
		for(int i = 0, j = 0; i < s.length(); ++ i){
		    // 出现重复字符
			if(map[s[i]] > 0) {
			    // 指针回调
				++j;
				i = j;
				// 记录最大值
				max = max > result ? max : result;
				// 初始化
				result = 0;
				map.clear();
			}else{
			    // 对应字符位置 +1
				map[s[i]] ++;
				// 当前子串长度 +1
				result ++;
			}
		}
		
        // 防止子串直到末尾都未出现重复值
		return max > result ? max : result;
    }
};