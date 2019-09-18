#include<iostream>
using namespace std;

// 0, ... , p , ... , n-1
// 0 ~ p-1 是一个数组
// p ~ n-1 是一个数组
// p , ... , n-1 , 0, ... , p-1

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

void core(int *array, int m, int n)
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

	int n = 10;
	int array[n];

	for (int i = 0; i < n; i++) array[i] = i;


	for (int i = 0; i < sizeof(array)/sizeof(int)  ; i++) {
		cout << i << "值为 " << array[i] << " ！\n";
	}

	int *a = array;

	int p = 6;
	core(a, p, sizeof(array)/sizeof(int) - p);
	
	cout << "=================================\n";

	for (int *e = &array[sizeof(array)/sizeof(int)]; a != e; ++a) {
		cout << "值为 " << *a << " ！\n";
	}

	return 0;
}