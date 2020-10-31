/**
 * 数值的整数次方
 * 实现函数double Power(double base, int exponent)，求base的 exponent次方。
 * 不得使用库函数，同时不需要考虑大数问题。
 */
class Solution16 {
    public static double Power(double base, int exponent) {
        // 处理返回本身的情况
        if (base == 1 || base == 0 || exponent == 1) return base;

        // 处理0次幂的情况
        if (exponent == 0) return 1;

        // 处理负数
        if (exponent < 0){
            exponent = -exponent;
            return 1 / handle(base, exponent);
        }
        
        return handle(base, exponent);
    }

    public static double handle(double base, int exponent) {
        // 处理1次幂的情况
        if (exponent == 1) return base;

        if (judge2N(base)) {
            return (long) base << (long)(base * exponent / 2);
        } 

        if (exponent % 2 == 0) {
            exponent = exponent / 2;
            base = handle(base, exponent) * handle(base, exponent);
        } else {
            exponent = (exponent - 1) / 2;
            double temp = base;
            base = handle(base, exponent) * handle(base, exponent);
            base *= temp;
        }
      
        return base;
    }

    // 判断是否是2的n次方
    public static boolean judge2N(double base){
        while(base % 2 == 0) 
            base /= base;
            if (base == 2) 
                return true;

        return false;
	}
	
	// 可以使用快速幂

    public static void main(String[] args) {
        long startTime = System.nanoTime();
		double result = Power(8, 7);
		long endTime = System.nanoTime();
		System.out.println("time：" + (endTime - startTime));
		System.out.println(result);
    }
}