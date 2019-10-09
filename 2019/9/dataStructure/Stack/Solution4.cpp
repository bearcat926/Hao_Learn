#include <iostream>
using namespace std;

struct ListNode
{
	char data;
	ListNode *next;

	ListNode(){};

	ListNode(char data, ListNode *next){
		this->data = data;
		this->next = next;
	};
};

int main(){
	int length = 0;
	
	ListNode *L6 = new ListNode('x', nullptr);
	ListNode *L5 = new ListNode('y', L6);
	ListNode *L4 = new ListNode('x', L5);
	ListNode *L3 = new ListNode('x', L4);
	ListNode *L2 = new ListNode('y', L3);
	ListNode *L1 = new ListNode('x', L2);

	ListNode *p = L1;
	while(p != nullptr) {
		length++;
		p = p->next;
	}

	if(length & 1 == 1) {
		cout << "非中心对称";
		return 0;
	}

	int mid = length / 2;
	p = L1;
	ListNode *q = new ListNode(); 
	q->next = nullptr;
	// 头插法模拟入栈
	while(mid--){
		ListNode *temp = p->next;
		p->next = q->next;
		q->next = p;
		p = temp;
	}
	
	// q出栈的结果与遍历p剩余部分的结果相同则中心对称
	q = q->next;
	while(q != nullptr){
		if(q->data == p->data){
			q = q->next;
			p = p->next;
		}else{
			cout << "非中心对称";
			return 0;
		}
	}

	cout << "中心对称";
	return 0;
}