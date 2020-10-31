#include<iostream>
#include<stack>
#include<vector>
using namespace std;

int p(int n, int x){
	if(n == 0) return 1;
	if(n == 1) return 2*x;

	return 2*x*p(n-1,x) - 2*(n-1)*p(n-2,x);
}

int pByStack(int n, int x){
	stack<vector<int>> stack;
	int p_0 = 1;
	int p_1 = 2*x;
	
	int k = n;
	while(k > 1){
		vector<int> list(2);
		list[0] = k;
		stack.push(list);
		--k;
	}

	int fn_1 = p_1;
	int fn_2 = p_0;
	while(!stack.empty()){
		vector<int> list = stack.top();
		list[1] = p_1 * fn_1 - 2 * (list[0] - 1) * fn_2;
		fn_2 = fn_1;
		fn_1 = list[1];
		stack.pop();
	}

	cout << fn_1 << "\n";
	return fn_1;
}

int main(int argc, char const *argv[])
{
	int n = 5, k = 2;
	char *str;
	str = (char *) (pByStack(n,k) == p(n,k) ? "true":"false");
	cout << str;
	return 0;
}