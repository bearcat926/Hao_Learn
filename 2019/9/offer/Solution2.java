/**
 * 数组中重复的数字 
 * 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
 * 数组中某些数字是重复的，但不知道有几个数字是重复的。
 * 也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
 * 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
 */
class Solution2 {

    public static void main(String[] args) {

        int[] nums = { 4, 5, 1, 3, 4, 1, 2 };
        int[] duplicate = new int[1];
        long startTime = System.nanoTime();
        boolean flag = duplicate(nums, nums.length, duplicate);
        long endTime = System.nanoTime();
        System.out.println("time：" + (endTime - startTime));
        System.out.println((flag == false ? -1 : duplicate[0]));
    }

    // 交换方法
    public static void swap(int[] nums, int src, int dest) {
        int temp;
        temp = nums[src];
        nums[src] = nums[dest];
        nums[dest] = temp;
    }

    public static boolean duplicate(int numbers[], int length, int[] duplication) {
        if (length == 0)
            return false;
        // 边缘检测
        for (int num : numbers)
            if (num < 0 || num > length)
                return false;
        for (int i = 0; i < length; i++) {
            // 将值放置到对应的槽位上
            // nums[i] != i -> 相应位置无需处理
            //
            while (numbers[i] != i && numbers[i] != numbers[numbers[i]])
                swap(numbers, i, numbers[i]);
            if (numbers[i] != i && numbers[i] == numbers[numbers[i]]) {
                duplication[0] = numbers[i];
                return true;
            }

        }
        // 没有重复的数
        return false;
    }

}
