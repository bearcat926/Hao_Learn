#include<iostream>
using namespace std;

// 是否是偶数
bool isEven(int length){
	return length & 1 == 0;
}

int midNumber(int a1[], int a2[], int length)
{
	int start1 = 0, end1 = length - 1;
	int start2 = 0, end2 = length - 1;
	int mid1 = 0, mid2 = 0;

	while (start1 < end1 && start2 < end2)
	{
		mid1 = (start1 + end1) / 2;
		mid2 = (start2 + end2) / 2;
		if(a1[mid1] == a2[mid2]){
			return a1[mid1];
		} else if (a1[mid1] < a2[mid2]){ // 中位数不相等时，较小的舍弃较小的部分，较大的舍弃较大的部分
			// 因为两数组长度等长，因此判断其中一个即可，偶数时，舍弃较小的比较大的少一个，因此较大的少舍弃一个
			// a1: 1, 2, 3, 4, 5
			// a2: 1, 2, 6, 7, 8
			if(isEven(end1 - start1 + 1)){
				end2 = mid2 + 1;
			}else{
				end2 = mid2;
			}
			start1 = mid1;
		} else {
			if(isEven(end1 - start1 + 1)){
				end1 = mid1 + 1;
			}else{
				end1 = mid1;
			}
			start2 = mid2;
		}
	}

	// 优化
	// 正常情况下，两个数组的长度应该是一样的
	// 如果不相同，则说明其中一方需要舍弃的值为空，即已舍弃过，却仍然不符合要求
	if (start1 == end1 && start2 != end2){
		start2++;
	} else if (start1 != end1 && start2 == end2) {
		start1++;
	}

	return a1[mid1] < a2[mid2] ? a1[start1] : a2[start2];
	
}

int main()
{
	int n = 5;

	int array1[n] = {1, 2, 3, 4, 5};
	int array2[n] = {1, 2, 6, 7, 8};
	// a1: 1, 2, 3, 4, 5
	// a2: 1, 2, 6, 7, 8


	// for (int i = 0; i < n; i++)
	// {
	// 	array1[i] = i * 2;
	// 	array2[i] = i + 2;
	// }
	// a1: 0, 2, 4, 8, 16
	// a2: 2, 3, 4, 5, 6

	// 02234 4568 16

	int length = sizeof(array1) / sizeof(int);

	int  mid_number = midNumber(array1, array2, length);

	cout << "中位数为 " << mid_number << " ！\n";

	return 0;
}