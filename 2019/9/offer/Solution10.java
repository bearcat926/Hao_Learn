/**
 * 斐波那契数列 
 * 输入一个整数 n ，求斐波那契数列的第 n 项。 
 * 假定从0开始，第0项为0。(n<=39)
 */

public class Solution10 {
	public static int Fibonacci(int n) {
		if (n == 0 || n == 1) {
			return n;
		}

		int fbnNum = 0;
		int fbnNum_1 = 1;
		int fbnNum_2 = 0;

		// 模拟斐波那契数列运算规则
		for (int i = 2; i <= n; i++) {
			// 当前数是前前两个的相加
			fbnNum = fbnNum_1 + fbnNum_2;
			// 相加之后将重新赋值
			fbnNum_2 = fbnNum_1;
			fbnNum_1 = fbnNum;
		}
		return fbnNum;
	}

	public static int FibonacciByRecursion(int n) {
		return (n == 0 || n == 1) ? n : FibonacciByRecursion(n - 1) + FibonacciByRecursion(n - 2);
	}

	public static void main(String[] args) {
		long startTime = System.nanoTime();
		int fbnNum = Fibonacci(5);
		long endTime = System.nanoTime();
		System.out.println("time：" + (endTime - startTime));
		System.out.println(fbnNum);
	}
}