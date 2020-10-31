// 判断带头结点的循环双链表是否对称

// p,q双指针，从两个方向出发
// 当时是奇数时，两指针相等，p=q
// 偶数时，p->pr

// 判断B是否是A的连续子序列
#include <iostream>
using namespace std;
struct DLinkList
{
	int val;
	DLinkList *prior = nullptr;
	DLinkList *next = nullptr;

	DLinkList(){}

	DLinkList(int val)
	{
		this->val = val;
	}

	DLinkList(DLinkList *prior, int val, DLinkList *next)
	{
		this->prior = prior;
		this->val = val;
		this->next = next;
	}
	
};

bool isSymmetry(DLinkList &A){

	DLinkList *p = &A, *q = &A;
	int i = 0;

	while (p->next != &A && q->prior != &A) {
		p = p->next;
		q = q->prior;
		++(++i);
		if (p == q && ((i-1) & 1) == 1){
			return true;
		} else if(p->prior == q && q->next == p && (i & 1) == 0) {
			return true;
		}
	}

	return false;
}

int main()
{	
	// 顺时针
	DLinkList *A = new DLinkList(0);

	DLinkList *r1 = new DLinkList(1);
	DLinkList *r2 = new DLinkList(2);
	DLinkList *r3 = new DLinkList(3);

	DLinkList *l3 = new DLinkList(3);
	DLinkList *l2 = new DLinkList(2);
	DLinkList *l1 = new DLinkList(1);

	A->prior = l1;
	A->next = r1;

	r1->prior = A;
	r1->next = r2;

	r2->prior = r1;
	r2->next = r3;

	r3->prior = r2;
	r3->next = l3;
	
	l3->prior = r3;
	l3->next = l2;

	l2->prior = l3;
	l2->next = l1;

	l1->prior = l2;
	l1->next = A;

	char result = isSymmetry(*A) ? 't' : 'f';
	
	cout << result << " !\n";
}