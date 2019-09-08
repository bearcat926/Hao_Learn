/**
 * 旋转数组的最小数字 
 * 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
 * 输入一个升序的数组的一个旋转，输出旋转数组的最小元素。
 * 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
 * 数组可能包含重复项。
 * 注意：数组内所含元素非负，若数组大小为0，请返回-1。
 */
public class Solution11 {

	/**
	 * 原始版本
	 * public int findMin(int[] nums) {
        int length;
		if(nums == null || (length = nums.length ) == 0){
			return -1;
		}
		int left = 0;
		int right = length - 1;
		int mid = (left + right) / 2;

		if(nums[left] >= nums[right]){
			while(left < right){
				// 在某一子数组中
				if(nums[mid] >= nums[mid - 1] && nums[mid] <= nums[mid + 1]){
					// mid 在前子数组中
					if(nums[mid] >= nums[left]){
						left = mid + 1;
					} else { // mid 在后子数组中
						right = mid - 1;
					}
					mid = (left + right) / 2;
				}else if (nums[mid] < nums[mid - 1]){
					return nums[mid];
				}else if (nums[mid] > nums[mid + 1]){
					return nums[mid + 1];
				}
			}
		}else{
			return nums[left];
		}
		return nums[mid];
    }
	 */

	public static int findMin(int[] nums) { // 不能解决{1, 0, 1, 1, 1} 或 {1, 1, 1, 0, 1}问题
		int length;
		if (nums == null || (length = nums.length) == 0) {
			return -1;
		}
		int left = 0;
		int right = length - 1;
		int mid = left; // 防止未旋转的子数组

		while (nums[left] >= nums[right]) {
			if (right - left == 1) { // 当mid节点为最小节点
				mid = right;
				break;
			}
			mid = (left + right) / 2;

			
			if (nums[left] == nums[right] && nums[left] == nums[mid]) {
				return findMinByOrder(nums, left, right);
			}

			// mid 在前子数组中
			if (nums[mid] >= nums[left]) {
				left = mid;
			} else if (nums[mid] <= nums[right]) { // mid 在后子数组中
				right = mid;
			}
		}

		return nums[mid];
	}

	// 当nums[left] == nums[right] && nums[left] == nums[mid]时，可以在left, right之间查找，因为当前left和right的值依然是初始值
	public static int findMinByOrder(int[] nums, int left, int right) {
		int result = nums[left];
		for (int i = left + 1; i <= right; i++) {
			if (result > nums[i]) result = nums[i];
		}
		return result;
	}

	public static void main(String[] args) {
		int[] nums = { 1, 1, 1, 0, 1 };
		long startTime = System.nanoTime();
		int min = findMin(nums);
		long endTime = System.nanoTime();
		System.out.println("time：" + (endTime - startTime));
		System.out.println(min);
	}
}