/**
 * 链表中倒数第k个节点
 * 输入一个链表，输出该链表中倒数第k个结点。
 */

class ListNode22 {
     int val;
     ListNode22 next;
     ListNode22(int x) { val = x; }
}

class Solution22 {
    public ListNode22 findKthToTail(ListNode22 pListHead, int k) {
        if (pListHead == null) {
            return null;
        }
        ListNode22 curr = pListHead;
        int length = 0;

        while (curr != null) {
            curr = curr.next;
            length ++;
            
        }

        System.out.println(length);
        if (k > length) {
            return null;
        }  
        
        curr = pListHead;
        /**
         * 倒数第 k 个 ，即从 0 开始计算，第length - k + 1个。
         * 0 1 2 3 4 5
         * length = 6
         * k = 2
         * length - k + 1 = 5
         * 所以需要执行 4 次 curr = curr.next
         * 因为初始复制之后不会 i--，但却执行了一次赋值
         * 因此将(length - k + 1) - 1
         * 之后就在 i > 0 的条件下执行了 length - k 次
         */
        for (int i = length - k; i > 0; i--) {
            curr = curr.next;
        }
        
        return curr;
    }
}