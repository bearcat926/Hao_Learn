// 根据两个有头结点的升序单链表A、B，求A、B的交集，结果存于A
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


void CreateCByA_B(LinkList &A, LinkList &B)
{
	if(&A.next == nullptr || &B.next == nullptr)  return;

	LinkList *ta = &A, *tb = &B;

	while (ta->next != nullptr && tb->next != nullptr) {
		if(ta->next->val > tb->next->val) {
			tb = tb->next;
		} else if(ta->next->val < tb->next->val){
			ta->next = ta->next->next;
		} else {
			ta = ta->next;
			tb = tb->next;
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

	CreateCByA_B(*A, *B);
	
	while(A->next != nullptr){
		A = A->next;
		cout << A->val << " !\n";
	}
}