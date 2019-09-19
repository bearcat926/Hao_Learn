import java.util.Arrays;

/**
 * 顺时针打印矩阵
 * 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
 */

 /**
  * 设置动态限制：当遇到转向时，将行动的相反方向长度减一
  */
class Solution29 {
    public static int[] printMatrix(int[][] matrix) {

		if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return new int[0];

		int yMax = matrix.length;
		int xMax = matrix[0].length;
		
		int[] result = new int[yMax * xMax];

		// 上右下左
		int[] dy = {-1, 0, 1, 0};
		int[] dx = { 0, 1, 0,-1};

		boolean[][] check = new boolean[yMax][xMax];
		int x = 0, y = 0;
		int i = 1;

		for (int j = 0; j < yMax * xMax; j++){
			result[j] = matrix[y][x];
			// 设置进入判断
			check[y][x] = true;

			// 使用回溯思想，加上预先值之后，判断该操作是否可行
			int a = y + dy[i];
			int b = x + dx[i];
			// 预先值越界，或已经进入过
			if(a < 0 || a >= yMax || b < 0 || b >= xMax || check[a][b]){
				// 转向
				i = (i + 1) % 4;
				a = y + dy[i];
				b = x + dx[i];
			}
			y = a;
			x = b;
		}

		return result;
	}

	public static void main(String[] args) {
		int[][] array = {
			{1, 2, 3, 4},
			{5, 6, 7, 8},
			{9,10,11,12}
		};
		
		Arrays.stream(printMatrix(array)).forEach(item -> System.out.print(item + " "));;
	}
}