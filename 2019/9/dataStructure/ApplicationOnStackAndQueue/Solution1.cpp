#include<iostream>
#include<stack>
using namespace std;

/**
 * 1. 遇到左括号，入栈
 * 2. 遇到有括号，出栈进行匹配，不匹配则该算术表达式有误。 
 */

bool match(char *str){
	stack<char> stack;
	int i = 0;
	char pushElement;
	while(str[i] != '\0'){
		switch (str[i])
		{
		case '{':
			stack.push(str[i]);
			break;
		case '[' :
			stack.push(str[i]);
			break;
		case '(':
			stack.push(str[i]);
			break;
		case '}':
			pushElement = stack.top();
			if(pushElement == '{') stack.pop();
			else {
				cout << "not match\n";
				return false;
			}
			break;
		case ']':
			pushElement = stack.top();
			if(pushElement == '[') stack.pop();
			else {
				cout << "not match\n";
				return false;
			}
			break;
		case ')':
			pushElement = stack.top();
			if(pushElement == '(') stack.pop();
			else {
				cout << "not match\n";
				return false;
			}
			break;
		default:
			break;
		}
		++i;
	}
	return true;
}


int main(int argc, char const *argv[])
{
	char* str = (char*)"[{()}]\0";
	const char* resultStr;
	resultStr = match(str) ? "true" : "false";
	cout << resultStr;
	return 0;
}
