#include<iostream>

using namespace std;

struct E
{
	int value = 0;

	E(){}

	E(int v){
		this->value = v;
	}
};

struct SqList
{
	E *data;
	int length, MaxSize = 16;
	const double threshold = 0.75;

	SqList(){}

	SqList(int length){
		while (length >= (threshold * MaxSize)) MaxSize <<= 1;
		this->length = length;
		data = new E[MaxSize];
	}

	void addElem(E *e, int pos){
		int newLength = length + 1 > pos + 1? length + 1 : pos + 1;
		if (newLength >= (threshold * MaxSize)) {
			while (newLength < (threshold * MaxSize)) MaxSize <<= 1;
			// 扩容
			E *newData;
			newData = new E[MaxSize];
			for (int i = 0; i < newLength;i++) {
				if (i != pos) newData[i] = data[i];
				else newData[i] = *e;
			}
			data = newData;
		} else {
			for (int i = length; i > pos; i--) {
				data[i] = data[i - 1];
			}
			data[pos] = *e;
		}
		length = newLength;
	}
};

void swap(E &a, E &b)
{
	E temp = b;
	b = a;
	a = temp;
}

void binarySearch(SqList &l, int x){
	int length = l.length;

	int start = 0;
	int end = length - 1;
	int mid = 0;
	while(start < end){
		mid = (start + end) / 2;
		// 等于中值
		if(l.data[mid].value == x) {
			swap(l.data[mid], l.data[mid + 1]);
			return;
		}
		// 大于中值
		else if (l.data[mid].value < x) start = mid + 1;
		// 小于中值
		else end = mid - 1;
	}

	int pos;
	// 数组越界
	if(start == 9) pos = start + 1;
	else pos = start;

	l.addElem(new E(x), pos);
}

int main()
{
	int length = 10;
	E *eList = new E[length];
	E *e;
	for (int i = 0; i < length; i++) {
		if(i != 5){
			e = new E(i);
			eList[i] = *e;
		} else {
			e = new E(6);
			eList[i] = *e;
		}
	}
	SqList *l = new SqList(length);
	l->data = eList;

	for (int i = 0; i < l->length; i++) {
		cout << i << "值为 " << l->data[i].value << " ！\n";
	}

	cout << "================================================\n";

	binarySearch(*l, 5);

	for (int i = 0; i < l->length; i++) {
		cout << i << "值为 " << l->data[i].value << " ！\n";
	}

	return 0;
}