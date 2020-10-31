
/**
 * 替换空格 
 * 请实现一个函数，把字符串中的每个空格替换成"%20"。 
 * 你可以假定输入字符串的长度最大是1000。 
 * 注意输出字符串的长度可能大于1000。
 */

class Solution5 {
    public static String replaceSpaces(StringBuffer str) {
        char[] charArray = str.toString().toCharArray();
        int length = charArray.length;
        int num = 0;
        // 空格计数
        for (int i = 0; i < length; i++) {
            if (charArray[i] == ' ') {
                num++;
            }
        }
        // 临时数组
        char[] temp = new char[length + num * 2];
        for (int i = 0, j = 0; i < length; i++) {
            // 空格赋值
            if (charArray[i] == ' ') {
                temp[j++] = '%';
                temp[j++] = '2';
                temp[j++] = '0';
            } else {
                temp[j++] = charArray[i];
            }
        }
        return new String(temp);
    }

    public static String replaceSpaces1(StringBuffer str) {
        char[] charArray = str.toString().toCharArray();
        int length = charArray.length;
        // 清空StringBuffer
        str = new StringBuffer();
        for (int i = 0; i < length; i++) {
            // 空格赋值
            if (charArray[i] == ' ') {
                str.append("%20");
            } else {
                str.append(charArray[i]);
            }
        }
        return str.toString();
    }

    // private static Object resizeArray(Object oldArray, int newSize) {
    //     // 获取旧长度
    //     int oldSize = java.lang.reflect.Array.getLength(oldArray);
    //     Class elementType = oldArray.getClass().getComponentType();

    //     Object newArray = java.lang.reflect.Array.newInstance(elementType, newSize);
    //     int preserveLength = Math.min(oldSize, newSize);
    //     if (preserveLength > 0)
    //         System.arraycopy(oldArray, 0, newArray, 0, preserveLength);
    //     return newArray;
    // }

    public static String replaceSpaces2(StringBuffer str) {
        char[] charArray = str.toString().toCharArray();
        int length = charArray.length;
        int newLength = length;
        // 空格计数
        for (int i = 0; i < length; i++) {
            if (charArray[i] == ' ') {
                newLength += 2;
            }
        }
        // 修改数组长度
        // charArray = (char[]) resizeArray(charArray, newLength);
        char[] temp = new char[newLength];
        System.arraycopy(charArray, 0, temp, 0, length);
        
        for (int i = newLength - 1, j = length - 1; j >= 0; j--) {
            // 空格赋值
            if (temp[j] == ' ') {
                temp[i--] = '0';
                temp[i--] = '2';
                temp[i--] = '%';
            } else {
                temp[i--] = temp[j];
            }
        }
        return new String(temp);
    }

    public static void main(String[] args) {

        StringBuffer inputStr = new StringBuffer("We are happy.");
        long startTime = System.nanoTime();
        String str = replaceSpaces2(inputStr);
        long endTime = System.nanoTime();
        System.out.println("time：" + (endTime - startTime));
        System.out.println(str);
    }
}