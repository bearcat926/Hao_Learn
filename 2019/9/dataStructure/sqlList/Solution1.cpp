#include <iostream>

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

bool del_min(SqList &l, E e)
{
	// nullptr 为 c++ 11 中的特性
	if (&l == nullptr || l.length == 0)
		return false;

	int pos;
	e = l.data[0];

	for (int i = 1; i < l.length; i++)
	{
		if (e.value > l.data[i].value)
		{
			e = l.data[i];
			pos = i;
		}
	}
	l.data[pos] = l.data[l.length - 1];

	return true;
}

int main()
{
	SqList *l = new SqList();
	l->data = new E[10];
	E *e;

	for (int i = 0; i < 10;)
	{
		e = new E();
		e->value = 10 - i;
		l->data[i++] = *e;
	}

	// 该处需要初始化，否则引用空指针，出现 Segmentation Fault 异常
	E *a = new E();

	del_min(*l, *a);

	cout << "最小值为 " << a->value << " ！";

	return 0;
}
