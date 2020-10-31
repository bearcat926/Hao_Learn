// 采用带头结点的单链表保存单词，当两个单词有相同后缀时，可共享相同的后缀空间
// 找出共同后缀的起始位置

/** 
 * 先遍历两者长度，到末尾是查看是否末尾相同，相同说明两个单词有相同部分
 * 使较长的单词的临时指针后移，直至两个单词的剩余长度长度相同（较短的单词只需从头指针开始即可）
 * 比较两个单词的字母是否相同，不相同则后移指针直至相同为止
 */
#include <iostream>
using namespace std;
struct LinkList
{
	char data;
	LinkList *next = nullptr;

	LinkList(){}

	LinkList(char data)
	{	
		this->data = data;
	}

	LinkList(char data, LinkList *next)
	{
		this->data = data;
		this->next = next;
	}
};

void findSame(LinkList &str1, LinkList &str2){
	int str1Length = 0, str2Length = 0;
	LinkList *p = &str1, *q = &str2;
	while(p->next != nullptr && q->next != nullptr) {
		++str1Length;
		++str2Length;
		p = p->next;
		q = q->next;
	}

	// 对长单词完成遍历
	if(p->next == nullptr){
		while(q->next != nullptr) {
			++str2Length;
			q = q->next;
		}
	} else {
		while(p->next != nullptr) {
			++str1Length;
			p = p->next;
		}
	}

	// 无相同后缀
	if(p != q) return;

	p = &str1;
	q = &str2;

	// 将两个指针的长度
	if(str1Length > str2Length){
		for(int i = 0; i < (str1Length - str2Length); ++i) p = p->next;
	} else {
		for(int i = 0; i < (str2Length - str1Length); ++i) q = q->next;
	}

	// 遍历两个链表直到找到相同后缀的起始位置
	while(p != q){
		p = p->next;
		q = q->next;
	}

	cout << "相同后缀的起始位置是：" << p->data << "！";
	
} 

int main()
{
	// loading, being
	
	LinkList *L17 = new LinkList('g', nullptr);	
	LinkList *L16 = new LinkList('n', L17);	
	LinkList *L15 = new LinkList('i', L16);

	LinkList *L14 = new LinkList('d', L15);
	LinkList *L13 = new LinkList('a', L14);
	LinkList *L12 = new LinkList('o', L13);
	LinkList *L11 = new LinkList('l', L12);
	LinkList *str1 = new LinkList();
	str1->next = L11;

	LinkList *L22 = new LinkList('e', L15);
	LinkList *L21 = new LinkList('b', L22);
	LinkList *str2 = new LinkList();
	str2->next = L21;

	findSame(*str1, *str2);

	return 0;
}
 

