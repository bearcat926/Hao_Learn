/**
 * 二进制中1的个数 
 * 输入一个32位整数，输出该数二进制表示中1的个数。
 */
class Solution15 {
    public static int NumberOf1(int n) {
        int count = 0;
        while (n != 0) {
            n = n & (n - 1);
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
		long startTime = System.nanoTime();
		int result = NumberOf1(-2);
		long endTime = System.nanoTime();
		System.out.println("time：" + (endTime - startTime));
		System.out.println(result);
	}
}
/*
n   9 1001
n-1 8 1000
&     1000
n   8 1000
n-1 7 0111
&     0000  

当末尾为 01 时，n-1 的末尾为 00，& 操作会减少一位1
当末尾为 10（可以多个0） 时，n-1 的末尾为01（相应位数的多个1），因此 & 操作之后，末尾会全部变成0，因此也会减少一位1
*/