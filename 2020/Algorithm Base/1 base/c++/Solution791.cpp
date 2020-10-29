/**
 * 高精度加法
 * 给定两个正整数，计算它们的和。
 * 
 * 输入格式
 * 共两行，每行包含一个整数。
 * 
 * 输出格式
 * 共一行，包含所求的和。
 * 
 * 数据范围
 * 1≤整数长度≤100000
 * 
 * 输入样例：
 * 12
 * 23
 * 
 * 输出样例：
 * 35
 */

#include<iostream>
#include<cstring>
#include<vector>
using namespace std;

vector<int> add(vector<int> &A, vector<int> &B){
	vector<int> C;
	int i = 0, t = 0;
	
	// 该写法过于啰嗦

	// 取较小的size
	// int A_size = A.size(), B_size = B.size();
	// int size = A_size > B_size ? B_size : A_size;

	// for(; i < size; ++ i){
	// 	int num = A[i] + B[i];
	// 	// 需要进位
	// 	if(num + t > 9) {
	// 		C.push_back(num + t - 10);
	// 		// 之前t等于0，则改为1
	// 		if(!t) t = 1;
	// 	} else { // 不需进位
	// 		C.push_back(num + t);
	// 		// 之前t等于1，则改为0
	// 		if(t) t = 0;
	// 	}
	// }

	// // 扫尾
	// while(i < A_size) {
	//     if(A[i] + t > 9){
	// 		C.push_back(A[i ++] + t - 10);
	// 		// 之前t等于0，则改为1
	// 		if(!t) t = 1;
	// 	} else { // 不需进位
	// 		C.push_back(A[i ++] + t);
	// 		// 之前t等于1，则改为0
	// 		if(t) t = 0;
	//     }
	// }
	
	// while(i < B_size) {
	//     if(B[i] + t > 9){
	// 		C.push_back(B[i ++] + t - 10);
	// 		// 之前t等于0，则改为1
	// 		if(!t) t = 1;
	// 	} else { // 不需进位
	// 		C.push_back(B[i ++] + t);
	// 		// 之前t等于1，则改为0
	// 		if(t) t = 0;
	//     }
	// }
	
	for(; i < A.size() || i < B.size(); ++ i){
		if(i < A.size()) t += A[i];
		if(i < B.size()) t += B[i];
		C.push_back(t % 10);
		t /= 10;
	}

	if(t) C.push_back(t);

	return C;
}

int main(){
    
    string a,b;
    cin >> a >> b;
    vector<int> A, B;
    
    for(int i = a.size() - 1; i >= 0; -- i) A.push_back(a[i] - '0');
    for(int i = b.size() - 1; i >= 0; -- i) B.push_back(b[i] - '0');
    
	vector<int> C = add(A, B);
	for(int i = C.size() - 1; i >= 0; -- i) cout << C[i];
	
    return 0;
}

