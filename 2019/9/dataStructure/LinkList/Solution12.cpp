// 将一个带头结点的单链表A分解为两个带头结点的单链表A、B， A存序号为奇数的元素，B存序号为偶数的元素，并保持其相对顺序不变
// 带头结点的单链表L,递增有序
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

void deleteDuplicate(LinkList &A)
{
	if(A.next == nullptr) return;

	LinkList *curr = &A;
	LinkList *next;

	while (curr->next != nullptr)
	{	
		// 减少一次判断
		next = curr->next;

		while (next != nullptr && curr->next->val == next->val) next = next->next;

		// 先移动当前指针，若重复则可留下一个重复节点
		curr = curr->next;
		// 重复
		if(curr->next != next) { 
			curr->next = next;
		}
	}
}

int main()
{	
	LinkList *L4 = new LinkList(5, nullptr);
	LinkList *L3 = new LinkList(3, L4);
	LinkList *L2 = new LinkList(3, L3);
	LinkList *L1 = new LinkList(1, L2);
	LinkList *L0 = new LinkList(1, L1);

	LinkList *A = new LinkList();
	A->next = L0;

	deleteDuplicate(*A);

	while(A->next != nullptr){
		A = A->next;
		cout << A->val << " !\n";
	}

}