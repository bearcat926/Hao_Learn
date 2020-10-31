// 逆序打印带头结点的单链表L中的节点
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

void reversePrint(LinkList &L)
{
	if(&L.next == nullptr) return;

	LinkList *pre = nullptr;
	LinkList *curr = L.next;
	LinkList *next = nullptr;

	while (curr->next != nullptr) {
		next = curr->next;
		curr->next = pre;
		pre = curr;
		curr = next;
	}
	curr->next = pre;
	L.next = curr;
}

int main()
{	
	LinkList *L4 = new LinkList(4, nullptr);
	LinkList *L3 = new LinkList(3, L4);
	LinkList *L2 = new LinkList(2, L3);
	LinkList *L1 = new LinkList(1, L2);
	LinkList *L0 = new LinkList(0, L1);

	LinkList *L = new LinkList();
	L->next = L0;
	reversePrint(*L);

	while(L->next != nullptr){
		L = L->next;
		cout << L->val << " !\n";
	}

}