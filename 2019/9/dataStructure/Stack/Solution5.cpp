#include <iostream>
using namespace std;

#define maxSize 100
#define element int

struct ShareStack
{
	element top[2] = {-1, maxSize};
	int data[maxSize];

	bool push(int i, element x)
	{
		if(isFull()) {
			cout << "栈满";
			return false;
		}
		// 0是s1, 1是s2
		if (i == 0) 
		{
			data[++top[i]] = x;
			return true;
		} 
		else if(i == 1) 
		{
			data[--top[i]] = x;
			return true;
		}
	}

	bool pop(int i, element &x)
	{
		// 0是s1, 1是s2
		if (i == 0) 
		{
			if(top[i] == -1) {
				cout << "s1栈空";
				return false;
			}
			x = data[top[i]--];
			return true;
		} 
		else if(i == 1) 
		{
			if(top[i] == maxSize) {
				cout << "s2栈空";
				return false;
			}
			x = data[top[i]++];
			return true;
		}
	}

	bool isFull()
	{
		return top[1] - top[0] == 1;
	}
};



