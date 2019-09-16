/**
 * 链表中环的入口结点
 * 给定一个链表，若其中包含环，则输出环的入口节点。
 * 若其中不包含环，则输出null。
 */

 
class ListNode23 {
    int val;
    ListNode23 next;
    ListNode23(int x) { val = x; }
}

/**
 * second 只能超过 first 一圈，当 first 走的步数为偶数时可以相遇
 */
class Solution23 {
    public static ListNode23 entryNodeOfLoop(ListNode23 head) {
        ListNode23 first = head;
        ListNode23 second = head;
        while (second != null) {
            first = first.next;
            second = second.next;

            if (second != null) second = second.next;
            else return null;

            if (first == second) break;
        }

        if (first == second) {
            first = head;
            while (first != second) {
                second = second.next;
                first = first.next;
            }
            return first;
        }

        return null;
    }
}