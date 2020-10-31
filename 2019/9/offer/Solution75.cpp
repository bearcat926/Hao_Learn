/**
 * 构建乘积数组
 * 给定一个数组A[0, 1, …, n-1]，请构建一个数组B[0, 1, …, n-1]，其中B中的元素B[i]=A[0]×A[1]×… ×A[i-1]×A[i+1]×…×A[n-1]。
 * 不能使用除法。
 * 
 * 输入：[1, 2, 3, 4, 5]
 * 输出：[120, 60, 40, 30, 24]
 */
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:

    vector<int> multiply(const vector<int>& A) {
		if(A.empty()) return vector<int>();
		int size = A.size();
        vector<int> B(size);
		
		// 将乘积数组的构建分为两部分

		/**
		 * 第一部分
		 * B0 = 1
		 * B1 = A0
		 * B2 = A0 * A1
		 */
		for(int i = 0, p = 1; i < size; ++ i){
			B[i] = p;
			p *= A[i];
		}

		/**
		 * 第二部分
		 * Bn-1 = 1
		 * Bn-2 = An-1
		 * Bn-3 = An-1 * An-2
		 * 第二次遍历需要将乘上第一次得到的结果
		 */
		for(int i = size - 1, p = 1; i >= 0; -- i){
			B[i] *= p;
			p *= A[i];
		}

		return B;
	}
};