/**
 * 数组中出现次数超过一半的数字
 * 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
 * 假设数组非空，并且一定存在满足条件的数字。
 * 思考题：
 * 假设要求只能使用 O(n) 的时间和额外 O(1) 的空间，该怎么做呢？
 */

class Solution41 {

    public static int moreThanHalfNum_Solution(int[] nums) {
		if(nums == null || nums.length == 0) return 0; 
		int n = nums[0];
		int p = 1;
		for(int i = 1; i < nums.length; ++i){
			if(n != nums[i]) --p;
			else ++p;
			// 说明当前数字出现的概率等于一半
			if(p == 0) {
				// 重新选择数字
			    n = nums[i];
			    p = 1;
			}
		}

		// 验证
		p = 0;
		for(int i = 0; i < nums.length; ++i)
			if(n == nums[i]) 
				++p;

		if(p <= nums.length / 2) System.out.println("不存在");

		return n;
	}
	
	public static void main(String[] args) {
		int[] nums = {1,2,1,1,3};
		System.out.println(moreThanHalfNum_Solution(nums));
	}
}