/**
 * 从尾到头打印链表 
 * 输入一个链表的头结点，按照 从尾到头 的顺序返回节点的值。 
 * 返回的结果用数组存储。
 */

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution6 {
    public static int[] printListReversingly(ListNode head) {
        ListNode temp = head;
        int length = 0;
        // 计算长度
        while (temp != null) {
            length++;
            temp = temp.next;
        }
        int i = length - 1;
        int[] array = new int[length];
        // 数组赋值
        while (head != null) {
            array[i--] = head.val;
            head = head.next;
        }
        return array;
    }

    /**
     * 链表反转：需要前中后三个临时节点，先存储后节点，在对当前节点的下一节点赋值为前节点，之后将前中节点依次置后
     * while (curr.next != null) {
            next = curr.next;
            curr.next = pre; 
            pre = curr; 
            curr = next; 
        }
     * 
     */
    public static void main(String[] args) {
        ListNode head = new ListNode(2);
        head.next = new ListNode(3);
        head.next.next = new ListNode(5);
        long startTime = System.nanoTime();
        int[] array = printListReversingly(head);
        long endTime = System.nanoTime();
        System.out.println("time：" + (endTime - startTime));
        for (int i : array) {
            System.out.println(i);
        }
    }
}