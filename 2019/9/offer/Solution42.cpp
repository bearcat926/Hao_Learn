#include <iostream>
#include <vector>
using namespace std;

/**
 * 最小的k个数
 * 输入n个整数，找出其中最小的k个数。
 * 
 * 注意：
 * 数据保证k一定小于等于输入数组的长度;
 * 输出数组内元素请按从小到大顺序排序;
 * 
 * 1. 排序取前4
 * 2. 临时数组存前四  （使用该种方法）
 * 3. 创建一个大顶堆，保存k个元素，遍历数组，如果当前元素比堆顶元素小，那么就把元素放进去，然后把堆顶元素pop掉，保证堆里保存k个最小的元素。
 */


class Solution42 {
	
public:
	int partition(vector<int> &input, int start, int end)
	{
		int p = input[start];

		while(start < end){
			while(start < end && p <= input[end]) --end;
			input[start] = input[end];
			while(start < end && p >= input[start]) ++start;
			input[end] = input[start];
		}

		input[start] = p;
		return start;			
	}

	void quickSort1(vector<int> &input, int start, int end)
	{
		if(start > end) return; 
		int p = partition(input, start, end);
		quickSort1(input, start, p - 1);
		quickSort1(input, p + 1, end);
	}

	void swap1(vector<int> &input, int i, int j)
	{
		int temp = input[i];
		input[i] = input[j];
		input[j] = temp;
	}

    vector<int> getLeastNumbers_Solution(vector<int> input, int k) {
		if(!input.size()|| !k) return input; 
		if(input.size() <= k) {
			quickSort1(input, 0, input.size() - 1);
			return input;
		}

		vector<int> list(k);

        for (int i = 0; i < input.size(); ++i)
		{
			if(i < k) list[i] = input[i];
			else // 临时数组满了
			{
				// 对已满数组进行排序
				if(i == k) quickSort1(list, 0, list.size() - 1);
				int temp = input[i];
				// 末尾数大于当前数
				if(list.back() > temp){
					// 末尾数出栈
					list.pop_back();
					// 当前数入栈
					list.push_back(temp);
					// 放入指定位置
					int a = k - 2;
					int b = k - 1;
					while(list[a] > temp) swap1(list, a--, b--);
				}
			}

		}

		return list;
    }
};

int main(int argc, char const *argv[])
{
	Solution42 *s = new Solution42();
	int array[] = {10, 29, 32, 5, 33, 41, 27, 3, 39, 56, 2, 14, 17, 20, 25, 45, 52, 22, 30, 9};
	int k = 15;

	int length = sizeof(array)/sizeof(int);
	vector<int> input(length);
	for(int i = 0; i < length; ++i)
	{
		input[i] = array[i];
	}
	
	vector<int> list = s->getLeastNumbers_Solution(input, k);

	for(int i = 0; i < k; ++i){
		cout << list[i] <<" ";
	}
	return 0;
}
	