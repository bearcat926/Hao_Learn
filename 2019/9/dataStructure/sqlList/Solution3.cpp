#include<iostream>

using namespace std;

struct E
{
	int value;
};

struct SqList
{
	E *data;
	int length, MaxSize;
};

SqList deleteX(SqList &l, int x)
{
	int k = 0;
	for (int i = 0; i < l.length; i++) 
	{
		if (l.data[i].value != x) 
		{
			l.data[k] = l.data[i]; 
			k++;
		}
	}
	l.length = k;

	return l;
}

int main()
{
	SqList *l = new SqList();
	l->data = new E[10];
	l->length = 10;
	E *e;

	for (int i = 0; i < 10;)
	{
		e = new E();
		e->value = 10 - i;
		l->data[i++] = *e;
	}

	SqList list = deleteX(*l, 5);

	for (int i = 0; i < list.length; i++) 
	{
		cout << i << "值为 " << list.data[i].value << " ！\n" ;
	}

	return 0;
}