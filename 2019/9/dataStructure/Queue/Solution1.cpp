#include <iostream>
using namespace std;

#define Element int
#define MaxSize 50

struct Queue{
	// 入队是0，出队是1
	int tag = 1, front = 0, rear = 0;
	Element data[MaxSize];

	// 入队
	bool EnQueue(Element x){
		// 检查队满
		if(front == rear && tag == 0) return false;
		data[front] = x;
		front = (++front) % MaxSize;
		tag = 0;
		return true;
	}
	// 出队
	bool DeQueue(Element &x){
		// 检查队空
		if(front == rear && tag == 1) return false;
		x = data[rear];
		rear = (++rear) % MaxSize;
		tag = 1;
		return true;
	}
};
