/**
 * 翻转单词顺序
 * 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
 * 为简单起见，标点符号和普通字母一样处理。
 * 例如输入字符串"I am a student."，则输出"student. a am I"。
 */
#include<iostream>
#include<cstring>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
		int i = 0, j = s.size() - 1;
		swap(s, i ,j);
		j = 0;
		while(s[j] != '\0'){
			if(s[j] == ' '){
				swap(s, i, j - 1);
				i = j + 1;
			}
			j++;
		}
		swap(s, i, j - 1);
		return s;
    }
	
	void swap(string &s, int i, int j){
		while(i < j){
			char t = s[i];
			s[i++] = s[j];
			s[j--] = t; 
		}
	}
};

int main(int argc, char const *argv[])
{
	string str = "I am a student.";
	Solution *s = new Solution();
	cout << s->reverseWords(str);
	return 0;
}
