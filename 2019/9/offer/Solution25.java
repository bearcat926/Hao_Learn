/**
 * 合并两个排序的链表
 * 输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按照递增排序的。
 */

class ListNode25 {
    int val;
    ListNode25 next;
    ListNode25(int x) { val = x; }
}
class Solution25 {
    public static ListNode25 merge(ListNode25 l1, ListNode25 l2) {
		ListNode25 dummy = new ListNode25(0);
	    ListNode25 curr = dummy;
	    
        while (l1 != null && l2 != null) {
			if (l1.val >= l2.val) {
				curr.next = l2;
				l2 = l2.next;
			} else {
				curr.next = l1;
				l1 = l1.next;
			}
			curr = curr.next;
		}
		
		if (l1 != null) curr.next = l1;
		else curr.next = l2;
		
		return dummy.next;
	}
	
	public static void insert(ListNode25 l1, ListNode25 l2) {
		ListNode25 next = l1.next;
		l1.next = l2;
		l2.next = next;
    }
}