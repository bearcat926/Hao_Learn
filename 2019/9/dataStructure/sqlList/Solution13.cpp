#include <iostream>
#include <cstring>
using namespace std;

int findMinPositiveInteger(int a[], int length){
	int i, *b;
	// 分配空间
	b = (int *)malloc(sizeof(int)*length);
	// malloc()函数申请的空间仅仅保证的是内存空间的大小，并不保证内存空间是否有数据垃圾清理空间
	// 使用memset()函数清理，并赋初值为0
	memset(b, 0, sizeof(int)*length);
	int *c = new int[length]();

	cout << "数组大小：" << sizeof(int)*length << ":" << sizeof(b) << ":" << sizeof(c) << " ！";
	
	for (i = 0; i < length; i++) 
		if(a[i] > 0 && a[i] <= length)
			b[a[i]] = 1;
	
	for (int i = 1; i <= length; i++){
		if(b[i] != 1) 
			return i;
	}

	return i+1;
}

int main()
{
	int array1[4] = {1, 3, 2, 3};
	int array2[3] = {1, 2, 3};

	int length = sizeof(array1) / sizeof(int);
	int  x = findMinPositiveInteger(array1, length);

	cout << "最小正整数为 " << x << " ！";
	return 0;
}