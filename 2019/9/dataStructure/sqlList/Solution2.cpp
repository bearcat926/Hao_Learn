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

void swap(E *a, E *b)
{
	E *temp = b;
	b = a;
	a = temp;
}

SqList reserve(SqList &l)
{
	int i = 0, j = l.length - 1;
	while(i < j){
		swap(l.data[i++],l.data[j--]);
	}

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

	for (int i = 0; i < 10; i++) 
	{
		cout << i << "值为 " << l->data[i].value << " ！\n" ;
	}

	cout << "===================================\n" ;
	SqList list = reserve(*l);

	for (int i = 0; i < 10; i++) 
	{
		cout << i << "值为 " << list.data[i].value << " ！\n" ;
	}

	return 0;
}

/**
 * 引用（&）即别名，即将一个变量与某个已经存在的对象绑定在一起。
 * 而且一旦初始化完成，引用将和它的初始化对象一只绑定在一起，因此引用必须初始化。
 * &，也是 取地址符
 * 
 * 指针（*）与引用不同，他本身就是一个对象，允许对其进行赋值和拷贝。
 * 无须在定义的时候初始化。
 * 使用 解引用符（*）可以访问指针指向的对象。
 * 
 * 建议在使用的时候初始化 所有 指针。
 */ 
