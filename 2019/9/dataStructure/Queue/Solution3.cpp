#include <iostream>
#include <stack>
using namespace std;


class MyQueue {
	// s2用作cache
	stack<int> *s1, *cache;

	public:
		
		/** Initialize your data structure here. */
		MyQueue() {
			this->s1 = new stack<int>();
			this->cache = new stack<int>();
		}
		
		/** Push element x to the back of queue. */
		void Enqueue(int x) {
			// 缓存不为空，则把s2数据放进s1
			while(cache->size())
			{
				s1->push(cache->top());
				cache->pop();
			}
			s1->push(x); 
		}
		
		/** Removes the element from in front of queue and returns that element. */
		int Dequeue() {
			if(QueueEmpty()) 
			{
				cout << "pop error!\n";
				return 0;
			}
			// s1不为空，则将数据放入cache中
			while(s1->size())
			{
				cache->push(s1->top());
				s1->pop();
			}
			int x = cache->top(); 
			cache->pop(); 

			return x;
		}
		
		/** Returns whether the queue is empty. */
		bool QueueEmpty() {
			return !s1->size() && !cache->size();
		}
};

int main(int argc, char const *argv[])
{
	MyQueue obj = MyQueue();
	obj.Enqueue(1);
	obj.Enqueue(2);
	obj.Enqueue(3);
	cout << obj.Dequeue() << "\n";
	string s = obj.QueueEmpty() == 0 ? "false" : "true";
	cout << s << "\n";
 
	return 0;
}
