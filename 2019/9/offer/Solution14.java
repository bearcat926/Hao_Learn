/**
 * 剪绳子 
 * 给你一根长度为 n 绳子，请把绳子剪成 m 段（m、n 都是整数，2≤n≤58 并且 m≥2）。
 * 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]k[1] … k[m] 可能的最大乘积是多少？
 * 例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到最大的乘积18。
 */
class Solution14 {
    public static int maxProductAfterCutting(int length) {
        // 处理 length = {2, 3}的情况
        if (length <= 3) return 1 * (length - 1);

        int result = 1;
        // length小于等于4时需要特殊处理，否则只需要剪去更多的3
        while (length > 4){
            length = length - 3;
            result *= 3;
        }
        // length为4时，可以拆分成2*2
        if(length == 4){
            result *= 4;
        }else{  // length为2，3时，直接×length
            result *= length;
        }

        return result;
    }

    public static void main(String[] args) {
		long startTime = System.nanoTime();
		int result = maxProductAfterCutting(8);
		long endTime = System.nanoTime();
		System.out.println("time：" + (endTime - startTime));
		System.out.println(result);
	}
}