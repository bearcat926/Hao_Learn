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


bool CreateCByA_B(LinkList &A, LinkList &B)
{
	if(&A.next == nullptr && &B.next == nullptr)  return true;
	if(&A.next == nullptr || &B.next == nullptr)  return false;

	LinkList *ta = &A, *tb = &B;
	LinkList *bak;

	while (ta->next != nullptr && tb->next != nullptr) {
		if(ta->next->val != tb->next->val) {
			ta = ta->next;
		} else {	// 遇到相等的值，先记录位置
			bak = ta;
			while (ta->next != nullptr && tb->next != nullptr && ta->next->val == tb->next->val) {
				ta = ta->next;
				tb = tb->next;
			}
			
			if(tb->next == nullptr) return true;
			else if(ta->next == nullptr) return false;
			
			tb = &B;
			ta = bak->next;
		}
	}	

	return false;

}

int main()
{	
	// LinkList *L14 = new LinkList(8, nullptr);
	// LinkList *L13 = new LinkList(6, L14);
	LinkList *L12 = new LinkList(8, nullptr);
	LinkList *L11 = new LinkList(5, L12);
	LinkList *B = new LinkList(1, L11);


	LinkList *L26 = new LinkList(8, nullptr);
	LinkList *L25 = new LinkList(8, L26);
	LinkList *L24 = new LinkList(5, L25);
	LinkList *L23 = new LinkList(4, L24);
	LinkList *L22 = new LinkList(5, L23);
	LinkList *L21 = new LinkList(2, L22);
	LinkList *A = new LinkList(1, L21);

	char result = CreateCByA_B(*A, *B) ? 't' : 'f';
	
	cout << result << " !\n";
}