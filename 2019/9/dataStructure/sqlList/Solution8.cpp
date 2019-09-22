#include<iostream>
using namespace std;

void swap(int &a, int &b)
{
	int temp = b;
	b = a;
	a = temp;
}

void reserve(int *array, int begin, int end)
{
	for(int i = begin, j = end; i < j; i++, j--){
		swap(*(array + i), *(array + j));
	}
}

void transform(int *array, int m, int n)
{
	// 将数组首位倒置  0，m-1 and m,m+n-1
	reserve(array, 0, m + n - 1);
	// 对每个子数组进行翻转
	// 0, n-1
	reserve(array, 0, n - 1);
	// n, m+n-1
	reserve(array, n, m + n - 1);
}

int main()
{
	int m = 8;
	int n = 10;

	int array[m+n];

	for (int i = 0; i < m;)
	{
		array[i++] = i * 2;
	}
	// 2, 4, ... , 16

	for (int i = m; i < m + n;)
	{
		array[i++] = i + 2;
	}
	// 11, 12, ... ,20



	for (int i = 0; i < sizeof(array)/sizeof(int)  ; i++) {
		cout << i << "值为 " << array[i] << " ！\n";
	}

	int *a = array;

	transform(a, m, n);

	cout << "=================================\n";

	for (int *e = &array[sizeof(array)/sizeof(int)]; a != e; ++a) {
		cout << "值为 " << *a << " ！\n";
	}

	return 0;
}
