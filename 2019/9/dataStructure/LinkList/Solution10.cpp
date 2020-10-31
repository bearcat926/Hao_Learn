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

void divideByOddAndEven(LinkList &A, LinkList &B)
{
	// 假设0是头结点
	int num = 1;
	LinkList *ta = &A;
	LinkList *tb = &B;
	while (ta->next != nullptr)
	{	
		// 偶数
		if(num % 2 == 0) 
		{ 
			// 将偶数节点赋值给B的next
			tb->next = ta->next;
			// 移动tb指针
			tb = tb->next;
			// 删除A表中的奇数节点
			ta->next = tb->next;
			// 置空tb的后置节点
			tb->next = nullptr;
		} else{
			// 奇数只须移动ta指针
			ta = ta->next;
		}
		++num;
	}
}

int main()
{	
	LinkList *L4 = new LinkList(5, nullptr);
	LinkList *L3 = new LinkList(4, L4);
	LinkList *L2 = new LinkList(3, L3);
	LinkList *L1 = new LinkList(2, L2);
	LinkList *L0 = new LinkList(1, L1);

	LinkList *A = new LinkList();
	A->next = L0;
	LinkList *B = new LinkList();

	divideByOddAndEven(*A, *B);

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