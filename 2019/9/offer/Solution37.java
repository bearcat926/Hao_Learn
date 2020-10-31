/**
 * 复杂链表的复刻
 * 请实现一个函数可以复制一个复杂链表。
 * 在复杂链表中，每个结点除了有一个指针指向下一个结点外，还有一个额外的指针指向链表中的任意结点或者null。
 * 注意：函数结束后原链表要与输入时保持一致。
 */
class Solution37 {

	// 时间复杂度 O(n^2)
    public ListNode copyRandomList(ListNode head) {
		ListNode copyHead = new ListNode(head.val);
		ListNode p = head;
		while(p.next != null){
			copyHead.next = new ListNode(p.next.val);
		}

		p = copyHead;
		ListNode q = head;
		while(q != null){
			if(q.random != null){
				ListNode i = copyHead;
				while(q.random.val != i.val) i = i.next;
				p.random = i;
			}
			p = p.next;
			q = q.next;
		}

		return copyHead;
	}

	/**
	 * 1. 在每个链表节点后加一个复刻
	 * 2. 复刻的random  = 原链表节点的random的复刻
	 * 3. 遍历复原并将新链表取出
	 * 时间复杂度 O(n)
	 * @param head
	 * @return
	 */
	public ListNode copyRandomList2(ListNode head) {	
		if(head == null) return null;	
		ListNode p = head;
		ListNode next, newNode;

		// 1. 复刻
		while(p != null){
			next = p.next;
			newNode = new ListNode(p.val);
			p.next = newNode;
			newNode.next = next;
			p = next;
		}

		p = head;
		ListNode random;
		// 2. random
		while(p != null){
			next = p.next;
			if(p.random != null){
				random = p.random;
				next.random = random.next;
			}
			p = next.next;
		}

		// 3. 复原并取出新链表
		p = head;
		ListNode copyHead = head.next;
		ListNode q; 
		while(p != null){
			q = p.next;
			// 原来的next
			next = q.next;
			// 修改新链表的下一节点
			if (next != null) q.next = next.next;
			// 复原链表的下一节点
			p.next = next;
			p = next;
		}

		return copyHead;
	}
	
}

class ListNode {
    int val;
    ListNode next, random;
    ListNode(int x) { this.val = x; }
}
