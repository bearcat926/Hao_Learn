// 合并两个无头结点的升序单链表为一个有头结点的升序单链表,之后就地逆序
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

void reverse(LinkList &L)
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

void ConbineA_B(LinkList &A, LinkList &B, LinkList &L)
{
	if(&A == nullptr) {
		L.next = &B;
		return;
	}
	if(&B == nullptr){
		L.next = &A;
		return;
	}

	LinkList *ta = &A, *tb = &B, *tl = &L, *min;

	if(ta->val > tb->val) {
		tl->next = tb;
		tb = tb->next;
	} else {
		tl->next = ta;
		ta = ta->next;
	}

	tl = tl->next;

	while (ta != nullptr && tb != nullptr) {
		if(ta->val > tb->val) {
			min = tb;
			tb = tb->next;
			tl->next = min; 
		} else {
			min = ta;
			ta = ta->next;
			tl->next = min; 
		}
		tl = tl->next;
	}	

	if(ta != nullptr) tl->next = ta;
	else tl->next = tb;

	reverse(L);
}

int main()
{	
	LinkList *L14 = new LinkList(8, nullptr);
	LinkList *L13 = new LinkList(6, L14);
	LinkList *L12 = new LinkList(4, L13);
	LinkList *L11 = new LinkList(2, L12);
	LinkList *A = new LinkList(0, L11);

	LinkList *L24 = new LinkList(9, nullptr);
	LinkList *L23 = new LinkList(7, L24);
	LinkList *L22 = new LinkList(5, L23);
	LinkList *L21 = new LinkList(3, L22);
	LinkList *B = new LinkList(1, L21);

	LinkList *L = new LinkList();

	ConbineA_B(*A, *B, *L);
	
	while(L->next != nullptr){
		L = L->next;
		cout << L->val << " !\n";
	}
}