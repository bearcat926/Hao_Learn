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
		if(isFull()) return false;
		data[rear] = x;
		rear = (++rear) % MaxSize;
		tag = 0;
		return true;
	}
	// 出队
	Element DeQueue(){
		// 检查队空
		if(isEmpty()) return 0;
		Element x = data[front];
		front = (++front) % MaxSize;
		tag = 1;
		return x;
	}

	bool isFull(){
		return front == rear && tag == 0;
	}

	bool isEmpty(){
		return front == rear && tag == 1;
	}
};

struct Stack{
	int top = -1;
	Element data[MaxSize];

	// 入栈
	bool EnStack(Element x){
		if(isFull()) return false;
		data[++top] = x;
		return true;
	}
	// 出栈
	Element DeStack(){
		if(isEmpty()) return 0;
		Element x = data[top--];
		return x;
	}

	bool isFull(){
		return top == MaxSize - 1;
	}

	bool isEmpty(){
		return top == -1;
	}
};

void reverse(Queue &q, Stack &s){
	Element e = 0;
	while(!q.isEmpty()){
		e = q.DeQueue();
		s.EnStack(e);
	}

	while(!s.isEmpty()){
		e = s.DeStack();
		q.EnQueue(e);
	}
} 

int main(int argc, char const *argv[])
{
	Queue *q = new Queue();
	Stack *s = new Stack();

	for(int i = 0; i < 5; ++i){
		q->EnQueue(i);
	}

	reverse(*q, *s);

	Element e = 0;
	while(!q->isEmpty()){
		e = q->DeQueue();
		cout << e << "\n";
	}

	return 0;
}
