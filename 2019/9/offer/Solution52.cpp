/**
 * 字符串中第一个只出现一次的字符
 * 在字符串中找出第一个只出现一次的字符。
 * 如输入"abaccdeff"，则输出b。
 * 如果字符串中不存在只出现一次的字符，返回#字符。
 */
#include<iostream>
#include<cstring>
#include<unordered_map>
using namespace std;

class Solution {
public:
    char firstNotRepeatingChar(string s) {
        unordered_map<char, int> map;
		char res = '#';
		int i = 0;
		while(s[i] != '\0'){
			map[s[i++]] ++;
		}

		for(int j = 0; j < s.length(); ++ j){
			if(map[s[j]]){
				res = map[s[j]];
				break;
			}
		}
		return res;
    }
};