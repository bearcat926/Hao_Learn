// 在不改变链表的前提下，查找链表中倒数第k个位置上的节点，k为正整数。查找成功则输出该节点的值，返回1，否则返回0

/** 
 * 先遍历一遍，确定链表长度
 * 如果长度小于k，则返回0
 * 否则使用for循环，移动链表指针length-k次即可找到对应节点
 */
#include <iostream>
using namespace std;
struct LinkList
{
	int data;
	LinkList *link = nullptr;

	LinkList(){}

	LinkList(int data)
	{
		this->data = data;
	}

	LinkList(int data, LinkList *link)
	{
		this->data = data;
		this->link = link;
	}
};

int findK(LinkList head, int k){

	LinkList *p = &head;
	int length = 0;

	while(p != nullptr) {
		++length;
		p = p->link;
	}
	// 长度小于k，则返回0
	if(length < k) return 0;
	// 重置指针
	p = &head;
	for(int i = 0; i < length - k; ++i) p = p->link;
	cout << "倒数第 " << k << " 个的节点的值是 " << p->data << " ！";
	return 1;
 }

int main()
{
	LinkList *L6 = new LinkList(6, nullptr);	
	LinkList *L5 = new LinkList(5, L6);
	LinkList *L4 = new LinkList(4, L5);
	LinkList *L3 = new LinkList(3, L4);
	LinkList *L2 = new LinkList(2, L3);
	LinkList *L1 = new LinkList(1, L2);

	int k = 2;
	findK(*L1, k);

	return 0;
}
 

