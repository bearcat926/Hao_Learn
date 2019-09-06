import java.util.Arrays;

/**
 * 从尾到头打印链表 输入一个链表的头结点，按照 从尾到头 的顺序返回节点的值。 返回的结果用数组存储。
 */

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
/**
     * ListNode i, j, temp = head;
        
        while(temp.next != null){
            i = temp.next;
            j = i.next;
            i.next = temp;
            temp = j;
        }

        head.next = null;
     */
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
        while (head != null){
            array[i--] = head.val;
            head = head.next;
        }
        return array;
    }
    
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