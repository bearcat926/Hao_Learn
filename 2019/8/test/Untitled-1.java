// 在 Iterator 遍历时加锁
Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
    synchronized(obj){
        String item= iterator.next() ;
        if (condition) {
            iterator.remove(); 
        }
    }
}  

// COWArrayList 测试添加
public static void main (String[] args) {
    List<Long> copy= new CopyOnWriteArrayList<Long>();

    long start = System.nanoTime();
    for (int i=0; i<20*10000; i++) {
        copy.add(System.nanoTime()) ; 
    }
}

// 返回Map类对象中的Key的Set视图
Set<K> keySet();
// 返回Map类对象中的所有Value集合的Collection视图
// 返回集合实现类为 Values extends AbstractCollection<V>
Collection<V> values(); 
//返回Map类对象中的Key-Value对的Set视图
Set<Map.Entry<K,V>> entrySet();