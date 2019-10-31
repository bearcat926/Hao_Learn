/**
 * 逆序对的数量
 * 给定一个长度为n的整数数列，请你计算数列中的逆序对的数量。
 * 逆序对的定义如下：对于数列的第 i 个和第 j 个元素，如果满足 i < j 且 a[i] > a[j]，则其为一个逆序对；否则不是。
 * 
 * 输入格式
 * 第一行包含整数n，表示数列的长度。
 * 第二行包含 n 个整数，表示整个数列。
 * 
 * 输出格式
 * 输出一个整数，表示逆序对的个数。
 * 
 * 数据范围
 * 1≤n≤100000
 * 
 * 输入样例：
 * 6
 * 2 3 4 5 6 1
 * 
 * 输出样例：
 * 5 
 */

#include<iostream>
#include<vector>
using namespace std;

// 使用剑指中的做法，TLE
int inversePairs(vector<int>& nums) {
	int result = 0;
	int length = nums.size();
	
	// 放置子序列的前后位
    vector<int> list;
	// 放置首位位置
	list.push_back(0);
    for(int i = 1; i < length; ++ i){\
		// 当前数字是否大于之前数字，小于则为两个有序子序列中间位置
		if(nums[i] < nums[i - 1]){
			// 放置前子序列末位位置
			list.push_back(i - 1);
			// 放置后子序列前位位置
			list.push_back(i);
		}
	}
	// 放置最末子序列的末位
	list.push_back(length - 1);

	int size = list.size();
	// 开始比较
	for(int i = 0; i < size; ++(++i))
		for(int j = i + 3; j < size; ++(++j))
			// 首位大于另一个的末尾
			if(nums[list[i]] > nums[list[j]])
			    result += ((list[i + 1] - list[i] + 1) * (list[j] - list[j - 1] + 1));
			// 首位大于另一个的首位 或 末尾大于另一个的首位
			else
			    for(int a = list[i]; a <= list[i + 1]; ++a)
					for(int b = list[j - 1]; b <= list[j]; ++b)
						if(nums[a] > nums[b]) ++result;
						else break;
		
	return result;
}

// int main(){
//     int n; 
//     scanf("%d", &n);
    
//     vector<int> array;
//     int num = 0;
//     for(int i = 0; i < n; ++ i) {
//         scanf("%d", &num);
//         array.push_back(num);
//     }
    
//     int result = inversePairs(array);
    
//     printf("%d ", result);
    
//     return 0;
// }

// --------------------------------

/**
 * 分三部分处理
 * 1. 两个数字都在左边时的逆序对
 * 2. 两个数字都在右边时的逆序对
 * 3. 两个数字在左右两边时的逆序对
 * 
 * 也是TLE
 */
 
void merge_sort(int q[], int temp[], int l, int r){
    if(l >= r) return;
    
    int mid = l + r >> 1;
    
	merge_sort(q, temp, l, mid);
	merge_sort(q, temp, mid + 1, r);
	
	int i = l, j = mid + 1, k = l;
	
	while(i <= mid && j <= r)
	    if(q[i] <= q[j] ) temp[k ++] = q[i ++];
	    else temp[k ++] = q[j ++];
	    
	while(i <= mid) temp[k ++] = q[i ++];
	while(j <= r) temp[k ++] = q[j ++];
	
	for(i = l, k = l; i <= r; ) q[i ++] = temp[k ++];
}

int inversePairs(int q[], int temp[], int l, int r) {
    int mid = l + r >> 1, num = 0;
	// 先计算1,2
	for(int i = l; i < mid; i ++)
	    for(int j = i + 1; j <= mid; j ++)
	        if(q[i] > q[j]) num++;
	
	for(int i = mid + 1; i < r; i ++)
	    for(int j = i + 1; j <= r; j ++)
	        if(q[i] > q[j]) num++; 
	        
	// 排序左右两部分
	merge_sort(q, temp, l, mid);
	
	// for(int i = l; i <= r; ++ i) printf("%d ", q[i]);
	// cout << "\n" << num <<endl;
	// 第一部分单调递增，第二部分单调递减
	// 第一部分找到一个大于第二部分的数，则 num += (mid - i + 1) * (r - j + 1)
	
	// 再计算3
	for(int j = mid + 1; j <= r; j ++)
	    for(int i = l; i <= mid; i ++)
	        if(q[i] > q[j]) {
	            num += mid - i + 1;
	            break;
	        }
	
	return num;
}

// int main(){
//     int n; 
//     scanf("%d", &n);
    
//     int q[n], temp[n];
    
//     for(int i = 0; i < n; ++ i) scanf("%d", &q[i]);
    
//     int result = inversePairs(q, temp, 0, n - 1);
    
//     printf("%d ", result);
    
//     return 0;
// }

/**
 * 在上述思想上继续优化：将1、2分治拆成3
 */
const int N = 100010;

int q[N], temp[N];

long long result = 0;

long long inversePairs2ByMerge(int l, int r){
	if(l >= r) return 0;
    
    int mid = l + r >> 1;
    
	result = inversePairs2ByMerge(l, mid) + inversePairs2ByMerge(mid + 1, r);
	
	int i = l, j = mid + 1, k = l;
	while(i <= mid && j <= r)
	    if(q[i] <= q[j] ) temp[k ++] = q[i ++];
	    else {
			temp[k ++] = q[j ++];
			result += mid - i + 1;
		}
	    
	while(i <= mid) temp[k ++] = q[i ++];
	while(j <= r) temp[k ++] = q[j ++];
	
	for(i = l, k = l; i <= r; ) q[i ++] = temp[k ++];

	return result;
}

int main(){
    int n;
    scanf("%d",&n);

    for(int i = 0 ; i < n ; i ++) scanf("%d ", &q[i]);
    
    cout<< inversePairs2ByMerge(0, n - 1);
    
    return 0;
}
