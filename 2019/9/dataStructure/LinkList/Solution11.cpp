// 将一个带头结点的单链表hc分解为两个带头结点的单链表A、B， A存序号为奇数的元素，B存序号为偶数的元素，并且逆序B
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

void reverse(LinkList &B)
{
	if(&B.next == nullptr) return;

	LinkList *pre = nullptr;
	LinkList *curr = B.next;
	LinkList *next = nullptr;

	while (curr->next != nullptr) {
		next = curr->next;
		curr->next = pre;
		pre = curr;
		curr = next;
	}
	curr->next = pre;
	B.next = curr;
}

void divideHcToA_B(LinkList &hc, LinkList &A, LinkList &B)
{
	// 假设0是头结点
	int num = 1;
	LinkList *tc = &hc;

	LinkList *ta = &A;
	LinkList *tb = &B;
	while (tc->next != nullptr)
	{	
		// 偶数
		if(num % 2 == 0) 
		{ 
			// 将偶数节点赋值给B的next
			tb->next = tc->next;
			// 移动tb指针
			tb = tb->next;
			// 先移动tc节点之后，交替清空后置节点
			tc = tc->next;
			ta->next = nullptr;
		} 
		else
		{ // 奇数
			// 将奇数节点赋值给A的next
			ta->next = tc->next;
			// 移动ta指针
			ta = ta->next;
			// 先移动tc节点之后，交替清空后置节点
			tc = tc->next;
			tb->next = nullptr;
		}
		++num;
	}
	reverse(B);
}

int main()
{	
	LinkList *L4 = new LinkList(5, nullptr);
	LinkList *L3 = new LinkList(4, L4);
	LinkList *L2 = new LinkList(3, L3);
	LinkList *L1 = new LinkList(2, L2);
	LinkList *L0 = new LinkList(1, L1);

	LinkList *hc = new LinkList();
	hc->next = L0;
	LinkList *A = new LinkList();
	LinkList *B = new LinkList();

	divideHcToA_B(*hc, *A, *B);

	while(A->next != nullptr){
		A = A->next;
		cout << A->val << " !\n";
	}

	cout << "================================\n";

	while(B->next != nullptr){
		B = B->next;
		cout << B->val << " !\n";
	}
}