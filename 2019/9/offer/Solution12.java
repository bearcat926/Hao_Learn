/**
 * 矩阵中的路径 
 * 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
 * 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
 * 如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 输入的路径不为空； 所有出现的字符均为大写英文字母；
 */
class Solution12 {
	public static boolean hasPath(char[][] matrix, String str) {
		// 非空检测
		if(matrix == null || matrix.length == 0 || str == null || str == ""){
			return false;
		}

		// 获取目标数组
		char[] src = str.toCharArray();
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[i].length; j++) {
				if (src[0] == matrix[i][j]) {
					if(hasPathCore(matrix, i, j, src, 0)) return true;
				}
			}
		}

		return false;
	}

	public static boolean hasPathCore(char[][] matrix, int i, int j, char[] src, int l) {
		// 成功条件，后一个条件是防止str串中只有一个元素的时候
		if (src.length == l || src.length == 1) {
			return true;
		}

		// 不相同则回溯
		if (matrix[i][j] != src[l]) {
			return false;
		}

		// 利用数组进行移动
		int[] dy = {-1, 0, 1 , 0};
		int[] dx = { 0, 1, 0 ,-1};
		// 声明临时变量为了回溯
		char temp = matrix[i][j];
		// 不能进入重复的格子
		matrix[i][j] = '*';
		// 尝试按上右下左的顺序移动
		for (int z = 0; z < 4 ; z++) {
			int a = i + dy[z];
			int b = j + dx[z];
			if (a >= 0 && a < matrix.length && b >= 0 && b < matrix[a].length ) {				
				if(hasPathCore(matrix, a, b, src, l + 1)) return true;
			}
		}
		// 回溯还原
		matrix[i][j] = temp;
		return false;
	}

	public static void main(String[] args) {
		// char[][] matrix = { { 'C', 'A', 'A' }, { 'A', 'A', 'A'}, { 'B', 'C', 'D'} };
		char[][] matrix = {{'A'}};
		String str = "A";
		long startTime = System.nanoTime();
		boolean flag = hasPath(matrix, str);
		long endTime = System.nanoTime();
		System.out.println("time：" + (endTime - startTime));
		System.out.println(flag);
	}
}