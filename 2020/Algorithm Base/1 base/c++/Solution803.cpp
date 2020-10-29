/**
 * 区间合并
 * 
 * 给定 n 个区间 [li,ri]，要求合并所有有交集的区间。
 * 注意如果在端点处相交，也算有交集。
 * 输出合并完成后的区间个数。
 * 例如：[1,3]和[2,6]可以合并为一个区间[1,6]。
 * 
 * 输入格式
 * 第一行包含整数n。
 * 接下来n行，每行包含两个整数 l 和 r。
 * 
 * 输出格式
 * 共一行，包含一个整数，表示合并区间完成后的区间个数。
 * 
 * 数据范围
 * 1 ≤ n ≤ 100000,
 * −10^9 ≤ li ≤ ri ≤ 10^9
 * 
 * 输入样例：
 * 5
 * 1 2
 * 2 4
 * 5 6
 * 7 8
 * 7 9
 * 
 * 输出样例：
 * 3
 */

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

const int N = 1e5 + 10;

typedef pair<int, int> PII;

vector<PII> segs;

void merge_seg(vector<PII> &segs){
    vector<PII> res;
    // 1.排序
    sort(segs.begin(), segs.end());
    // 2.合并
    int start = -2e9, end = -2e9;
    
    for(auto seg : segs){
        // 处理下一个区间
        if(seg.first > end){
            // 排除初始情况
            if(start != -2e9) res.push_back({start, end});
            start = seg.first;
            end = seg.second;
        }
        else end = max(end, seg.second);
    }
    
    // 处理最后一个区间
    if(start != -2e9) res.push_back({start, end});
    
    segs = res;
}

int main(){
    int n;
    cin >> n;
    
    for(int i = 0; i < n; i ++){
        int l, r;
        cin >> l >> r;
        segs.push_back({l, r});
    }
    
    merge_seg(segs);
    
    cout << segs.size() << endl;
    
    return 0;
}