// 0553 5755
// 0553 5157

// x的数量 > n/2

#include <iostream>
#include <vector>
using namespace std;

int findX(int array[], int length)
{
	int* b = new int[length]();
	 
	for (int i = 0; i < length; i++)
	{
		// 当前数
		int num = array[i];
		// 在槽位为当前数的槽上+1
		b[num]++;
	}

	int max = 0;
	for (int i = 1; i <= length; i++) 
		if(b[max] < b[i]) max = i;

	if(b[max] > length / 2) return max;

	return -1;
}

int main()
{
	int n = 8;

	int array1[n] = {0, 5, 5, 3, 5, 7, 5, 5};
	int array2[n] = {0, 5, 5, 3, 5, 1, 5, 7};

	int length = sizeof(array1) / sizeof(int);

	int  x = findX(array1, length);

	cout << "主元素为 " << x << " ！";
	return 0;
}