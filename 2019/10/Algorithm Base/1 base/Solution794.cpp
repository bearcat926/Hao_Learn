/**
 * 高精度除法
 * 给定两个正整数A，B，请你计算 A / B的商和余数。
 * 
 * 输入格式
 * 共两行，第一行包含整数A，第二行包含整数B。
 * 
 * 输出格式
 * 共两行，第一行输出所求的商，第二行输出所求余数。
 * 
 * 数据范围
 * 1≤A的长度≤100000,
 * 1≤B≤10000
 * 
 * 输入样例：
 * 7
 * 2
 * 
 * 输出样例：
 * 3
 * 1
 */

#include<iostream>
#include<cstring>
#include<vector>
using namespace std;

/**
 * 1. 取A的前一部分，若大于B则，做除法，记录商和余数
 * 2. 余数加到下次除法中使用
 * 3. 每次增加A的一位时，需要在C中添加一个0，且前一部分和余数都乘10
 * 4. 计算完成时，剩下的部分为余数，且需要去除前置位的0
 */
vector<int> division(vector<int> &A, int B){
    vector<int> C;
    
	int t = 0;
	for(int i = 0; i < A.size(); ++i){
		t = t * 10 + A[i];
		C.push_back(t / B);
		if(t >= B)	t = t % B;
	}
    
    int i = 0;
    while(C[i] == 0) ++ i; 
    // 开始遍历的位置
    C.push_back(i);
    // 余数
    C.push_back(t);

	return C;
}

int main(){

    string a, b;
	cin >> a >> b; 

	vector<int> A;
	int B = 0;
	for(int i = 0; i < a.size(); ++ i) A.push_back(a[i] - '0');
	for(int i = b.size() - 1, r = 1; i >= 0; -- i, r *= 10) B += (b[i] - '0') * r;
	
	vector<int> C = division(A, B);
	// 数组存放数据：前导0，商，开始遍历位置，余数
	for(int i = C[C.size() - 2]; i < C.size() - 2; ++ i) cout << C[i];
	cout << endl << C[C.size() - 1] << endl;

	return 0;
}