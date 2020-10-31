/**
 * 字符流中第一个只出现一次的字符
 * 请实现一个函数用来找出字符流中第一个只出现一次的字符。
 * 例如，当从字符流中只读出前两个字符”go”时，第一个只出现一次的字符是’g’。
 * 当从该字符流中读出前六个字符”google”时，第一个只出现一次的字符是’l’。
 * 如果当前字符流没有存在出现一次的字符，返回#字符。 
 */
#include<iostream>
#include<unordered_map>
#include<queue>
using namespace std;
/**
 * map 用于判断重复
 * queue 存放字符流
 */
class Solution{
public:
    unordered_map<char, int> map;
	std::queue<char> queue;

    void insert(char ch){
		// 重复
        if(map[ch]) {
			char c;
			int size = queue.size();
			// 重复时遍历队列，将不重复的字符加入到队列之后
			// 重复的字符只出队列不加入队列
			for(int i = 0; i < size; ++ i){
				c = queue.front();
				// 不相等则加入
				if(ch != c) queue.push(c);
				queue.pop();
			}
		} else {
			++ map[ch];
			// 放置元素进入队列
			queue.push(ch);
		}
    }
    
    char firstAppearingOnce(){
		if(queue.size()) return queue.front();
		else return '#';
    }
};

int main(int argc, char const *argv[])
{
	string s = "AKAKjCnhEZzxUNLHhgiSIUoDjCrfKPUuoXRzyvrhtyQuNGyMtFklaxhjqWlwYizFHIDlcncfjqNCbKcAedbGrkvyCOhicczLpIcRTKUIfQsuzxAmceOKjVUNpLQrKzqryoPHMCTPhfDHhJMhnvQaJdwaboQSSVqMjKPyMGQxWnBwbPWFibHVcvphygASNQFKwdCYBJJeYCPoKhEhkVfidSSenJHinlCPQIdAoCjGeZvDWvWyxGICeODGHbQRwJuXrgveUHXtDLAWyDOAunJsgcnxFYXlnOwzRCktLABffkiAPYRsqwKwCegsSdSIvrtmAGwpOHalPXjwjOxkBwbzIUlzfefqZnYvWfWFRjVVivJgSAnMtiOJGDKHZLxaaXIHGOjBGeWTxfDjpsQwgUfTIGAtPxJPNRkTfQfNnOgsTgjvdzagXKyHcDSxeooCMfaKOuVasrmCJIOAXAHdrYduTvHWjwfRratrZizwbttBztettJdAayKqsKMVdjglXoDPScmdbxPqPUukQTBMGwxUfezQgxPgOKkKSCeyIVWqFaghFlVfkGrbAjkUdmgBIjerpNtyfSSwaxXJBtJpblXRlRqwKVKHAaftRbYOOepVSgKZBBqOaAIxpJyJnYGQakRvTnuGphVTtMzRhDmIKreYGbfPzCQwczjgxpIUAwCfTqlhqeYvILKXJRoZWleciLRoRThxYOGWCxrZLcjozyDXdfLIFYldHIzwZQRIsaybIXtgkkverRZDMtSvdfRoNjQxoKfSJMAhbGFsosvmOruSrVACLUrdTNncynCrPJCXHFyJZaZGNHPOekXOZtCOTBlpfoLMeRumULhFpLMkbMfEUYUxGZHOIrHXjkaulPhNQsysPGWnypLULcelBhrLPUvcrLXRfhHwSZdhsJpuyOFrjHYqNrGAAlNXjowmVjMOLcljjarWvwxpNSKAWfNcBVSKhLRNMZFWMiJhdjJCRZVIdTYpMHXhrjDbwMwgLdBc";
	Solution *obj = new Solution();
	int i = 0;
	while(s[i]){
		obj->insert(s[i]);
		char c = obj->firstAppearingOnce();
		cout << c << endl;
		//if(c == 'a')
		//	cout << 'a' << s[i] << endl;
		i ++;
	}
	return 0;
}
