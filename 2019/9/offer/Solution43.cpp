/**
 * 数据流中的中位数
 * 如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
 * 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
 */
#include<iostream>
#include<vector>
#include<queue>
using namespace std;
class Solution {
public:
	/**
	 * priority_queue<Type, Container, Functional>
	 * Type为数据类型， Container为保存数据的容器，Functional为元素比较方式。
	 * 如果不写后两个参数，那么容器默认用的是vector，比较方式默认用operator<，(即less)，也就是优先队列是大顶堆，队头元素最大。
	 * 
	 * greater和less是std实现的两个仿函数（就是使一个类的使用看上去像一个函数。其实现方式是类中实现一个operator()，
	 * 这个类就有了类似函数的行为，就是一个仿函数类了）
	 */
	priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;

    void insert(int num){
        maxHeap.push(num);
		// 利用大根堆存储前n/2个或前(n/2)+1个数字
        if(maxHeap.size() > minHeap.size() + 1)
        {
            int t = maxHeap.top();
            maxHeap.pop();
            minHeap.push(t);
        }
		// 大根堆的所有元素理应比小根堆的所有元素要小，如果违反了此规则，就需要进行元素的对换。
        while(minHeap.size() && maxHeap.top() > minHeap.top())
        {
            int t1 = maxHeap.top();
            int t2 = minHeap.top();
            maxHeap.pop(); 
			maxHeap.push(t2);
            minHeap.pop(); 
			minHeap.push(t1);
        }
    }

	double getMedian(){
		if(minHeap.size() == maxHeap.size()) return (minHeap.top() + maxHeap.top()) / 2.0;
        else return maxHeap.top();
    }   
};

int main(int argc, char const *argv[])
{
	Solution *s = new Solution();
	for(int i = 1; i <= 9; ++i){
		s->insert(i);
	}
	cout << s->getMedian();
	return 0;
}
