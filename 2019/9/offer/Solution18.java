/**
 * 删除链表中重复的节点
 * 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留。
 */

 /**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class ListNode18 {
    int val;
    ListNode18 next;
    ListNode18(int x) { val = x; } 
    public ListNode18 setNext(ListNode18 next) {
        this.next = next;
        return this;
    }
}
class Solution18 {
    public static ListNode18 deleteDuplication(ListNode18 head) {
        // 创建虚拟元素 dummy 指向链表头节点。
        ListNode18 dummy = new ListNode18(-1);
        dummy.next = head;

        // 创建临时节点p
        ListNode18 p = dummy;
        // 判断p的下一节点是否为空，即链表中是否还有节点
        while (p.next != null) {
            // 创建临时节点q，实则为当前节点
            ListNode18 q = p.next;
            // 如果遇到重复链表，则一直移动指针直到遇到 值不相等的节点 或者 null（可以防止末尾的重复链表）
            while (q != null && p.next.val == q.val) 
                q = q.next;

            // 未重复，则移动到下一节点
            if (p.next.next == q) 
                p = p.next;
            else // 重复，则删除对中间重复的链表的引用
                p.next = q;
        }
        return dummy.next;  
    }

    public static void main(String[] args) {
        

        ListNode18 listNode5 = new ListNode18(5);
        ListNode18 listNode4 = new ListNode18(4).setNext(listNode5);
        ListNode18 listNode3 = new ListNode18(4).setNext(listNode4);
        ListNode18 listNode2 = new ListNode18(3).setNext(listNode3);
        ListNode18 listNode111 = new ListNode18(3).setNext(listNode2);
        ListNode18 listNode11 = new ListNode18(2).setNext(listNode111);
        ListNode18 listNode1 = new ListNode18(1).setNext(listNode11);
        ListNode18 tNode = listNode1;
        while (tNode != null) {
            System.out.print(tNode.val + " ");
            tNode = tNode.next;
        }
        long startTime = System.nanoTime();
		ListNode18 l = deleteDuplication(listNode1);
		long endTime = System.nanoTime();
        System.out.println("time：" + (endTime - startTime));
        tNode = l;
        while (tNode != null) {
            System.out.print(tNode.val + " ");
            tNode = tNode.next;
        }
    }
}
