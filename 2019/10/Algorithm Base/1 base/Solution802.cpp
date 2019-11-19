/**
 * 区间和
 * 
 * 假定有一个无限长的数轴，数轴上每个坐标上的数都是0。
 * 现在，我们首先进行 n 次操作，每次操作将某一位置x上的数加c。
 * 近下来，进行 m 次询问，每个询问包含两个整数l和r，你需要求出在区间[l, r]之间的所有数的和。
 * 
 * 输入格式
 * 第一行包含两个整数n和m。
 * 接下来 n 行，每行包含两个整数x和c。
 * 再接下里 m 行，每行包含两个整数l和r。
 * 
 * 输出格式
 * 共m行，每行输出一个询问中所求的区间内数字和。
 * 
 * 数据范围
 * −10^9 ≤ x ≤ 10^9,
 * 1 ≤ n, m ≤ 10^5,
 * −10^9 ≤ l ≤ r ≤ 10^9,
 * −10000 ≤ c ≤ 10000
 * 
 * 输入样例：
 * 3 3
 * 1 2
 * 3 6
 * 7 5
 * 1 3
 * 4 6
 * 7 8
 * 
 * 输出样例：
 * 8
 * 0
 * 5
 */

// 前缀和
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef pair<int, int> PII;
/**
 * map里的元素由key和value组成，这个key和value的组合是什么类型呢？
 * 答案：pair类型
 */
const int N = 3 * 1e5 + 10;

int a[N], s[N];

// 存放插入操作的处理值
vector<PII> add;
// 存放查询操作的处理值
vector<PII> query;
// 存放原数组下标
vector<int> alls;

int find(int num){
	int l = 0, r = alls.size() - 1;
	while(l < r){
		int mid = l + r >> 1;
		if(alls[mid] >= num) r = mid;
		else l = mid + 1;
	}
	return l;
}

// unique方法的写法
vector<int>::iterator unique(vector<int> &a){
    int j = 0;
    for(int i = 0; i < a.size(); i ++)
        // 第一个数 或者 前一个数与后一个数不相同时，赋值
        if(!i || a[i] != a[i - 1])
            a[j ++] = a[i];
            
    return a.begin() + j;
}

int main(int argc, char const *argv[])
{
	int n, m;
	cin >> n >> m;
	// 初始化
	for(int i = 0; i < n; i ++) {
		int x, c;
		cin >> x >> c;
		add.push_back({x, c});
		alls.push_back(x);
	}

	for(int i = 0; i < m; i ++) {
		int l, r;
		cin >> l >> r;
		query.push_back({l, r});

		alls.push_back(l);
		alls.push_back(r);
	}

	// 对数组下标排序
	sort(alls.begin(), alls.end());
	// 对数组下标去重
	/**
	 * unique函数属于STL中比较常用函数，它的功能是元素去重。
	 * 即”删除”序列中所有相邻的重复元素(只保留一个)。
	 * 此处的删除，并不是真的删除，
	 * 而是指重复元素的位置被不重复的元素给占领了。
	 * 由于它”删除”的是相邻的重复元素，
	 * 所以在使用unique函数之前，
	 * 一般都会将目标序列进行排序。
	 */
	auto site = unique(alls.begin(), alls.end());
	/**
	 * c.erase(b,e)
	 * 从c中删除迭代器对b和e所表示的范围中的元素，返回e 
	 */
	alls.erase(site, alls.end());

	// 排序和去重的同时，做了alls数组值和原数据下标的映射

	// 处理插入
	for(auto item : add){
		int x = find(item.first);
		a[x] += item.second;
	}

	// 预处理前缀和
	for(int i = 1; i <= alls.size(); i ++) s[i] = s[i - 1] + a[i];

	// 处理询问
	for(auto item : query){
		int l = find(item.first), r = find(item.second);
		cout << s[r] - s[l - 1] << endl;
	}

	return 0;
}
