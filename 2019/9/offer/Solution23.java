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
 * l1 = x + y;
 * l2 = 2l1 = 2*(x + y) = x + n*(y + z) + y;
 * so
 * x + y = n*(y + z)
 * x = (n - 1)*(y + z) + z
 * 根据这个等式相遇之后，若first从节点a单步移动到节点b所需的步数，就等于second从节点c单步移动到节点b所需的步数(可能会转n-1圈)
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