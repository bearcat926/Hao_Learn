// 删除带头结点的单链表L中所有值为 x 的节点，并释放其空间，且x节点个数不唯一
#include <iostream>
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

void deleteXCore(LinkList &node, int x)
{
	// 递归返回条件
	if(node.next == nullptr) return;

	LinkList *nextNode;

	if(node.next->val == x) {	
		//删除节点
		LinkList *clearNode = node.next;
		node.next = node.next->next;
		// 释放空间
		free(clearNode);
		// 删除，设置则下一节点为自身
		nextNode = &node;
	}else{
		// 未删除，设置为下一节点
		nextNode = node.next;
	}

	deleteXCore(*nextNode, x);
}

void deleteX(LinkList &L, int x)
{
	if(&L.next == nullptr) return;

	deleteXCore(L, x);
}

int main()
{	
	LinkList *L4 = new LinkList(4, nullptr);
	LinkList *L3 = new LinkList(3, L4);
	LinkList *L2 = new LinkList(1, L3);
	LinkList *L1 = new LinkList(1, L2);
	LinkList *L0 = new LinkList(0, L1);

	LinkList *L = new LinkList();
	L->next = L0;
	deleteX(*L, 1);
	
	while(L->next != nullptr){
		L = L->next;
		cout << L->val << " !\n";
	}

}