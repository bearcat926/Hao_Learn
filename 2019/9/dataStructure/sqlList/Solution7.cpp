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

SqList combine(SqList &l1, SqList &l2)
{	
	SqList *l = new SqList();
	l->length = l1.length + l2.length;
	l->data = new E[l->length];

	int i = 0, j = 0, k = 0;
	while (i < l1.length || j < l2.length)
	{
		if (i == l1.length || l1.data[i].value > l2.data[j].value) {
			l->data[k] = l2.data[j];
			j++;
		} else if (j == l2.length || l1.data[i].value <= l2.data[j].value) {
			l->data[k] = l1.data[i];
			i++;
		}
		k++;
	}
	
	return *l;
}

int main()
{
	SqList *l1 = new SqList();
	l1->data = new E[10];
	l1->length = 10;

	SqList *l2 = new SqList();
	l2->data = new E[10];
	l2->length = 10;
	
	E *e;

	for (int i = 0, j = 0; i < 10;)
	{
		e = new E();
		e->value = i;
		l1->data[i++] = *e;
		l2->data[j++] = *e;
	}

	// for (int i = 0; i < l1->length; i++) {
	// 	cout << i << "值为 " << l1->data[i].value << " ！\n";
	// }

	SqList list = combine(*l1, *l2);

	for (int i = 0; i < list.length; i++) {
		cout << i << "值为 " << list.data[i].value << " ！\n";
	}

	return 0;
}