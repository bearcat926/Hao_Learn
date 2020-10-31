// 判断B是否是A的连续子序列
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


void combineAToB(LinkList &h1, LinkList &h2)
{
	LinkList *a = &h1, *b = &h2;
	while(a->next != &h1) a = a->next;
	a->next = &h2;
	while(b->next != &h2) b = b->next;
	b->next = &h1;
}

int main()
{	
	LinkList *L16 = new LinkList(6, nullptr);
	LinkList *L15 = new LinkList(5, L16);
	LinkList *L14 = new LinkList(4, L15);
	LinkList *L13 = new LinkList(3, L14);
	LinkList *L12 = new LinkList(2, L13);
	LinkList *h1 = new LinkList(1, L12);

	L16->next = h1;

	LinkList *L26 = new LinkList(6, nullptr);
	LinkList *L25 = new LinkList(5, L26);
	LinkList *L24 = new LinkList(4, L25);
	LinkList *L23 = new LinkList(3, L24);
	LinkList *L22 = new LinkList(2, L23);
	LinkList *h2 = new LinkList(1, L22);

	L26->next = h2;

	combineAToB(*h1, *h2);
	
	for (int i = 0; i < 12; i++){
		cout << h1->val << " !\n";
		h1 = h1->next;
	}
}