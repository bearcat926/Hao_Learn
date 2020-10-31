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

bool deleteS_T(SqList &l, int s, int t)
{
	if(&l == nullptr || l.length == 0 || s >= t) return false;

	int k = 0;

	for (int i = 0; i < l.length; i++) 
	{
		if(l.data[i].value <= s || l.data[i].value >= t){
			l.data[k] = l.data[i];
			k++;
		}
	}
	l.length = k;

	return true;
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

	deleteS_T(*l, 3, 6);

	for (int i = 0; i < l->length; i++) 
	{
		cout << i << "值为 " << l->data[i].value << " ！\n" ;
	}

	return 0;
}