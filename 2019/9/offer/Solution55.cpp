/**
 * 两个链表的第一个公共结点
 * 输入两个链表，找出它们的第一个公共结点。
 * 当不存在公共节点时，返回空节点。
 */
#include<iostream>
#include<vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
	/**
	 * 1.若没有公共结点，则末尾结点不相同
	 * 2.相同则取较短链表作为标准，将较长链表前部的多余部分刨除，
	 *  进行后边链表的遍历比较，找到相同的节点。
	 */
	/**
    ListNode *findFirstCommonNode(ListNode *headA, ListNode *headB) {
		ListNode *a = headA, *b = headB;
		int length_a = 1, length_b = 1;

        while(a->next != NULL && b->next != NULL){
			a = a->next;
			++ length_a;
			b = b->next;
			++ length_b;
		}

		if(a->next != NULL){
			while(a->next != NULL){
				a = a->next;
				++ length_a;
			}
		}else if(b->next != NULL){
			while(b->next != NULL){
				b = b->next;
				++ length_b;
			}
		}

		if(a != b) return NULL;
		
		
		int offset = length_a - length_b;
		if(offset > 0)	//a > b
			while(offset--)
				headA = headA->next;
		else if(offset < 0) //a < b
			while(offset++)
				headB = headB->next;
		
		while(headA != headB){
			headA = headA->next;
			headB = headB->next;
		}

		return headA;
    }
	*/

/**
 * 设a链表长度为a，b链表长度为b，公共长度为c
 * p节点走a+c+b，q结点走b+c+a 
 * 两个路径长度相同，则最终会在公共节点相遇
 * 时间复杂度为O(n)	
 */
	ListNode *findFirstCommonNode(ListNode *headA, ListNode *headB) {
		auto p = headA, q = headB;
		while(p != q){
			if(p) p = p->next;
			else p = headA;
			if(q) q = q->next;
			else q = headB;
		}
		return p;
    }
};