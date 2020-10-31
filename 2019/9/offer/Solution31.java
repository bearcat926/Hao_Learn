/**
 * 栈的压入、弹出序列
 * 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
 * 假设压入栈的所有数字均不相等。
 * 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
 * 注意：若两个序列长度不等则视为并不是一个栈的压入、弹出序列。若两个序列都为空，则视为是一个栈的压入、弹出序列。
 */

class Solution31 {
    public boolean isPopOrder(int [] pushV,int [] popV) {
        if(pushV == null && popV == null) return false;
		if(pushV == null || popV == null || pushV.length != popV.length) return false;
		
		MyStack31 s = new MyStack31();

		int i = 0;
		for (int a : pushV){
			s.pushToTop(a);
			while(!s.isEmpty() && s.peekFromTop() == popV[i]){
				i++;
				s.popFromTop();
			}
		}

		return s.isEmpty();
    }
}

class MyStack31 {

	LinkedNode31 top;
	int size = 0;

	public void pushToTop(int x) {
		LinkedNode31 newTop = new LinkedNode31(x, null, top);
		// 空栈添加不需要更改
		if (size != 0) {
			top.pre = newTop;
		}
		top = newTop;
		size++;
	}

	public int popFromTop() {
		int val = top.val;
		top = top.next;
		// 只剩栈顶元素时不需要进行更改
		if (size != 1) {
			top.pre = null;
		}
		size--;
		return val;
	}

	public int peekFromTop() {
		return top.val;
	}

	public int size() {
		return size;
	}

	public boolean isEmpty() {
		return size == 0 ? true : false;
	}
}

class LinkedNode31 {
	int val;
	LinkedNode31 pre;
	LinkedNode31 next;

	public LinkedNode31() {

	}

	public LinkedNode31(int val, LinkedNode31 pre, LinkedNode31 next) {
		this.val = val;
		this.pre = pre;
		this.next = next;
	}
}