import java.util.*;

/**
 * 数字排列 
 * 输入一组数字（可能包含重复数字），输出其所有的排列方式。
 * [
		[1,2,3],
		[1,3,2],
		[2,1,3],
		[2,3,1],
		[3,1,2],
		[3,2,1]
	]

	暴力搜索，按顺序填位置，如果后一个数与前一个数字重复，则它只能放在后一个数字的后面
	原因是放前面的话，在前面的数字必定尝试过，也因此重复的数字位置要相对固定，可通过排序固定
 */

class Solution40 {
	static List<List<Integer>> list = new ArrayList<>();

    public static List<List<Integer>> permutation(int[] nums) {
        quickSort(nums, 0, nums.length - 1);
        backtrack(new ArrayList<>(), nums, new boolean[nums.length]);
        return list;
    }

    private static void backtrack(List<Integer> tempList, int [] nums, boolean [] used){
        if(tempList.size() == nums.length){
            list.add(new ArrayList<>(tempList));
        } else{
            for(int i = 0; i < nums.length; i++){
				// used[i] == true -> 说明当前槽位槽位被占
				// nums[i] == nums[i-1] && !used[i - 1] -> 当前位置（非首位）与之前位置，且之前槽位未使用则跳过
                if(used[i] || i > 0 && nums[i] == nums[i-1] && !used[i - 1]) continue;
                used[i] = true; 
                tempList.add(nums[i]);
                backtrack(tempList, nums, used);
                used[i] = false; 
                tempList.remove(tempList.size() - 1);
            }
        }
    }
	
	public static void main(String[] args) {
		int[] nums = {1, 2, 1};
		permutation(nums);
		
		list.forEach(item -> {
			((Iterable) item).forEach(item1 -> System.out.print(item1 + " "));
			System.out.println();
		});
	}
	
	public static void quickSort(int[] nums, int start, int end){
		if(start > end) return; 

		int p = partition(nums, start,end);

		quickSort(nums, start, p - 1);
		quickSort(nums, p + 1, end);
	}

	public static int partition(int[] nums, int start, int end){
		int p = nums[start];

		while(start < end){
			while(start < end && nums[end] >= p) --end;
			nums[start] = nums[end]; 
			while(start < end && nums[start] <= p) ++start;
			nums[end] = nums[start];
		}
		nums[start] = p;
		return start;
	}
}