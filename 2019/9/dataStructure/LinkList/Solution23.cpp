// 有头结点单链表保存m个整数，data的绝对值 <= n（n为正整数）
// 要求对于链表中data的绝对值相等的节点，仅保留第一次出现的结点而删除其余绝对相同的节点。

#include <iostream>
#include <cstring>
using namespace std;
struct LinkList
{
	int data;
	LinkList *link = nullptr;

	LinkList(){}

	LinkList(int data)
	{
		this->data = data;
	}

	LinkList(int data, LinkList *link)
	{
		this->data = data;
		this->link = link;
	}
};

void deleteAbsoluteIsDuplicate(LinkList &head, int n){

	// 取值范围是 1 ~ n，为了在数组中映射，所以将长度加一
	bool *array = (bool *)malloc(sizeof(int) * (n+1));
	memset(array, false, sizeof(int) * (n+1));

	LinkList *p = &head, *temp;
	int data, absolute;
	while(p->link != nullptr){
		data = p->link->data;
		absolute = data < 0 ? (~data + 1) : data;
		if(!array[absolute]){
			array[absolute] = true;
			p = p->link;
		}else{	//重复，则删除下一节点
			temp = p->link;
			p->link = temp->link;
			free(temp);
		}
	}

}

int main()
{
	LinkList *L5 = new LinkList(15, nullptr);
	LinkList *L4 = new LinkList(-7, L5);
	LinkList *L3 = new LinkList(-15, L4);
	LinkList *L2 = new LinkList(-15, L3);
	LinkList *L1 = new LinkList(21, L2);

	LinkList *head = new LinkList();
	head->link = L1;

	int n = 21;

	deleteAbsoluteIsDuplicate(*head, n);
	
	while(head->link != nullptr){
		head = head->link;
		cout << head->data << " !\n";
	}

	return 0;
}