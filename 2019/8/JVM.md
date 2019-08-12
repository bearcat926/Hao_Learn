![JVM1](E:\git_repo\Hao_Learn\2019\8\img\JVM1.png)
new 出来的所有对象都放在堆里面

每个线程对应一个栈

一个方法对应一块栈帧内存区域，即栈帧也叫方法帧

栈帧：

局部变量表，操作数栈，动态链接，方法出口

```
用法: javap <options> <classes>
其中, 可能的选项包括:
  -help  --help  -?        输出此用法消息
  -version                 版本信息
  -v  -verbose             输出附加信息
  -l                       输出行号和本地变量表
  -public                  仅显示公共类和成员
  -protected               显示受保护的/公共类和成员
  -package                 显示程序包/受保护的/公共类
                           和成员 (默认)
  -p  -private             显示所有类和成员
  -c                       对代码进行反汇编
  -s                       输出内部类型签名
  -sysinfo                 显示正在处理的类的
                           系统信息 (路径, 大小, 日期, MD5 散列)
  -constants               显示最终常量
  -classpath <path>        指定查找用户类文件的位置
  -cp <path>               指定查找用户类文件的位置
  -bootclasspath <path>    覆盖引导类文件的位置
```

```Java
package hao.jvm;

/**
 * Created by hao hao on 2019/8/9 0009.
 */
public class JavapDemo {

    public static final Integer CONST = 666;

    public int compute(){
        int a = 1;
        int b = 2;
        int c = (a + b) * 10;
        return c;
    }

    public static void main(String[] args){
        JavapDemo javapDemo = new JavapDemo();
        javapDemo.compute();
    }

}

```
在class文件目录下调用`javap -c JavapDemo.class > JavapDemo.txt`，之后打开JavapDemo.txt：

```
Compiled from "JavapDemo.java"
public class hao.jvm.JavapDemo {
  public static final java.lang.Integer CONST;

  public static final java.lang.Object object;

  public hao.jvm.JavapDemo();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public int compute();
    Code:
       0: iconst_1
       1: istore_1
       2: iconst_2
       3: istore_2
       4: iload_1
       5: iload_2
       6: iadd
       7: bipush        10
       9: imul
      10: istore_3
      11: iload_3
      12: ireturn

  public static void main(java.lang.String[]);
    Code:
       0: new           #2                  // class hao/jvm/JavapDemo
       3: dup
       4: invokespecial #3                  // Method "<init>":()V
       7: astore_1
       8: aload_1
       9: invokevirtual #4                  // Method compute:()I
      12: pop
      13: new           #2                  // class hao/jvm/JavapDemo
      16: dup
      17: invokespecial #3                  // Method "<init>":()V
      20: astore_2
      21: aload_2
      22: invokevirtual #4                  // Method compute:()I
      25: pop
      26: return

  static {};
    Code:
       0: sipush        666
       3: invokestatic  #5                  // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
       6: putstatic     #6                  // Field CONST:Ljava/lang/Integer;
       9: new           #7                  // class java/lang/Object
      12: dup
      13: invokespecial #1                  // Method java/lang/Object."<init>":()V
      16: putstatic     #8                  // Field object:Ljava/lang/Object;
      19: return
}

```

