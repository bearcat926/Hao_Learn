/**
 * 不修改数组找出重复的数字 
 * 给定一个长度为 n+1 的数组nums，数组中所有的数均在 1∼n 的范围内，其中 n≥1。
 * 请找出数组中任意一个重复的数，但不能修改输入的数组。
 */

class Solution3 {

    public static void main(String[] args) {

        int[] numbers = { 3, 1, 5, 2, 2, 0 };
        long startTime = System.nanoTime();
        int num = getDuplicate(numbers);
        long endTime = System.nanoTime();
        System.out.println("time：" + (endTime - startTime));
        System.out.println(num);
    }

    public static int getDuplicate(int[] numbers) {
        int length = numbers.length;
        // 非空判断
        if (length == 0)
            return -1;
        int[] duplicate = new int[length];

        for (int i = 0; i < length; i++) {
            // 数组上的值与当前值相等则重复
            if (duplicate[numbers[i]] == numbers[i])
                return numbers[i];
            // 不相等则赋值
            duplicate[numbers[i]] = numbers[i];
        }
        return -1;
    }

}