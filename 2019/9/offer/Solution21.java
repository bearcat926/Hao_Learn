/*
 * 调整数组顺序使奇数位于偶数前面
 * 输入一个整数数组，实现一个函数来调整该数组中数字的顺序。
 * 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分。
 */

class Solution21 {
    public static void reOrderArray(int [] array) {
        if (array != null && array.length != 0) {
            int temp,i = 0,j = array.length - 1;
            while (i < j) {
                // 直到是偶数
                while (i < j && isOdd(array[i])) i++;
                // 直到是奇数
                while (i < j && !isOdd(array[j])) j--;
                if(i < j){
                    temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }        
        }
    }
    
    public static boolean isOdd(int number) {
        return (number & 1) == 1;
    }
}
