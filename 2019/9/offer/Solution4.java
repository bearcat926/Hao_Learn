/**
 * 二维数组中的查找 
 * 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
 * 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
 */

class Solution4 {

    public static void main(String[] args) {

        int[][] array = { { 1, 2, 8, 9 }, { 2, 4, 9, 12 }, { 4, 7, 10, 13 }, { 6, 8, 11, 15 } };
        int target = 7;
        long startTime = System.nanoTime();
        boolean flag = searchArray(array, target);
        long endTime = System.nanoTime();
        System.out.println("time：" + (endTime - startTime));
        System.out.println(flag);
    }

    public static boolean searchArray(int[][] array, int target) {
        int high = array.length;
        // 非空检测
        if (array == null || high == 0 || (array.length == 1 && array[0].length == 0))
            return false;
        int length = array[0].length;
        int i = high - 1;
        int j = 0;

        // 从左下角开始查找，溢出边界则停止
        while (i >= 0 && j < length) {
            // 值小于target，则向右查找
            if (array[i][j] < target){
                j++;
            } else if (array[i][j] > target) { // 值大于target，则向上查找
                i--;
            } else { // 值等于target，则返回
                return true;
            }
        }
        return false;
    }
}