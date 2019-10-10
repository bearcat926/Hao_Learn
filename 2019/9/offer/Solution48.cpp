/**
 * 把数字翻译成字符串
 * 给定一个数字，我们按照如下规则把它翻译为字符串：
 * 0翻译成”a”，1翻译成”b”，……，11翻译成”l”，……，25翻译成”z”。
 * 一个数字可能有多个翻译。例如12258有5种不同的翻译，它们分别是”bccfi”、”bwfi”、”bczi”、”mcfi”和”mzi”。
 * 请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。
 * 
 * 根据字母分1位和2位的情况，若2位时大于25则不合法
 */
#include<iostream>
#include<string>
#include<vector>
using namespace std;
class Solution {
public:
	int result = 0; 
    int getTranslationCount(string s) {
		if(s.length() >= 1) matchByNoCreateString(s, 0, 1);
		if(s.length() >= 2) matchByNoCreateString(s, 0, 2);
		return result;
    }
	// length = 3
	// 0 1 2
	void match(string s,int start, int length){
		// 剩余的字符串长度
		int superfluity = s.length() - start - length;

		// 获取子串数字
		string str;
		str.assign(s, start, length);
		// 排除0*的组合
		if(str.length() == 2 && str.substr(0, 1) == "0") return;
		int num = atoi(str.c_str());
		// 大于25，则非法
		if(num > 25) return;

		// 到末尾了仍然合法，则结果 + 1
		if(!superfluity) ++result;
		// 1位子串
		if(superfluity >= 1) match(s, start + length, 1);
		// 2位子串
		if(superfluity >= 2) match(s, start + length, 2);
		return;
	}

	// 不创建新字符串的改进
	void matchByNoCreateString(string s,int start, int length){
		// 排除0*的组合
		if(length == 2) {
			if(s[start] == '0') return;
			else if(s[start] == '2' && s[start + 1] > '5') return;
			else if(s[start] > '2') return;
		}
		// 剩余的字符串长度
		int superfluity = s.length() - start - length;
		// 到末尾了仍然合法，则结果 + 1
		if(!superfluity) ++result;
		// 1位子串
		if(superfluity >= 1) matchByNoCreateString(s, start + length, 1);
		// 2位子串
		if(superfluity >= 2) matchByNoCreateString(s, start + length, 2);
		return;
	}

	// 使用dp
	int getTranslationCount1(string s) {
        int n = s.size();
		// 非0
        if(!n) return 0;
		// 1位数
        if(n == 1) return 1;

        vector<int> dp(n+1, 0);
		// 初始为1，因为数字本身是一种
        dp[n-1] = 1;
        for(int i=n-2;i>=0;i--){
            dp[i] = dp[i+1];
            if(s[i]=='1' || (s[i]=='2' && s[i+1]<'6')){
				cout << s[i] << s[i+1] << endl;
                dp[i] += dp[i+2];
            }
			cout << dp[i] << " " << dp[i + 1] << " " << dp[i + 2] << endl;
        }
        return dp[0];
    }
	/**
	 * 以dp[i]表示从字符串i位开始到末尾，最大的翻译次数。
	 * dp[i] = dp[i+1] 
	 * 
	 * 比如都是67876878，这种只有1种解码方式，不会增加 dp[i] 的值 
	 * 当 s[i]=='1'||(s[i]=='2'&&s[i+1]<'6') 这种情况的出现会使解码次数增加
	 * 
	 * 举个例子12xxxxxx;将1作为单独的一个数看，解码方法和2xxxxxx相同；
	 * 将12作为一个整体看，解码方法数量和xxxxxx相同。
	 * 
	 * 即一个合法的两位数，将为 dp[i] 增加 dp[i+2] 序列的解码方法数量，即dp[i] = dp[i+1] + dp[i+2]
	 */
};

int main(int argc, char const *argv[])
{
	Solution *s = new Solution();
	cout << s->getTranslationCount1("12258");
	return 0;
}
