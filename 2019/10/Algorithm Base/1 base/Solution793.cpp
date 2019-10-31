/**
 * 高精度乘法
 * 给定两个正整数A和B，请你计算A * B的值。
 * 
 * 输入格式
 * 共两行，第一行包含整数A，第二行包含整数B。
 * 
 * 输出格式
 * 共一行，包含A * B的值。
 * 
 * 数据范围
 * 1≤A的长度≤100000,
 * 1≤B≤10000
 * 
 * 输入样例：
 * 2
 * 3
 * 
 * 输出样例：
 * 6
 */

#include<iostream>
#include<cstring>
#include<vector>
using namespace std;

vector<int> add(vector<int> &A, vector<int> &B){
    vector<int> C;
	
	if(A.size() < B.size()) return add(B, A);
    
	int i = 0, t = 0;
	
    for(; i < A.size(); ++ i){
        t += A[i];
        if(i < B.size()) t += B[i];
        C.push_back(t % 10);
        t /= 10;
	}
	
	if(t) C.push_back(t);
	
	return C;
}

vector<int> multiplication(vector<int> &A, vector<int> &B){

    vector<vector<int>> C(B.size() ,vector<int>());
	
    for(int i = 0; i < B.size(); ++ i){
		int t = 0;
		// 乘数为0，结果得0
		if(!B[i]) {
		    C[i].push_back(0);
		    continue;
		}
		// 乘数非个位，末尾补0
		for(int j = i; j > 0; -- j) C[i].push_back(0);
		// 乘法运算
		for(int k = 0; k < A.size(); ++ k){
		    t = B[i] * A[k] + t;
		    C[i].push_back(t % 10);
		    t /= 10;
		}
		// 最后首位补进位
		if(t) C[i].push_back(t);
	}
	
	// B的位数只有一位时
	if(C.size() == 1) return C[0];
	// 将所有乘法运算的结果累加起来
	for(int i = C.size() - 2; i >= 0 ; -- i){
	    vector<int> q = add(C[C.size() - 1], C[i]);
		// 数组最后一位存放结果
	    C.pop_back();
	    C.push_back(q);
	}
	
	return C[C.size() - 1];
}

int main(){
    string a, b;
	cin >> a >> b; 

	vector<int> A, B;
	for(int i = a.size() - 1; i >= 0; -- i) A.push_back(a[i] - '0');
	for(int i = b.size() - 1; i >= 0; -- i) B.push_back(b[i] - '0');
	
	vector<int> C = multiplication(A, B);
	
	for(int i = C.size() - 1; i >= 0; -- i) cout << C[i];

	return 0;
}

// 极简写法

vector<int> multiplication(vector<int> &A, int b){

    vector<int> C;
	// t % 10 取个位的值；t / 10 是需要进位的值，每次计算需要加上下次的乘积，再取个位的值
    int t = 0;
    for(int i = 0; i < A.size() || t; ++ i){
        if(i < A.size()) t += A[i] * b;
        C.push_back(t % 10);
        t /= 10;
    }
    
    return C;
}

int main(){
    string a;
    int b;
	cin >> a >> b; 

	vector<int> A;
	for(int i = a.size() - 1; i >= 0; -- i) A.push_back(a[i] - '0');
	
	vector<int> C = multiplication(A, b);
	
	for(int i = C.size() - 1; i >= 0; -- i) cout << C[i];

	return 0;
}
