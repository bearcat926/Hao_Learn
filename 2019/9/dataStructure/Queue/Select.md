|index|my answer|standard answer|
|----|----|----|
|1 -  5|DBDBD|DBDBD|
|6 - 10|DBDCA|**C**B**B**CA|
|11 - 15|BAADD|BAADD|
|16 - 19|BCCC|**A**CCC|

6、front 指向队头元素的前一个位置，rear指向队尾元素 == front 指向队头元素，rear指向队尾元素的后一个位置

8、rear指向队尾元素 ，front 指向队头元素，所以先进行`rear = (rear + 1) % MaxSize`，执行之后是0，所以之前是 n-1。而入队不需要进行front操作，所以front是0。

16、头指针在链表表头，进队在队尾，在链表表尾，进队需要遍历整个链表



例：

1）由输入受限的双端队列得到，但不能由输出受限的双端队列得到的输出序列
2）由输出受限的双端队列得到，但不能由输入受限的双端队列得到的输出序列
3）既不能由输入受限的双端队列得到，又不能由输出受限的双端队列得到的输出序列

解：
输入受限：只有一端可以输入
1）假设同端输入输出，即一个栈，则有 Catalan 数个输出序列
2）剩下的 n! - Catalan 可能，通过两端混合输出。
3）剩下不能通过该数据结构得到的可能

输出受限：只有一端可以输出
1）假设同端输入输出，即一个栈，则有 Catalan 数个输出序列
2）剩下的 n! - Catalan 可能，通过两端混合输入。
3）剩下不能通过该数据结构得到的可能

由以上思路：

输入受限：LI，LO，RO
输出受限：LI，LO，RI

|result|stack|InLimitQueue|OutLimitQueue|
|---|---|---|---|
|1234|stack|||
|1243|stack|||
|1324|stack|||
|1342|stack|||
|1423|x	| LILOLILILILORORO |LILORIRILILOLOLO|
|1432|stack|||
|2134|stack|||
|2143|stack|||
|2314|stack|||
|2341|stack|||
|2413|x|LILILOLILILOROLO|LILILORILILOLOLO|
|2431|stack|||
|3124|x|LILILILOROROLILO|LIRILILOLOLOLILO|
|3142|x|LILILILOROLILOLO|LIRILILOLOLILOLO|
|3214|stack|||
|3241|stack|||
|3412|x|LILILILOLILORORO|LIRILILOLILOLOLO|
|3421|stack|||
|4123|x|LILILILILORORORO|RIRIRILILOLOLOLO|
|4132|x|LILILILILOROLOLO|x|
|4213|x|x|RILIRILILOLOLOLO|
|4231|x|x|x|
|4312|x|LILILILILOLOROLO|RIRILILILOLOLOLO|
|4321|stack|||



