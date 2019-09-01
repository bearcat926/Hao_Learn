import java.util.*;

public class ArrayListFailFast {
    public static void main(String[] args) {
        List<String> list = new ArrayList<String>();
        list.add("one");
        list.add("two");
        list.add("three");
        for (String s : list) {
            if ("two".equals(s)) {
                list.remove(s);
            }
        }
        System.out.println(list);
    }
}