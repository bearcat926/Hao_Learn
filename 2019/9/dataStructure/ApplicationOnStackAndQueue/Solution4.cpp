#include<iostream>
#include<queue>
#include<string.h>
using namespace std;

char * Ferry_Arrange(char *str)
{
	std::queue<char> queue;
	std::queue<char> kQueue;
	std::queue<char> hQueue;
	
	int count;
	char *p = (char *)malloc(strlen(str)*sizeof(char));
	char *result = p;
	strcpy(p,str);

	while(*str){
		if(*str == 'K') kQueue.push('K');
		else hQueue.push('H');
		++str;
	}
	
	while(!kQueue.empty() && !hQueue.empty()){
		// 剩余客车大于0 且 客车上船计数小于4
		while(!kQueue.empty() && count < 4){
			queue.push(kQueue.front());
			kQueue.pop();
			++count;
		}
		// 客车上船计数小于4，则剩余货车为0，用货车代替
		if(!kQueue.empty() && count == 4) {
			queue.push(hQueue.front());
			hQueue.pop();
			count = 0;
		}
	}

	// 哪个队列空了则将另一个入队
	while(!hQueue.empty()){
		queue.push(hQueue.front());
		hQueue.pop();
	}

	while(!kQueue.empty()){
		queue.push(kQueue.front());
		kQueue.pop();
	}

	// 根据队列生成字符串
	while(!queue.empty()){
		*(p++) = queue.front();
		queue.pop();
	}

	return result;
}

int main(int argc, char const *argv[])
{
	// K表示客车，H表示货车
	char *str = (char *)"KHKHKHHKKK";
	char *result = Ferry_Arrange(str);
	cout << str << "\n" << result;
	return 0;
}
