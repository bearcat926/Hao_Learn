#include <iostream>
using namespace std;

int main(){
	char c[] = {'I', 'O', 'I', 'I', 'O', 'I', 'O', 'O'};

	int result = 0, i = 0;
	while(result >= 0 && c[i] != '\0'){
		result += c[i] == 'I' ? 1 : c[i] == 'O' ? -1 : 0;
		++i;
	}
	if(result < 0) cout << "非法序列";
	cout << result;
}