// 删除带头结点的单链表L中唯一的最小值节点
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

void deleteMin(LinkList &L)
{	
	if(L.next == nullptr) return;

	LinkList *curr = L.next;
	// 最小值之前的节点
	LinkList *minPre = &L;
	// 最小值节点
	LinkList *min = curr;

	// 先判断当前节点的下个节点是否为空
	while (curr->next != nullptr)
	{
		// 判断谁是最小值
		if(min->val > curr->next->val) {
			minPre = curr;
			min = curr->next;
		}
		// 移动当前节点指针
		curr = curr->next;
	}
	// 删除最小值节点并释放空间
	minPre->next = min->next;
	free(min);
	
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

	deleteMin(*L);

	while(L->next != nullptr){
		L = L->next;
		cout << L->val << " !\n";
	}

}