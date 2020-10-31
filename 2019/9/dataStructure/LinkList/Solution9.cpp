// 带头结点的单链表L,递增次序输出单链表各节点数据元素，并释放节点所占的存储空间（不使用数组）
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

void sortPrintAndFree(LinkList &L)
{
	LinkList *curr, *minPre, *min;
	int i = 0;
	// 冒泡思想
	while (L.next != nullptr) {
		curr = L.next;
		// 最小值之前的节点
		minPre = &L;
		// 最小值节点
		min = curr;

		// 先判断当前节点的下个节点是否为空
		while (curr->next != nullptr)
		{
			// 判断谁是最小值
			if(min->val > curr->next->val) {
				minPre = curr;
				min = curr->next;
			}
			// 移动当前节点指针
			curr = curr->next;
		}
		// 删除原链表中最小值节点
		minPre->next = min->next;
		cout << "第" << ++i << "个值为" << min->val << "\n";
		free(min);
	}
	free(&L);
}

int main()
{	
	LinkList *L4 = new LinkList(0, nullptr);
	LinkList *L3 = new LinkList(1, L4);
	LinkList *L2 = new LinkList(2, L3);
	LinkList *L1 = new LinkList(3, L2);
	LinkList *L0 = new LinkList(4, L1);

	LinkList *L = new LinkList();
	L->next = L0;

	sortPrintAndFree(*L);
}