```
Classfile /E:/git_repo/jvm/JavapDemo.class
  Last modified 2019-8-9; size 644 bytes
  MD5 checksum d20d2c0df8d908d026bdd41913850efa
  Compiled from "JavapDemo.java"
public class hao.jvm.JavapDemo
  minor version: 0
  major version: 52
  flags: ACC_PUBLIC, ACC_SUPER
Constant pool:
   #1 = Methodref          #7.#24         // java/lang/Object."<init>":()V
   #2 = Class              #25            // hao/jvm/JavapDemo
   #3 = Methodref          #2.#24         // hao/jvm/JavapDemo."<init>":()V
   #4 = Methodref          #2.#26         // hao/jvm/JavapDemo.compute:()I
   #5 = Methodref          #27.#28        // java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
   #6 = Fieldref           #2.#29         // hao/jvm/JavapDemo.CONST:Ljava/lang/Integer;
   #7 = Class              #30            // java/lang/Object
   #8 = Fieldref           #2.#31         // hao/jvm/JavapDemo.object:Ljava/lang/Object;
   #9 = Utf8               CONST
  #10 = Utf8               Ljava/lang/Integer;
  #11 = Utf8               object
  #12 = Utf8               Ljava/lang/Object;
  #13 = Utf8               <init>
  #14 = Utf8               ()V
  #15 = Utf8               Code
  #16 = Utf8               LineNumberTable
  #17 = Utf8               compute
  #18 = Utf8               ()I
  #19 = Utf8               main
  #20 = Utf8               ([Ljava/lang/String;)V
  #21 = Utf8               <clinit>
  #22 = Utf8               SourceFile
  #23 = Utf8               JavapDemo.java
  #24 = NameAndType        #13:#14        // "<init>":()V
  #25 = Utf8               hao/jvm/JavapDemo
  #26 = NameAndType        #17:#18        // compute:()I
  #27 = Class              #32            // java/lang/Integer
  #28 = NameAndType        #33:#34        // valueOf:(I)Ljava/lang/Integer;
  #29 = NameAndType        #9:#10         // CONST:Ljava/lang/Integer;
  #30 = Utf8               java/lang/Object
  #31 = NameAndType        #11:#12        // object:Ljava/lang/Object;
  #32 = Utf8               java/lang/Integer
  #33 = Utf8               valueOf
  #34 = Utf8               (I)Ljava/lang/Integer;
{
  public static final java.lang.Integer CONST;
    descriptor: Ljava/lang/Integer;
    flags: ACC_PUBLIC, ACC_STATIC, ACC_FINAL

  public static final java.lang.Object object;
    descriptor: Ljava/lang/Object;
    flags: ACC_PUBLIC, ACC_STATIC, ACC_FINAL

  public hao.jvm.JavapDemo();
    descriptor: ()V
    flags: ACC_PUBLIC
    Code:
      stack=1, locals=1, args_size=1
         0: aload_0
         1: invokespecial #1                  // Method java/lang/Object."<init>":()V
         4: return
      LineNumberTable:
        line 6: 0

  public int compute();
    descriptor: ()I
    flags: ACC_PUBLIC
    Code:
      stack=2, locals=4, args_size=1
         0: iconst_1
         1: istore_1
         2: iconst_2
         3: istore_2
         4: iload_1
         5: iload_2
         6: iadd
         7: bipush        10
         9: imul
        10: istore_3
        11: iload_3
        12: ireturn
      LineNumberTable:
        line 12: 0
        line 13: 2
        line 14: 4
        line 15: 11

  public static void main(java.lang.String[]);
    descriptor: ([Ljava/lang/String;)V
    flags: ACC_PUBLIC, ACC_STATIC
    Code:
      stack=2, locals=3, args_size=1
         0: new           #2                  // class hao/jvm/JavapDemo
         3: dup
         4: invokespecial #3                  // Method "<init>":()V
         7: astore_1
         8: aload_1
         9: invokevirtual #4                  // Method compute:()I
        12: pop
        13: new           #2                  // class hao/jvm/JavapDemo
        16: dup
        17: invokespecial #3                  // Method "<init>":()V
        20: astore_2
        21: aload_2
        22: invokevirtual #4                  // Method compute:()I
        25: pop
        26: return
      LineNumberTable:
        line 19: 0
        line 20: 8
        line 21: 13
        line 22: 21
        line 23: 26

  static {};
    descriptor: ()V
    flags: ACC_STATIC
    Code:
      stack=2, locals=0, args_size=0
         0: sipush        666
         3: invokestatic  #5                  // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
         6: putstatic     #6                  // Field CONST:Ljava/lang/Integer;
         9: new           #7                  // class java/lang/Object
        12: dup
        13: invokespecial #1                  // Method java/lang/Object."<init>":()V
        16: putstatic     #8                  // Field object:Ljava/lang/Object;
        19: return
      LineNumberTable:
        line 8: 0
        line 9: 9
}
SourceFile: "JavapDemo.java"
```


![JVM2](E:\git_repo\Hao_Learn\2019\8\img\JVM2.png)