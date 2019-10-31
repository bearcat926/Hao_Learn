/**
 * 左旋转字符串
 * 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
 * 请定义一个函数实现字符串左旋转操作的功能。
 * 比如输入字符串"abcdefg"和数字2，该函数将返回左旋转2位得到的结果"cdefgab"。
 * 数据保证n小于等于输入字符串的长度。
 */
#include<iostream>
#include<cstring>
using namespace std;

class Solution {
public:
    string leftRotateString(string str, int n) {
		int size = str.size();
        int i = 0, j = size - 1;
		swap(str, i ,j);
		swap(str, i ,j - n);
		swap(str, j - n + 1 ,j);
		return str;
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
	string str = "abcdefg";
	Solution *s = new Solution();
	cout << s->leftRotateString(str, 2);
	return 0;
}
