// 给定两个单链表，找到公共节点

// 公共节点即从某一节点开始，他们的next都指向同一节点
// 其拓扑图为Y形，而不是X形
#include <iostream>
#include <cstring>
using namespace std;
struct LinkList
{
	int val;
	LinkList *next = nullptr;

	LinkList(){}

	LinkList(int val, LinkList *next)
	{
		this->val = val;
		this->next = next;
	}
};

void findPublicNode(LinkList &L1, LinkList &L2, LinkList &L)
{
	if(&L1 == nullptr || &L2 == nullptr) return;

	int L1Length = 1;
	int L2Length = 1;
	LinkList *L1Temp = &L1, *L2Temp = &L2;

	// 测量长度
	while (L1Temp->next != nullptr && L2Temp->next != nullptr) {
		++L1Length;
		++L2Length;
		L1Temp = L1Temp->next;
		L2Temp = L2Temp->next;
	};

	// L2比较长
	if(L1Temp->next == nullptr) {
		while(L2Temp->next != nullptr) 
		{
			++L2Length;
			L2Temp = L2Temp->next;
		}
		// 末尾节点不相等说明没有公共节点
		if(L1Temp != L2Temp) return;
		// 通过偏移量设置开始节点
		for (int i = L2Length - L1Length; i > 0; ++i) L2 = *L2.next; 
	} else { // L1比较长
		while(L1Temp->next != nullptr) 
		{
			++L1Length;
			L1Temp = L1Temp->next;
		}
		// 末尾节点不相等说明没有公共节点
		if(L1Temp != L2Temp) return;
		// 通过偏移量设置开始节点
		for (int i = L1Length - L2Length; i > 0; ++i) L1 = *L1.next; 
	} 

	L1Temp = &L1;
	L2Temp = &L2;
	// 遍历找公共节点
	// 在此不能使用 &L1 != &L2 判断
	while (L1Temp != L2Temp) {
		L1Temp = L1Temp->next;
		L2Temp = L2Temp->next;
	};

	L = *L1Temp;
}

int main()
{	
	LinkList *L14 = new LinkList(0, nullptr);
	LinkList *L13 = new LinkList(1, L14);
	LinkList *L12 = new LinkList(2, L13);
	LinkList *L11 = new LinkList(3, L12);
	LinkList *L10 = new LinkList(4, L11);

	
	LinkList *L21 = new LinkList(1, L12);
	LinkList *L20 = new LinkList(0, L21);

	LinkList *L = new LinkList();

	findPublicNode(*L10, *L20, *L);
	
	// 无 头结点
	while(L != nullptr){
		cout << L->val << " !\n";
		L = L->next;
	}

}