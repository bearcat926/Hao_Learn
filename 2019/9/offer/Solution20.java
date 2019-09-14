/**
 * 表示数值的字符串
 * 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
 * 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
 * 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
 * 
 * 1.先去除行首和行尾空格；
 * 2.行首如果有一个正负号，直接忽略；
 * 3.如果字符串为空或只有一个'.'，则不是一个合法数；
 * 4.循环整个字符串，去掉以下几种情况：
 *   (1) '.'或'e'多于1个;
 *   (2) '.'在'e'后面出现；
 *   (3) 'e'后面或前面为空，或者'e'前面紧跟着'.'；
 *   (4) 'e'后面紧跟着正负号，但正负号后面为空；
 * 5.剩下的情况都合法；
 */
 
 class Solution20 {
    boolean firstPoint = false;
    boolean firstEOre = false;
    int length;
    public static boolean isNumber(String s) {
        if (s == null || s == "") {
            return false;
        }
        char[] sc = s.toCharArray();
        length = sc.length;
        
        return isNumberCore(sc);
    }
    
    public static boolean isNumberCore(char[] sc) {
        // 处理行首和行尾的空格
        if (sc[0] == ' ') sc[0] = '0';

        for (int i = 0; i < length; i++) {
            if(sc[i] >= '0' && sc[i] <= '9');
            else if (sc[i] == 'e' || sc[i] == 'E') { // 1.判断 e Or E
                if(!firstEOre){ // 第一次出现 e Or E
                    // 首位出现
                    if (i == 0) return false; 
                    firstEOre = true;
                } else if(firstEOre) { // 重复出现 e Or E
                    return false;   
                }
                // e Or E是末尾
                if (i + 1 == length) {
                    return false;
                }
                
            } else if (sc[i] == '.') { // 2.判断 '.'
                if (firstEOre) { // '.'在 e Or E之后
                    return false;
                } else if(!firstPoint){ //第一次 '.'
                    // 只有一个点
                    if (length == 1) return false; 
                    firstPoint = true;
                }else if(firstPoint){ //重复 '.'
                    return false;
                }
            } else if (sc[i] == '+' || sc[i] == '-' && i + 1 == length) { // 3.+、- 在末尾
                return false;
            } else { // 其他字符
                return false;
            }
        }
        return true;
    }
}
