class MyQueue {
	MyStack myStack1, myStack2;
	boolean stack1IsStack = true;

	/** Initialize your data structure here. */
	public MyQueue() {
		myStack1 = new MyStack();
		myStack2 = new MyStack();
	}

	/** Push element x to the back of queue. */
	public void push(int x) {
		if (!stack1IsStack) { // 说明stack2是FIFO，需要将stack2中的数据存入stack1，再插入，之后改变stack1IsStack值
			while (!myStack2.isEmpty()) {
				myStack1.pushToTop(myStack2.popFromTop());
			}
			stack1IsStack = true;
		} // 说明stack1是FILO，插入stack1可以做到LILO
		myStack1.pushToTop(x);
	}

	/** Removes the element from in front of queue and returns that element. */
	public int pop() {
		// 非空判断
		if (!empty()) {
			// 说明stack1是FILO，需要将stack1中的数据存入stack2，再弹出stack2的top，之后改变stack1IsStack值
			if (stack1IsStack) {
				while (!myStack1.isEmpty()) {
					myStack2.pushToTop(myStack1.popFromTop());
				}
				stack1IsStack = false;
			} // 说明stack2是FIFO，弹出即可
			return myStack2.popFromTop();
		}
		return 0;
	}

	/** Get the front element. */
	public int peek() {
		// 非空判断
		if (!empty()) {
			// 说明stack1是FILO，需要将stack1中的数据存入stack2，再查找stack2的top，之后改变stack1IsStack值
			if (stack1IsStack) {
				while (!myStack1.isEmpty()) {
					myStack2.pushToTop(myStack1.popFromTop());
				}
				stack1IsStack = false;
			} // 说明stack2是FIFO，查找即可
			return myStack2.peekFromTop();
		}
		return 0;
	}

	/** Returns whether the queue is empty. */
	public boolean empty() {
		return myStack1.isEmpty() && myStack2.isEmpty();
	}
}

class MyStack {

	LinkedNode top;
	int size = 0;

	public void pushToTop(int x) {
		LinkedNode newTop = new LinkedNode(x, null, top);
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

class LinkedNode {
	int val;
	LinkedNode pre;
	LinkedNode next;

	public LinkedNode() {

	}

	public LinkedNode(int val, LinkedNode pre, LinkedNode next) {
		this.val = val;
		this.pre = pre;
		this.next = next;
	}
}

public class Solution9 {

}
