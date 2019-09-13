/**
 * 正则表达式匹配
 * 请实现一个函数用来匹配包括'.'和'*'的正则表达式。
 * 模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
 * 在本题中，匹配是指字符串的所有字符匹配整个模式。
 * 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配。
 */
class Solution19 {

    int sLength, pLength;
    char[] sc, pc;
    boolean[][] f ;
	
    public boolean isMatch(String s, String p) {
	// 非空检测
	if (s == null || p == null) {
	    return false;
	}
	
	sc = s.toCharArray();
	pc = p.toCharArray();
	sLength = sc.length;
	pLength = pc.length;
	
	// pLength + 1 为了防止 y + 1 时出现空指针的情况
	f = new boolean[sLength][pLength + 1];
	return matchCoreByDP(0, 0);  
    }

    public boolean matchCoreByDP(int x, int y) {
        // 两个长度都相同则返回；也可以防止 `.` or `.*` 模式对空字符串的不匹配情况
	if (y == pLength) {
	    return x == sLength;
	}      
	
	// 对当前需要检测的字符进行判断，分为 字符是否相等 和 当前的匹配模式是否是 `.`
	boolean currMatch = x < sLength && (sc[x] == pc[y] || pc[y] == '.');

	// 判断下一个匹配模式是否是 '*'
	if (y + 1 < pLength && pc[y + 1] == '*') {
	    // 判断 0次 和 1次 两种情况。其中，判断 1次 时，要检测对当前字符的判断结果
	    // 0次：模式字符跳到 '*' 后，y = y + 2
	    // 1次：尝试使用 '*' 匹配下一字符，x = x + 1
	    return matchCoreByDP(x, y + 2) || currMatch && matchCoreByDP(x + 1, y);
	} else {
	    // 检测的对第一个字符的判断结果.通过则继续下一字符的判断
	    return currMatch  && matchCoreByDP(x + 1, y + 1);
	}

    }



    public static void main(String[] args) {
        String s = "aa";
        String p = "a*";
        long startTime = System.nanoTime();
	boolean flag = isMatch(s, p);
	long endTime = System.nanoTime();
        System.out.println("time：" + (endTime - startTime));
        System.out.println(flag);
    }
}
