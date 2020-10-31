/**
 * 最长连续不重复子序列
 * 给定一个长度为n的整数序列，请找出最长的不包含重复数字的连续区间，输出它的长度。
 * 
 * 输入格式
 * 第一行包含整数n。
 * 第二行包含n个整数（均在0~100000范围内），表示整数序列。
 * 
 * 输出格式
 * 共一行，包含一个整数，表示最长的不包含重复数字的连续子序列的长度。
 * 
 * 数据范围
 * 1≤n≤100000
 * 
 * 输入样例：
 * 5
 * 1 2 2 3 5
 * 
 * 输出样例：
 * 3
 */

#include<iostream>
#include<unordered_map>
using namespace std;

const int N = 100010;

int q[N];
unordered_map<int, int> map;

int main(){
    int n, length = 0, max = 0;
    cin >> n;
    
    for(int i = 1; i <= n; ++ i) cin >> q[i];
    
    for(int i = 1, j = 1; j <=n; ++ j){
        if(map[q[j]]){
            // 获取重复数字的位置
            int t = map[q[j]];
            // 设置最大长度
            max = length > max ? length : max;
            // 对于 i <= t 的情况进行修正
            if(i <= t) {
                i = t + 1;
                length = j - i;
            }
        }
        map[q[j]] = j;
        ++ length;
    }    
    
    max = length > max ? length : max;
    cout << max;
}