/**
 * 反转链表
 * 定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。
 */
class ListNode24 {
    int val;
    ListNode24 next;
    ListNode24(int x) { val = x; }
}

class Solution24 {
    public static ListNode24 reverseList(ListNode24 head) {
		if (head == null) return null;

		ListNode24 pre = null;
		ListNode24 curr = head;
		ListNode24 next = null;
        while (curr.next != null) {
			next = curr.next;
			curr.next = pre;
			pre = curr;
			curr = next;
		}
		curr.next = pre;
		return curr;
	}
	
}