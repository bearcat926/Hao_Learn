// 根据两个有头结点的升序单链表的公共元素产生一个有头结点的单链表C，要求不能破坏A、B结构
#include <iostream>
using namespace std;
struct LinkList
{
	int val;
	LinkList *next = nullptr;

	LinkList(){}

	LinkList(int val)
	{
		this->val = val;
	}

	LinkList(int val, LinkList *next)
	{
		this->val = val;
		this->next = next;
	}
};


void CreateCByA_B(LinkList &A, LinkList &B, LinkList &L)
{
	if(&A.next == nullptr || &B.next == nullptr)  return;

	LinkList *ta = &A, *tb = &B, *tl = &L;

	while (ta->next != nullptr && tb->next != nullptr) {
		if(ta->next->val > tb->next->val) {
			tb = tb->next;
		} else if(ta->next->val < tb->next->val){
			ta = ta->next;
		} else {
			tl->next = new LinkList(ta->next->val);
			ta = ta->next;
			tb = tb->next;
			tl = tl->next;
		}
	}	

}

int main()
{	
	LinkList *L14 = new LinkList(8, nullptr);
	LinkList *L13 = new LinkList(6, L14);
	LinkList *L12 = new LinkList(4, L13);
	LinkList *L11 = new LinkList(2, L12);
	LinkList *A = new LinkList(1, L11);

	LinkList *L24 = new LinkList(9, nullptr);
	LinkList *L23 = new LinkList(8, L24);
	LinkList *L22 = new LinkList(5, L23);
	LinkList *L21 = new LinkList(2, L22);
	LinkList *B = new LinkList(1, L21);

	LinkList *L = new LinkList();

	CreateCByA_B(*A, *B, *L);
	
	while(L->next != nullptr){
		L = L->next;
		cout << L->val << " !\n";
	}
}