#include<iostream>
#include<stack>
#include<string.h>
using namespace std;

/**
 * char* 指向内容不能修改的问题 
 * char *q =  (char *) malloc(strlen(str)*sizeof(char));
 * strcpy(q, str);
 */
char* Train_Arrange(char *train){
	char *p = train;
	char *q =  (char *) malloc(strlen(train)*sizeof(char));
	char *result = q;
	strcpy(q, train);
	stack<char> stack;
	while(*p){
		if(*p == 'H') stack.push(*p);
		else {
			*(q++) = *p;
		}
		++p;
	}
	char *c = (char *)"H";
	while(!stack.empty()){
		*(q++) = *c;
		stack.pop();
	}
	return result;
}

int main(int argc, char const *argv[])
{
	char *train = (char*) "SHSHSHSHHHSS";
	char *q;
	q = Train_Arrange(train);
	cout << q;
	return 0;
}
