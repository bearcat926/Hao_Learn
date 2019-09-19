/**
 * 包含min函数的栈
 * 设计一个支持push，pop，top等操作并且可以在O(1)时间内检索出最小元素的堆栈。
 * push(x)–将元素x插入栈中
 * pop()–移除栈顶元素
 * top()–得到栈顶元素
 * getMin()–得到栈中最小元素
 */

class LinkedNode30 {
	int val;
	LinkedNode30 pre;
	LinkedNode30 next;

	public LinkedNode30() {

	}

	public LinkedNode30(int val, LinkedNode30 pre, LinkedNode30 next) {
		this.val = val;
		this.pre = pre;
		this.next = next;
	}
}

class MinStack {

	LinkedNode30 top;
	LinkedNode30 min;	
	int size = 0;

	public int top() {
		return top.val;
	}

	public int getMin() {
		return min.val;
	}

	public int size() {
		return size;
	}

	public boolean isEmpty() {
		return size == 0 ? true : false;
	}

	public void push(int x) {
		LinkedNode30 newTop = new LinkedNode30(x, null, top);
		// 空栈添加不需要更改
		if (size != 0) {
			top.pre = newTop;
		}
		top = newTop;
		size++;

		if(min == null){
			min = new LinkedNode30(x, null, null);
		}else if(min.val >= x){
			LinkedNode30 newMin = new LinkedNode30(x, null, min);
			min.pre = newMin;
			min = newMin;
		}else{
			LinkedNode30 curr = min;
			while(curr != null){
				if(curr.val < x){
					curr = curr.next;
				}else{
					LinkedNode30 newMin = new LinkedNode30(x, curr.pre, curr);
					curr.pre.next = newMin;
					curr.pre = newMin;
				}
			}
		}
	}

	public int pop() {
		int val = top.val;
		top = top.next;
		// 只剩栈顶元素时不需要进行更改
		if (size != 1) {
			top.pre = null;
		}
		size--;

		if(size == 0){
			min = null;
		}else if(min.val == val){
			min = min.next;
			min.pre = null;
		}else{
			LinkedNode30 curr = min;
			while(curr != null){
				if(curr.val == val){
					curr.pre.next = curr.next;
					curr.next.pre = curr.pre;
					break;
				}else{
					curr = curr.next;
				}
			}
		}

		return val;
	}
}

/**
 * 上一种方式会出现Memory Limit Exceeded。
 * 
 * 更改为使用单调栈
 * 1. 向栈中压入一个数时，如果该数 <= 单调栈的栈顶元素，则将该数同时压入单调栈中；否则，不压入
 * 2. 从栈中弹出一个数时，如果该数等于单调栈的栈顶元素，则同时将单调栈的栈顶元素弹出。
 * 单调栈由于其具有单调性，所以它的栈顶元素，就是当前栈中的最小数。
 */

class MyStack30 {

	LinkedNode30 top;
	int size = 0;

	public void pushToTop(int x) {
		LinkedNode30 newTop = new LinkedNode30(x, null, top);
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

class MinStack2 {

    MyStack30 top = new MyStack30();
    MyStack30 min = new MyStack30();
    int size = 0;

	public void push(int x) {
		top.pushToTop(x);
		if(!min.isEmpty()){
    		if(min.peekFromTop() >= x){
    		    min.pushToTop(x);
    		}
		}else{
		    min.pushToTop(x);
		}
	}

	public int pop() {
		int val = top.popFromTop();
	    if(min.peekFromTop() == val){
		    min.popFromTop();
		}
		return val;
	}

	public int top() {
		return top.peekFromTop();
	}

	public int getMin() {
		return min.peekFromTop();
	}
}

class Solution30 {
	public static void main(String[] args) {

		MinStack obj = new MinStack();
		obj.push(2);
		obj.push(2);
		obj.pop();
		obj.push(7);
		
		// int param_3 = obj.top();
		// int param_4 = obj.getMin();

	}
}