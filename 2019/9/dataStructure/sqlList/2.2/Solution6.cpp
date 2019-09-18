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
/*0值为 10 ！
1值为 9 ！
2值为 8 ！
3值为 7 ！
4值为 7 ！
5值为 7 ！
6值为 4 ！
7值为 3 ！
8值为 2 ！
9值为 2 ！
*/
bool deleteDuplicate(SqList &l)
{
	if(&l == nullptr || l.length == 0) return false;

	int i = 0, k = 0;
	int length = l.length;
	bool duplicate = false;
	while (i < length) {
		// 遇到重复，i + 1 == length 即 i为末尾，且仍重复
		while (i + 1 != length && l.data[i].value == l.data[i + 1].value) 
		{
			i++;
			duplicate = true;
		}

		// 重复的留一个
		l.data[k++].value = l.data[i].value;

		// 重复的都删除
		// if(i != 0 && l.data[i - 1].value == l.data[i].value)
		// {	// 非首尾末尾，i 与 i-1重复
		// 	if (i + 1 != length) l.data[k++].value = l.data[i + 1].value;
		// } else {	
		// 	if (duplicate) { // 之前遇到重复，会产生重复赋值
		// 		duplicate = false;
		// 	} else { // 不重复，则正常赋值
		// 		l.data[k++].value = l.data[i].value;
		// 	}
		// }
		i++;
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

	for (int i = 0; i < 3;)
	{
		e = new E();
		e->value = 10 - i;
		l->data[i++] = *e;
	}

	e->value = 7;
	l->data[3] = *e;
	l->data[4] = *e;
	l->data[5] = *e;
		
	for (int i = 6; i < 8;)
	{
		e = new E();
		e->value = 10 - i;
		l->data[i++] = *e;
	}

	e->value = 2;
	l->data[8] = *e;
	l->data[9] = *e;

	for (int i = 0; i < l->length; i++) 
	{
		cout << i << "值为 " << l->data[i].value << " ！\n" ;
	}

	deleteDuplicate(*l);

	for (int i = 0; i < l->length; i++) 
	{
		cout << i << "值为 " << l->data[i].value << " ！\n" ;
	}

	return 0;
}