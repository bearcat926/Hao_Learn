/**
 * 高精度减法
 * 给定两个正整数，计算它们的差，计算结果可能为负数。
 * 
 * 输入格式
 * 共两行，每行包含一个整数。
 * 
 * 输出格式
 * 共一行，包含所求的差。
 * 
 * 数据范围
 * 1≤整数长度≤105
 * 
 * 输入样例：
 * 32
 * 11
 * 
 * 输出样例：
 * 21
 */

#include<iostream>
#include<cstring>
#include<vector>
using namespace std;

// 判断A是否大于等于B
bool bigger(vector<int> &A, vector<int> &B){
    if(A.size() > B.size()) return true;
    if(A.size() < B.size()) return false;
    
    // 位数相等
    for(int i = A.size() - 1; i >= 0; --i){
        if(A[i] > B[i]) return true;
        if(A[i] < B[i]) return false;
    }
    
    // 两数相等
    return true;
}

// 减法流程：末尾相减不够则借位
vector<int> NumMinus(vector<int> &A, vector<int> &B){
	vector<int> C;
	int i = 0, t = 0;

    // 判断较大的数
    if(!bigger(A, B)) return NumMinus(B, A);
    
    for(; i < A.size(); ++ i){
		t += A[i];
		if(i < B.size()) t -= B[i];
		// 1.大于等于0 -> 不变
		// 2.小于0 -> 前置位减一，借位，该位加10
		if(t < 0) C.push_back(t + 10);
		else C.push_back(t);
		t = t < 0 ? -1 : 0;
	}
	
	// 去除前面重复的0
	while(C.size() > 1 && C.back() == 0) C.pop_back();
		
	return C;
}

int main(int argc, char const *argv[])
{
	string a, b;
	cin >> a >> b; 

	vector<int> A, B;
	for(int i = a.size() - 1; i >= 0; -- i) A.push_back(a[i] - '0');
	for(int i = b.size() - 1; i >= 0; -- i) B.push_back(b[i] - '0');
	
	vector<int> C = NumMinus(A, B);
    if(!bigger(A, B)) C[C.size() - 1] = -C[C.size() - 1];
	for(int i = C.size() - 1; i >= 0; -- i) cout << C[i];

	return 0;
}
