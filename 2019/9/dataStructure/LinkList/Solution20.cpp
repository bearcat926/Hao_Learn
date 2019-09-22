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
	int freq = 0;

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

DLinkList Locate(DLinkList L, int x){

	DLinkList *p = &L, *q = &L, *temp;
	DLinkList *node;

	// 找到值为x的所有节点将其freq加一
	while (p->next != nullptr){
		if(p->next->val == x){
			// 取需要更改的节点，将其freq加一
			node = p->next;
			++(node->freq);
			// 安排该节点的前置节点和后置节点，此处约等于删除源节点
			p->next = node->next;
			// 此处可能为空，即node为末尾节点
			if(p->next != nullptr) {
				p->next->prior = p;
			}

			// 找到freq相同的值，头插法
			q = &L;
			while (q->next != nullptr && node->freq < q->next->freq) q = q->next;
			// 取freq相同或者小于的后置节点
			if (q->next == nullptr) {	// q处于末尾，且node的freq依旧小于q
				q->next = node;
				node->prior = q;
			}else{
				temp = q->next;
				// 与前置节点关系
				q->next = node;
				node->prior = q;
				// 与后置节点关系
				node->next = temp;
				temp->prior = node;
			}
		} else {
			p = p->next;
		}
	}
	
	return L;
}

int main()
{	
	// 顺时针
	DLinkList *A = new DLinkList();

	DLinkList *r1 = new DLinkList(1);
	DLinkList *r2 = new DLinkList(2);
	DLinkList *r3 = new DLinkList(3);

	DLinkList *l3 = new DLinkList(4);
	DLinkList *l2 = new DLinkList(5);
	DLinkList *l1 = new DLinkList(5);

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

	int x = 5;

	DLinkList node = Locate(*A, x);
	
	while(node.next != nullptr){
		node = *node.next;
		cout << node.val << " !\n";
	}
}