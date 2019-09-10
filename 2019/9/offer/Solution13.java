class Solution13 {
	public static int movingCount(int threshold, int rows, int cols) {
		// 非空验证
		if (rows == 0 || cols == 0)
			return 0;
		// 初始值为false
		/**
		 * 按照 x * cols + y 的方式检查路径
		 * rows/cols           
		 *      0 1 2 3 4
		 *    0 1 2 3 4 5
		 *    1 6 7 8 9 10
		 *    2 ....
		 *    3
		 *    4
 		 */
		boolean[] checkDuplicate = new boolean[rows * cols];
		return getCore(threshold, rows, cols, 0, 0, 0, checkDuplicate);
	}

	public static int getCore(int threshold, int rows, int cols, int x, int y, int input, boolean[] checkDuplicate) {
		// 检查未通过返回则返回input，否则+1
		if (!check(threshold, cols, x, y, checkDuplicate)) {
			return input;
		} else {
			input++;
		}

		// 上右下左 移动
		int[] dx = { -1, 0, 1, 0 };
		int[] dy = { 0, 1, 0, -1 };
		for (int z = 0; z < 4; z++) {
			int a = x + dx[z];
			int b = y + dy[z];
			// 边缘检测
			if (a >= 0 && a < rows && b >= 0 && b < cols)
				input = getCore(threshold, rows, cols, a, b, input, checkDuplicate);
		}

		return input;
	}

	public static boolean check(int threshold, int cols, int x, int y, boolean[] checkDuplicate) {
		// 值不为false则已进入
		if (checkDuplicate[x * cols + y] == true) {
			return false;
		}
		checkDuplicate[x * cols + y] = true;
		// 数位运算
		if (x > 9) {
			x = x / 10 + x % 10;
		}
		if (y > 9) {
			y = y / 10 + y % 10;
		}
		return (x + y) <= threshold;
	}

	public static void main(String[] args) {
		long startTime = System.nanoTime();
		int count = movingCount(7, 4, 5);
		long endTime = System.nanoTime();
		System.out.println("time：" + (endTime - startTime));
		System.out.println(count);
	}
}