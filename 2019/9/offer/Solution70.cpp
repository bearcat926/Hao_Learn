/**
 * 扑克牌的顺子
 * 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
 * 2～10为数字本身，A为1，J为11，Q为12，K为13，大小王可以看做任意数字。
 * 为了方便，大小王均以0来表示，并且假设这副牌中大小王均有两张。
 */
#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    bool isContinuous( vector<int> numbers) {
		// 非空检测
        if(!numbers.size()) return false;
        int size = numbers.size();
		// 排序
		quickSort(numbers, 0, size - 1);
		int zero = 0, i = 0;
		// 数zero个数
		while(!numbers[i]) {
			zero ++;
			i ++;
		}
        int start = numbers[i];
		while(i < size){
		    // 用大小王替换
			if(start != numbers[i]){
				if(!zero) break;
				zero --;
			}else{ // 匹配，则下标后移
			    i++;
			}
			start++;
		}
		// zero多，或者最后一位匹配
		if(zero || (start - 1) == numbers[size - 1]) return true;
		return false;
    }

	// 优化，不用排序
	bool isContinuous( vector<int> numbers) {
		// 非空
        int size = numbers.size();
		if(!size) return false;
		// 数zero个数
		int zero = 0;
		// 找最小值或最大值
		int min = 0, max = 0, minFlag = 0;
		// 判断是否有重复值
		unordered_map<int,int> map;
		
		for(int i = 0; i < size; i ++){
			int t = numbers[i];
			if(!t) zero ++;
			else{
				// 初始化最小值
				if(!minFlag){
					min = t;
					minFlag++;
				}
				min = min < t ? min : t;
				max = max > t ? max : t;

				if(!map[t]) map[t] ++;
				else return false;
			}
		}

		// 1 3 
		// 2 2/3
		// 3 1/2/3
		int val = max - min;
		if(val == 4) return true;
		else if(val < 4) {
			if(val + zero >= 4) return true;
		} 
		return false;
    }

	int partition(vector<int> &input, int start, int end)
	{
		int t = input[start];

		while(start < end){
			while(start < end && t <= input[end]) --end;
			input[start] = input[end];
			while(start < end && t >= input[start]) ++start;
			input[end] = input[start];
		}

		input[start] = t;
		return start;			
	}

	void quickSort(vector<int> &input, int start, int end)
	{
		if(start > end) return; 
		int p = partition(input, start, end);
		quickSort(input, start, p - 1);
		quickSort(input, p + 1, end);
	}

	
};

int main(int argc, char const *argv[])
{
	int array[] = {0,9,10,11,12};
	int length = sizeof(array) / sizeof(int);
	vector<int> list;
 	for(int i = 0; i < length;++ i)
		list.push_back(array[i]);
		
	Solution *s = new Solution();
	cout << s->isContinuous(list);

	return 0;
}
