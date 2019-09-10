class Solution13 {
    public int movingCount(int threshold, int rows, int cols)
    {
        return getCore(threshold, rows, cols, 0, 0, 0);
    }

    public int getCore(int threshold, int rows, int cols, int x, int y, int input) {
        // ÉÏÓÒÏÂ×ó ÒÆ¶¯
        int[] dx = {-1, 0, 1, 0};
        int[] dy = { 0, 1, 0,-1};
        for (int z = 0; z < 4 ; z++) {
            if(check(int threshold, int x, int y)){
                input ++;
            }
        }
    }
    
    public boolean check(int threshold, int x, int y){
        if (x > 9) {
            x = x / 10 + x % 10;
        }
        if (y > 9) {
            y = y / 10 + y % 10;
        }
        return (x + y) <= threshold;
    }
}