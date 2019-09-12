/**
 * 在O(1)时间删除链表结点
 * 给定单向链表的一个节点指针，定义一个函数在O(1)时间删除该结点。
 * 假设链表一定存在，并且该节点一定不是尾节点。
 */

 /**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode17 next;
 *     ListNode17(int x) { val = x; }
 * }
 */
class ListNode17 {
    int val;
    ListNode17 next;
    ListNode17(int x) { val = x; } 
    public ListNode17 setNext(ListNode17 next) {
        this.next = next;
        return this;
    }
}
class Solution17 {
    public static void deleteNode(ListNode17 node) {
        ListNode17 next = node.next;
        node.val = next.val;
        node.next = next.next;
    }

    public static void main(String[] args) {
        
        ListNode17 listNode8 = new ListNode17(8);
        ListNode17 listNode6 = new ListNode17(6).setNext(listNode8);
        ListNode17 listNode4 = new ListNode17(4).setNext(listNode6);
        ListNode17 listNode1 = new ListNode17(1).setNext(listNode4);
        ListNode17 tNode = listNode1;
        while (tNode != null) {
            System.out.print(tNode.val + " ");
            tNode = tNode.next;
        }
        long startTime = System.nanoTime();
		deleteNode(listNode6);
		long endTime = System.nanoTime();
        System.out.println("time：" + (endTime - startTime));
        tNode = listNode1;
        while (tNode != null) {
            System.out.print(tNode.val + " ");
            tNode = tNode.next;
        }
    }
}