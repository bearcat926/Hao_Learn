import java.util.HashMap;

public V put(K key, V value) {
	// 先把 TreeMap 的根节点 root 引用赋值给当前节点
	Entry<K,V> t = root;
	// 如果当前节点为 null ，即是空树，新增的 KV 形成的节点就是根节点
	if (t == null) {
		// 看似事此一举，实际预检了 Key 是否可以比较,
		compare(key, key); 
	/*
		@SuppressWarnings("unchecked")
		final int compare(Object k1, Object k2) {
			return comparator==null ? ((Comparable<? super K>)k1).compareTo((K)k2)
				: comparator.compare((K)k1, (K)k2);
		}
	*/

		root = new Entry<>(key, value, null);
		size = 1;
		modCount++;
		return null;
	}
	// 用来接收比较结果
	int cmp;
	Entry<K,V> parent;
	// 构造方法中置入的外部比较器
	Comparator<? super K> cpr = comparator;
	// 根据二叉查找树的特性，找到新节点插入的合适位置
	if (cpr != null) {
		do {
			parent = t;
			cmp = cpr.compare(key, t.key);
			if (cmp < 0)
				t = t.left;
			else if (cmp > 0)
				t = t.right;
			else
				return t.setValue(value);
		} while (t != null);
	}
	// 在没有指定比较嚣的情况下,调用自然排序的 Comparable 比较
	else { 
		if (key == null)
			throw new NullPointerException();
		@SuppressWarnings("unchecked")
			Comparable<? super K> k = (Comparable<? super K>) key;
		do {
			parent = t;
			cmp = k.compareTo(t.key);
			if (cmp < 0)
				t = t.left;
			else if (cmp > 0)
				t = t.right;
			else
				return t.setValue(value);
		} while (t != null);
	}
	Entry<K,V> e = new Entry<>(key, value, parent);
	// 对 parent 维护
	if (cmp < 0)
		parent.left = e;
	else
		parent.right = e;
	fixAfterInsertion(e);
	size++;
	modCount++;
	return null;
}

@SuppressWarnings("unchecked")
final int compare(Object k1, Object k2) {
	return comparator==null ? ((Comparable<? super K>)k1).compareTo((K)k2)
		: comparator.compare((K)k1, (K)k2);
}

private void fixAfterInsertion(Entry<K,V> x) {
	// 虽然内部类 Entry 的属性 color 默认为黑色，但新节点一律先赋值为红色
	// 这样可以避免插入新节点时违反性质五，只需专注于满足性质四即可。
	x.color = RED;

	// 若该节点为根节点或叶子节点，或该节点的父亲为黑色，则退出循环
	while (x != null && x != root && x.parent.color == RED) {
		// 父亲是爷爷的左孩子，且为红色
		if (parentOf(x) == leftOf(parentOf(parentOf(x)))) {
			Entry<K,V> y = rightOf(parentOf(parentOf(x)));
			// 右叔是红色
			if (colorOf(y) == RED) {
				// 则将父亲和右叔设置为黑色，爷爷设置为红色
				setColor(parentOf(x), BLACK);
				setColor(y, BLACK);
				setColor(parentOf(parentOf(x)), RED);
				// 将当前节点设置为爷爷之后循环，继续调整
				x = parentOf(parentOf(x));
			// 右叔是黑色	
			} else {
				// 若该节点是父亲的右孩子，则需先对父亲进行一次左旋
				// 之后父亲变为该节点的左孩子
				if (x == rightOf(parentOf(x))) {
					x = parentOf(x);
					rotateLeft(x);
				}
				// 注意当前节点为之前的父亲！
				// 将该节点设置为黑色，曾经的爷爷设置为红色
				// 因为爷爷变成红色了，所有右边缺少了一个黑色节点
				// 则需要对爷爷进行右旋，即将该（黑色）节点放置在之前爷爷的位置上
				setColor(parentOf(x), BLACK);
				setColor(parentOf(parentOf(x)), RED);
				rotateRight(parentOf(parentOf(x)));
			}
		// 父亲是爷爷的右孩子
		} else {
			Entry<K,V> y = leftOf(parentOf(parentOf(x)));
			// 左叔是红色
			if (colorOf(y) == RED) {
				// 则将父亲和左叔设置为黑色，爷爷设置为红色
				setColor(parentOf(x), BLACK);
				setColor(y, BLACK);
				setColor(parentOf(parentOf(x)), RED);
				// 将当前节点设置为爷爷之后循环，继续调整
				x = parentOf(parentOf(x));
			// 左叔是黑色
			} else {
				// 若该节点是父亲的左孩子，则需先对父亲进行一次右旋
				// 之后父亲变为该节点的右孩子
				if (x == leftOf(parentOf(x))) {
					x = parentOf(x);
					rotateRight(x);
				}
				// 注意当前节点为之前的父亲！
				// 将该节点设置为黑色，曾经的爷爷设置为红色
				// 因为爷爷变成红色了，所有左边缺少了一个黑色节点
				// 则需要对爷爷进行左旋，即将该（黑色）节点放置在之前爷爷的位置上
				setColor(parentOf(x), BLACK);
				setColor(parentOf(parentOf(x)), RED);
				rotateLeft(parentOf(parentOf(x)));
			}
		}
	}
	// 将根节点置为黑色
	root.color = BLACK;
}

private void rotateLeft(Entry<K,V> p) {
	if (p != null) {
		Entry<K,V> r = p.right;
		// 1. 先修改该节点与其右孩子的关系（p认子），将 p.right 设置为 r.left。
		p.right = r.left;
		//如果 r.left 不为空（叶子节点），则需要将其parent 设置为 p，即维护一
		if (r.left != null)
			r.left.parent = p;
		// 2. 之后修改将 r.parent 设置为 p.parent（r认父）
		r.parent = p.parent;
		// 如果 p.parent为空，则 p为根节点，则将 root设置为r
		if (p.parent == null)
			root = r;
		// 否则将 p.parent的对应孩子设置为r
		else if (p.parent.left == p)
			p.parent.left = r;
		else
			p.parent.right = r;
		// 3. 最后将 r和p 与其原有的关系断开（一刀两断），即p认父，r认子
		// 将 r和rl 的关系断掉，将 r.left设置为p
		// 将 p和pp 的关系断掉，将 p.parent设置为r
		r.left = p;
		p.parent = r;
	}
}

private void rotateRight(Entry<K,V> p) {
	if (p != null) {
		Entry<K,V> l = p.left;
		p.left = l.right;
		if (l.right != null) l.right.parent = p;
		l.parent = p.parent;
		if (p.parent == null)
			root = l;
		else if (p.parent.right == p)
			p.parent.right = l;
		else p.parent.left = l;
		l.right = p;
		p.parent = l;
	}
}

public V put(K key, V value) {
	// 先把 TreeMap 的根节点 root 引用赋值给当前节点
	Entry<K,V> t = root;
	// 如果当前节点为 null ，即是空树，新增的 KV 形成的节点就是根节点
	if (t == null) {
		// 看似事此一举，实际预检了 Key 是否可以比较,
		compare(key, key); 
	/*
		@SuppressWarnings("unchecked")
		final int compare(Object k1, Object k2) {
			return comparator==null ? ((Comparable<? super K>)k1).compareTo((K)k2)
				: comparator.compare((K)k1, (K)k2);
		}
	*/

		root = new Entry<>(key, value, null);
		size = 1;
		modCount++;
		return null;
	}
	// 用来接收比较结果
	int cmp;
	Entry<K,V> parent;
	// 构造方法中置入的外部比较器
	Comparator<? super K> cpr = comparator;
	// 根据二叉查找树的特性，找到新节点插入的合适位置
	if (cpr != null) {
		do {
			parent = t;
			cmp = cpr.compare(key, t.key);
			if (cmp < 0)
				t = t.left;
			else if (cmp > 0)
				t = t.right;
			else
				return t.setValue(value);
		} while (t != null);
	}
	// 在没有指定比较嚣的情况下,调用自然排序的 Comparable 比较
	else { 
		if (key == null)
			throw new NullPointerException();
		@SuppressWarnings("unchecked")
			Comparable<? super K> k = (Comparable<? super K>) key;
		do {
			parent = t;
			cmp = k.compareTo(t.key);
			if (cmp < 0)
				t = t.left;
			else if (cmp > 0)
				t = t.right;
			else
				return t.setValue(value);
		} while (t != null);
	}
	Entry<K,V> e = new Entry<>(key, value, parent);
	// 对 parent 维护
	if (cmp < 0)
		parent.left = e;
	else
		parent.right = e;
	fixAfterInsertion(e);
	size++;
	modCount++;
	return null;
}

@SuppressWarnings("unchecked")
final int compare(Object k1, Object k2) {
	return comparator==null ? ((Comparable<? super K>)k1).compareTo((K)k2)
		: comparator.compare((K)k1, (K)k2);
}

private void fixAfterInsertion(Entry<K,V> x) {
	// 虽然内部类 Entry 的属性 color 默认为黑色，但新节点一律先赋值为红色
	// 这样可以避免插入新节点时违反性质五，只需专注于满足性质四即可。
	x.color = RED;

	// 若该节点为根节点或叶子节点，或该节点的父亲为黑色，则退出循环
	while (x != null && x != root && x.parent.color == RED) {
		// 父亲是爷爷的左孩子，且为红色
		if (parentOf(x) == leftOf(parentOf(parentOf(x)))) {
			Entry<K,V> y = rightOf(parentOf(parentOf(x)));
			// 右叔是红色
			if (colorOf(y) == RED) {
				// 则将父亲和右叔设置为黑色，爷爷设置为红色
				setColor(parentOf(x), BLACK);
				setColor(y, BLACK);
				setColor(parentOf(parentOf(x)), RED);
				// 将当前节点设置为爷爷之后循环，继续调整
				x = parentOf(parentOf(x));
			// 右叔是黑色	
			} else {
				// 若该节点是父亲的右孩子，则需先对父亲进行一次左旋
				// 之后父亲变为该节点的左孩子
				if (x == rightOf(parentOf(x))) {
					x = parentOf(x);
					rotateLeft(x);
				}
				// 注意当前节点为之前的父亲！
				// 将该节点设置为黑色，曾经的爷爷设置为红色
				// 因为爷爷变成红色了，所有右边缺少了一个黑色节点
				// 则需要对爷爷进行右旋，即将该（黑色）节点放置在之前爷爷的位置上
				setColor(parentOf(x), BLACK);
				setColor(parentOf(parentOf(x)), RED);
				rotateRight(parentOf(parentOf(x)));
			}
		// 父亲是爷爷的右孩子
		} else {
			Entry<K,V> y = leftOf(parentOf(parentOf(x)));
			// 左叔是红色
			if (colorOf(y) == RED) {
				// 则将父亲和左叔设置为黑色，爷爷设置为红色
				setColor(parentOf(x), BLACK);
				setColor(y, BLACK);
				setColor(parentOf(parentOf(x)), RED);
				// 将当前节点设置为爷爷之后循环，继续调整
				x = parentOf(parentOf(x));
			// 左叔是黑色
			} else {
				// 若该节点是父亲的左孩子，则需先对父亲进行一次右旋
				// 之后父亲变为该节点的右孩子
				if (x == leftOf(parentOf(x))) {
					x = parentOf(x);
					rotateRight(x);
				}
				// 注意当前节点为之前的父亲！
				// 将该节点设置为黑色，曾经的爷爷设置为红色
				// 因为爷爷变成红色了，所有左边缺少了一个黑色节点
				// 则需要对爷爷进行左旋，即将该（黑色）节点放置在之前爷爷的位置上
				setColor(parentOf(x), BLACK);
				setColor(parentOf(parentOf(x)), RED);
				rotateLeft(parentOf(parentOf(x)));
			}
		}
	}
	// 将根节点置为黑色
	root.color = BLACK;
}

private void rotateLeft(Entry<K,V> p) {
	if (p != null) {
		Entry<K,V> r = p.right;
		// 1. 先修改该节点与其右孩子的关系（p认子），将 p.right 设置为 r.left。
		p.right = r.left;
		//如果 r.left 不为空（叶子节点），则需要将其parent 设置为 p，即维护一
		if (r.left != null)
			r.left.parent = p;
		// 2. 之后修改将 r.parent 设置为 p.parent（r认父）
		r.parent = p.parent;
		// 如果 p.parent为空，则 p为根节点，则将 root设置为r
		if (p.parent == null)
			root = r;
		// 否则将 p.parent的对应孩子设置为r
		else if (p.parent.left == p)
			p.parent.left = r;
		else
			p.parent.right = r;
		// 3. 最后将 r和p 与其原有的关系断开（一刀两断），即p认父，r认子
		// 将 r和rl 的关系断掉，将 r.left设置为p
		// 将 p和pp 的关系断掉，将 p.parent设置为r
		r.left = p;
		p.parent = r;
	}
}

private void rotateRight(Entry<K,V> p) {
	if (p != null) {
		Entry<K,V> l = p.left;
		p.left = l.right;
		if (l.right != null) l.right.parent = p;
		l.parent = p.parent;
		if (p.parent == null)
			root = l;
		else if (p.parent.right == p)
			p.parent.right = l;
		else p.parent.left = l;
		l.right = p;
		p.parent = l;
	}
}


ThreadLocal

public T get() {
	Thread t = Thread.currentThread();
	ThreadLocalMap map = getMap(t);
	if (map != null) {
		ThreadLocalMap.Entry e = map.getEntry(this);
		if (e != null) {
			@SuppressWarnings("unchecked")
			T result = (T)e.value;
			return result;
		}
	}
	return setInitialValue();
}

protected T initialValue() {
	return null;
}

private T setInitialValue() {
	T value = initialValue();
	Thread t = Thread.currentThread();
	ThreadLocalMap map = getMap(t);
	if (map != null)
		map.set(this, value);
	else
		createMap(t, value);
	return value;
}

static class Entry extends WeakReference<ThreadLocal<?>> {
	/** The value associated with this ThreadLocal. */
	Object value;

	Entry(ThreadLocal<?> k, Object v) {
		super(k);
		value = v;
	}
}

Thread

public Thread(ThreadGroup group, Runnable target, String name,
				long stackSize) {
	init(group, target, name, stackSize);
}

private void init(ThreadGroup g, Runnable target, String name,
                      long stackSize) {
	init(g, target, name, stackSize, null, true);
}

private void init(ThreadGroup g, Runnable target, String name,
					long stackSize, AccessControlContext acc,
					boolean inheritThreadLocals) {
	if (name == null) {
		throw new NullPointerException("name cannot be null");
	}
	this.name = name;

	Thread parent = currentThread();
	SecurityManager security = System.getSecurityManager();
	if (g == null) {
		/* Determine if it's an applet or not */

		/* If there is a security manager, ask the security manager
			what to do. */
		if (security != null) {
			g = security.getThreadGroup();
		}

		/* If the security doesn't have a strong opinion of the matter
			use the parent thread group. */
		if (g == null) {
			g = parent.getThreadGroup();
		}
	}

	/* checkAccess regardless of whether or not threadgroup is
		explicitly passed in. */
	g.checkAccess();

	/*
		* Do we have the required permissions?
		*/
	if (security != null) {
		if (isCCLOverridden(getClass())) {
			security.checkPermission(SUBCLASS_IMPLEMENTATION_PERMISSION);
		}
	}

	g.addUnstarted();

	this.group = g;
	this.daemon = parent.isDaemon();
	this.priority = parent.getPriority();
	if (security == null || isCCLOverridden(parent.getClass()))
		this.contextClassLoader = parent.getContextClassLoader();
	else
		this.contextClassLoader = parent.contextClassLoader;
	this.inheritedAccessControlContext =
			acc != null ? acc : AccessController.getContext();
	this.target = target;
	setPriority(priority);
	if (inheritThreadLocals && parent.inheritableThreadLocals != null)
		this.inheritableThreadLocals =
			ThreadLocal.createInheritedMap(parent.inheritableThreadLocals);
	/* Stash the specified stack size in case the VM cares */
	this.stackSize = stackSize;

	/* Set thread ID */
	tid = nextThreadID();
}

static ThreadLocalMap createInheritedMap(ThreadLocalMap parentMap) {
	return new ThreadLocalMap(parentMap);
}

private ThreadLocalMap(ThreadLocalMap parentMap) {
	Entry[] parentTable = parentMap.table;
	int len = parentTable.length;
	setThreshold(len);
	table = new Entry[len];

	for (int j = 0; j < len; j++) {
		Entry e = parentTable[j];
		if (e != null) {
			@SuppressWarnings("unchecked")
			ThreadLocal<Object> key = (ThreadLocal<Object>) e.get();
			if (key != null) {
				Object value = key.childValue(e.value);
				Entry c = new Entry(key, value);
				int h = key.threadLocalHashCode & (len - 1);
				while (table[h] != null)
					h = nextIndex(h, len);
				table[h] = c;
				size++;

			}
		}
	}
}

public class RequestProcessTrace {
	private static final InheritableThreadLocal<FullLinkContext> FULL_LINK_THREADLOCAL = new InheritableThreadLocal<>();
	public static FullLinkContext getContext() {
		FullLinkContext fullLinkContext = FULL_LINK_THREADLOCAL.get();
		if (fullLinkContext == null ) {
			FULL_LINK_THREADLOCAL.set(new FullLinkContext()) ;
			fullLinkContext = FULL_LINK_THREADLOCAL.get () ;
		}
		return fullLinkContext;
	}

	public static class FullLinkContext {
		private String traceId;
		public String getTraceid () {
			if (StringUtils.isEmpty(traceid)) {
				FrameWork.startTrace(null, "gujin");
				traceid = FrameWork.getTraceId();
			}
			return traceId;
		}
		public void setTraceid(String traceid) {
			this.traceId = traceId;
		}
	}
}

HashMap
//JDK7

public V put(K key, V value) {
	// 数组为空，则初始化扩容
	if (table == EMPTY_TABLE) {
		inflateTable(threshold);
	}
	// 存储空键的KV对
	if (key == null)
		return putForNullKey(value);
	int hash = hash(key);
	int i = indexFor(hash, table.length);
	// 此循环通过 hashCode 返回值找到对应的数组下标位置
	for (Entry<K,V> e = table[i]; e != null; e = e.next) {
		Object k;
		// 为了覆盖旧值
		if (e.hash == hash && ((k = e.key) == key || key.equals(k))) {
			V oldValue = e.value;
			e.value = value;
			e.recordAccess(this);
			return oldValue;
		}
	}

	// 还没有添加元素就进行 modCount++，将为后续留下很多隐患
	modCount++;
	// 添加元素，参数i为table数组的下标
	addEntry(hash, key, value, i);
	return null;
}

void addEntry(int hash, K key, V value, int bucketIndex) {
	// 如果元素的个数达到扩容阈值threshold且数组下标位置已经存在元素，则进行扩容
	if ((size >= threshold) && (null != table[bucketIndex])) {
		// 扩容2倍，size是实际存放元素的个数，而length是数组的容量大小
		resize(2 * table.length);
		hash = (null != key) ? hash(key) : 0;
		bucketIndex = indexFor(hash, table.length);
	}

	createEntry(hash, key, value, bucketIndex);
}

// 插入元素时，应插入头部，而不是尾部
void createEntry(int hash, K key, V value, int bucketIndex) {
	// 不管原来的数组对应的下标元素是否为null，都作为Entry的bucketIndex的next值
	Entry<K,V> e = table[bucketIndex];
	// 即使原来是链表，也把整条链都挂在新插入的节点下
	table[bucketIndex] = new Entry<>(hash, key, value, e);
	size++;
}

void resize(int newCapacity) {
	// 获取旧表
	Entry[] oldTable = table;
	int oldCapacity = oldTable.length;
	// int MAXIMUM_CAPACITY = 1073741824 = 1 << 30
	if (oldCapacity == MAXIMUM_CAPACITY) {
		// 扩容阈值设置为 ‭2147483647‬，并返回，不能再扩容了
		threshold = Integer.MAX_VALUE;
		return;
	}
	Entry[] newTable = new Entry[newCapacity];
	// JDK8移除hashSeed计算，因为计算时会调用Random.nextInt()，存在性能问题
	transfer(newTable, initHashSeedAsNeeded(newCapacity));
	// 在此步骤完成前，旧表上依然可以进行元素的增加操作，这是对象丢失的原因之一
	table = newTable;
	threshold = (int)Math.min(newCapacity * loadFactor, MAXIMUM_CAPACITY + 1);
}

// 从旧表迁移数据到新表
void transfer(Entry[] newTable, boolean rehash) {
	// 新表大小已经指定为2 * oldTable.length
	int newCapacity = newTable.length;
	// 使用 foreach 方式遍历整个数组
	for (Entry<K,V> e : table) {
		// 如果此 slot 上存在元素，则进行链表遍历（也有可能是单个节点），
		// 直到null != e，退出循环
		while(null != e) {
			Entry<K,V> next = e.next;
			// 当前元素总是直接放在数组下标的 slot 上．而不是放在链表的最后
			if (rehash) {
				e.hash = null == e.key ? 0 : hash(e.key);
			}
			int i = indexFor(e.hash, newCapacity);
			// 因为新数组上可能有元素（没有的话就是null），
			// 所以把原来 slot 上的元素作为 e.next
			// 新迁移过来的节点直接放置在 slot 位置上
			// 形象来说就是，将节点放入两者之间
			e.next = newTable[i];
			newTable[i] = e;
			// 链表继续向下遍历
			e = next;
		}
	}
}


//JDK8
public V put(K key, V value) {
	return putVal(hash(key), key, value, false, true);
}

final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                   boolean evict) {
	Node<K,V>[] tab; Node<K,V> p; int n, i;
	if ((tab = table) == null || (n = tab.length) == 0)
		n = (tab = resize()).length;
	if ((p = tab[i = (n - 1) & hash]) == null)
		tab[i] = newNode(hash, key, value, null);
	else {
		Node<K,V> e; K k;
		if (p.hash == hash &&
			((k = p.key) == key || (key != null && key.equals(k))))
			e = p;
		else if (p instanceof TreeNode)
			e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
		else {
			for (int binCount = 0; ; ++binCount) {
				if ((e = p.next) == null) {
					p.next = newNode(hash, key, value, null);
					if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
						treeifyBin(tab, hash);
					break;
				}
				if (e.hash == hash &&
					((k = e.key) == key || (key != null && key.equals(k))))
					break;
				p = e;
			}
		}
		if (e != null) { // existing mapping for key
			V oldValue = e.value;
			if (!onlyIfAbsent || oldValue == null)
				e.value = value;
			afterNodeAccess(e);
			return oldValue;
		}
	}
	++modCount;
	if (++size > threshold)
		resize();
	afterNodeInsertion(evict);
	return null;
}

final Node<K,V>[] resize() {
	Node<K,V>[] oldTab = table;
	int oldCap = (oldTab == null) ? 0 : oldTab.length;
	int oldThr = threshold;
	int newCap, newThr = 0;
	if (oldCap > 0) {
		if (oldCap >= MAXIMUM_CAPACITY) {
			threshold = Integer.MAX_VALUE;
			return oldTab;
		}
		else if ((newCap = oldCap << 1) < MAXIMUM_CAPACITY &&
				 oldCap >= DEFAULT_INITIAL_CAPACITY)
			newThr = oldThr << 1; // double threshold
	}
	else if (oldThr > 0) // initial capacity was placed in threshold
		newCap = oldThr;
	else {               // zero initial threshold signifies using defaults
		newCap = DEFAULT_INITIAL_CAPACITY;
		newThr = (int)(DEFAULT_LOAD_FACTOR * DEFAULT_INITIAL_CAPACITY);
	}
	if (newThr == 0) {
		float ft = (float)newCap * loadFactor;
		newThr = (newCap < MAXIMUM_CAPACITY && ft < (float)MAXIMUM_CAPACITY ?
				  (int)ft : Integer.MAX_VALUE);
	}
	threshold = newThr;
	@SuppressWarnings({"rawtypes","unchecked"})
		Node<K,V>[] newTab = (Node<K,V>[])new Node[newCap];
	table = newTab;
	if (oldTab != null) {
		for (int j = 0; j < oldCap; ++j) {
			Node<K,V> e;
			if ((e = oldTab[j]) != null) {
				oldTab[j] = null;
				if (e.next == null)
					newTab[e.hash & (newCap - 1)] = e;
				else if (e instanceof TreeNode)
					((TreeNode<K,V>)e).split(this, newTab, j, oldCap);
				else { // preserve order
					Node<K,V> loHead = null, loTail = null;
					Node<K,V> hiHead = null, hiTail = null;
					Node<K,V> next;
					do {
						next = e.next;
						if ((e.hash & oldCap) == 0) {
							if (loTail == null)
								loHead = e;
							else
								loTail.next = e;
							loTail = e;
						}
						else {
							if (hiTail == null)
								hiHead = e;
							else
								hiTail.next = e;
							hiTail = e;
						}
					} while ((e = next) != null);
					if (loTail != null) {
						loTail.next = null;
						newTab[j] = loHead;
					}
					if (hiTail != null) {
						hiTail.next = null;
						newTab[j + oldCap] = hiHead;
					}
				}
			}
		}
	}
	return newTab;
}

final TreeNode<K,V> putTreeVal(HashMap<K,V> map, Node<K,V>[] tab,
                                       int h, K k, V v) {
	Class<?> kc = null;
	boolean searched = false;
	TreeNode<K,V> root = (parent != null) ? root() : this;
	for (TreeNode<K,V> p = root;;) {
		int dir, ph; K pk;
		if ((ph = p.hash) > h)
			dir = -1;
		else if (ph < h)
			dir = 1;
		else if ((pk = p.key) == k || (k != null && k.equals(pk)))
			return p;
		else if ((kc == null &&
					(kc = comparableClassFor(k)) == null) ||
					(dir = compareComparables(kc, k, pk)) == 0) {
			if (!searched) {
				TreeNode<K,V> q, ch;
				searched = true;
				if (((ch = p.left) != null &&
						(q = ch.find(h, k, kc)) != null) ||
					((ch = p.right) != null &&
						(q = ch.find(h, k, kc)) != null))
					return q;
			}
			dir = tieBreakOrder(k, pk);
		}

		TreeNode<K,V> xp = p;
		if ((p = (dir <= 0) ? p.left : p.right) == null) {
			Node<K,V> xpn = xp.next;
			TreeNode<K,V> x = map.newTreeNode(h, k, v, xpn);
			if (dir <= 0)
				xp.left = x;
			else
				xp.right = x;
			xp.next = x;
			x.parent = x.prev = xp;
			if (xpn != null)
				((TreeNode<K,V>)xpn).prev = x;
			moveRootToFront(tab, balanceInsertion(root, x));
			return null;
		}
	}
}

final void treeifyBin(Node<K,V>[] tab, int hash) {
	int n, index; Node<K,V> e;
	if (tab == null || (n = tab.length) < MIN_TREEIFY_CAPACITY)
		resize();
	else if ((e = tab[index = (n - 1) & hash]) != null) {
		TreeNode<K,V> hd = null, tl = null;
		do {
			TreeNode<K,V> p = replacementTreeNode(e, null);
			if (tl == null)
				hd = p;
			else {
				p.prev = tl;
				tl.next = p;
			}
			tl = p;
		} while ((e = e.next) != null);
		if ((tab[index] = hd) != null)
			hd.treeify(tab);
	}
}

Entry<K, V> next = e.next; 
e.next = newTable[i];
newTable[i] = e;
e = next;

ConcurrentHashMap
// 默认为null，ConcurrentHashMap 存放数据的地方，扩容时大小总是2的幂次方
// 初始化发生在第一次插入操作，数组默认初始化大小为 16
transient volatile Node<K,V>[] table;
// 默认为null，扩容时新生成的数组，其大小为原数组的两倍
private transient volatile Node<K,V>[] nextTable;
// 存储单个KV数据节点。内部有 key、value、hash、next 指向下一个节点
// 它有4个在 ConcurrentHashMap 类内部定义的子类：
// TreeBin、TreeNode、ForwardingNode、ReservationNode
// 前3个子类都重写了查找元素的重要方法 find()
static class Node<K,V> implements Map.Entry<K,V> { ... }

// 它并不存储实际数据，维护对桶内红黑树的读写锁，存储对红黑树节点的引用
static final class TreeBin<K,V> extends Node<K,V> { ... }
// 在红黑树结构中，实际存储数据的节点
static final class TreeNode<K,V> extends Node<K,V> { ... }
// 扩容转发节点，放置此节点后，外部对原有哈希槽的操作会转发到 nextTable 上
static final class ForwardingNode<K,V> extends Node<K,V> { ... }
// 占位加锁节点。执行某些方法时，对其加锁，如 computeIfAbsent 等
static final class ReservationNode<K,V> extends Node<K,V> { ... }

// 默认为0，用来控制table的初始化和扩容操作
// sizeCtl = -1，表示正在初始化中
// sizeCtl = -n，表示（n-1）个线程正在进行扩容，即-1 -（线程数）
// sizeCtl > 0，初始化或扩容中需要使用的容量
// sizeCtl = 0，默认值，使用默认容量进行初始化
private transient volatile int sizeCtl;
// 集合size小于64，无论如何，都不会使用红黑树结构
// 转化为红黑树还有一个条件是 TREEIFY_THRESHOLD
static final int MIN_TREEIFY_CAPACITY = 64;
// 同一个哈希桶内存储的元素个数超过此阈值时
// 存储结构有链表转换为红黑树
static final int TREEIFY_THRESHOLD = 8;
// 同一个哈希桶内存储的元素个数小于等于此阈值时
// 从红黑树回退至链表结构，因为元素个数较少时，链表更快
static final int UNTREEIFY_THRESHOLD = 6;

// 记录了元素总数值，主要用在无竞争状态下
// 在总数更新后，通过 CAS 方式直接更新这个值
private transient volatile long baseCount;
// 一个计数器单元．维护了一个 value 值
@sun.misc.Contended static final class CounterCell { ... }
// 在竟争激烈的状态下启用，线程会把总数更新情况存放到该结构内
// 当竞争进一步加剧时，会通过扩容减少竞争
private transient volatile CounterCell[] counterCells;


ThreadPoolExecutor

public ThreadPoolExecutor(
				int corePoolSize,
				int maximumPoolSize,
				long keepAliveTime,
				TimeUnit unit,
				BlockingQueue<Runnable> workQueue,
				ThreadFactory threadFactory,
				RejectedExecutionHandler handler) {
	if (corePoolSize < 0 ||
		maximumPoolSize <= 0 ||
		maximumPoolSize < corePoolSize ||
		keepAliveTime < 0)
		throw new IllegalArgumentException();
	if (workQueue == null || threadFactory == null || handler == null)
		throw new NullPointerException();
	this.acc = System.getSecurityManager() == null ?
			null :
			AccessController.getContext();
	this.corePoolSize = corePoolSize;
	this.maximumPoolSize = maximumPoolSize;
	this.workQueue = workQueue;
	this.keepAliveTime = unit.toNanos(keepAliveTime);
	this.threadFactory = threadFactory;
	this.handler = handler;
}


// 初始值为 线程池能接受新任务且线程数为0
private final AtomicInteger ctl = new AtomicInteger(ctlOf(RUNNING, 0));
// Integer有32位，最左边3位表示线程池状态，右边29位表示工作线程数
private static final int COUNT_BITS = Integer.SIZE - 3;
// 线程容量，但实际为掩码，用于位的与运算
// 000 - 11111111111111111111111111111
private static final int CAPACITY   = (1 << COUNT_BITS) - 1;

// 111 - 00000000000000000000000000000
// 此状态表示线程池能接受新任务
private static final int RUNNING    = -1 << COUNT_BITS;
// 000 - 00000000000000000000000000000
// 此状态表示线程池不能接受新任务，但可以继续执行队列中的任务
private static final int SHUTDOWN   =  0 << COUNT_BITS;
// 001 - 00000000000000000000000000000
// 此状态表示线程池全面拒绝，并中断正在处理的任务
private static final int STOP       =  1 << COUNT_BITS;
// 010 - 00000000000000000000000000000
// 此状态表示线程池中所有的任务都被终止了
private static final int TIDYING    =  2 << COUNT_BITS;
// 011 - 00000000000000000000000000000
// 此状态表示已清理完现场
private static final int TERMINATED =  3 << COUNT_BITS;

// c & 111 - 00000000000000000000000000000，有0得0，可得到状态值
private static int runStateOf(int c)     { return c & ~CAPACITY; }
// c & 000 - 11111111111111111111111111111，有0得0，可得到线程数
private static int workerCountOf(int c)  { return c & CAPACITY; }
// 有1得1，可合并出ctl
private static int ctlOf(int rs, int wc) { return rs | wc; }

private static boolean runStateLessThan(int c, int s) {
	return c < s;
}

private static boolean runStateAtLeast(int c, int s) {
	return c >= s;
}

private static boolean isRunning(int c) {
	return c < SHUTDOWN;
}

public void execute(Runnable command) {
	if (command == null)
		throw new NullPointerException();
	

	int c = ctl.get();
	// 如果工作线程数小于核心线程数，则创建线程任务并执行
	if (workerCountOf(c) < corePoolSize) {
		// 判断常驻核心线程数
		if (addWorker(command, true))
			return;
		// 如果创建任务失败，防止外部已经在线程池中加入新任务，重新获取一下
		c = ctl.get();
	}

	// 只有线程池处于RUNNING状态，才执行workQueue.offer - 置入队列
	if (isRunning(c) && workQueue.offer(command)) {
		int recheck = ctl.get();
		// 如果线程池当前不是RUNNING状态，则将刚加入队列的任务移除，之后唤醒拒绝策略
		if (! isRunning(recheck) && remove(command))
			reject(command);
		// 如果之前的线程已经被消费完，新建一个线程，判断最大允许线程数
		else if (workerCountOf(recheck) == 0)
			addWorker(null, false);
	}
	// 核心池和队列都已满，尝试创建一个新线程，判断最大允许线程数
	else if (!addWorker(command, false))
		// 如果创建失败，则唤醒拒绝策略
		reject(command);
}


// 根据当前线程池状态，检查是否可以添加新的任务线程，如果可以则创建并启动任务
private boolean addWorker(Runnable firstTask, boolean core) {
	retry: // 配合循环语旬出现的label ，类似于goto作用。
	for (;;) {
		int c = ctl.get();
		int rs = runStateOf(c);

		// 如果RUNNING状态，则条件为假，不执行后面的判断
		// 如果为STOP及之上的状态，或者初始线程firstTask不为空，或者队列为空
		// 都会直接导致创建失败
		if (rs >= SHUTDOWN &&
			! (rs == SHUTDOWN &&
			   firstTask == null &&
			   ! workQueue.isEmpty()))
			return false;

		for (;;) {
			int wc = workerCountOf(c);
			// 如果线程数超过容量则不能再添加新的线程。
			// 如果线程数超过常驻核心线程数 最大允许线程数
			if (wc >= CAPACITY ||
				wc >= (core ? corePoolSize : maximumPoolSize))
				return false;
			// 将当前活动线程数+1，原子性操作
			// 该方法执行失败的概率非常低。即使失败，
			// 再次执行时成功的概率也是极高的，类似于自旋锁原理。
			if (compareAndIncrementWorkerCount(c))
				break retry;
			
			// ctl是可变化的，需要经常读取最新值
			c = ctl.get(); 
			// 如果线程池已关闭，则再次循环
			if (runStateOf(c) != rs)
				continue retry;
			// 否则，由于WorkerCount更改，CAS失败；retry内部循环
		}
	}

	// 开始创建工作线程
	boolean workerStarted = false;
	boolean workerAdded = false;
	Worker w = null;
	try {
		// 利用Worker构造方法中的线程池工厂创建线程，并封装成工作线程Worker类
		w = new Worker(firstTask);
		// 获取Worker中的属性对象thread
		final Thread t = w.thread;
		if (t != null) {
			// 在进行ThreadPoolExecutor的敏感操作时，需要加主锁，避免在添加和启动线程时被干扰
			final ReentrantLock mainLock = this.mainLock;
			mainLock.lock();
			try {
				// 当保持锁的时候重新检查
				// 如果ThreadFactory发生故障或在获取锁之前关闭，则退出
				int rs = runStateOf(ctl.get());
				// 线程池为RUNNING状态 或 线程池为RUNNING状态且初始线程firstTask为空
				if (rs < SHUTDOWN ||
					(rs == SHUTDOWN && firstTask == null)) {
					if (t.isAlive()) // 预检t是否启动
						throw new IllegalThreadStateException();
					// private final HashSet<Worker> workers = new HashSet<Worker>();
					// 运用HashSet存储了线程池中所有的工作线程，只有在保持主锁的时候才访问
					workers.add(w);
					int s = workers.size();
					// largestPoolSize 为整个线程池在运行期间的最大并发任务个数
					if (s > largestPoolSize)
						largestPoolSize = s;
					workerAdded = true;
				}
			} finally {
				mainLock.unlock();
			}
			if (workerAdded) {
				// 通过查看下面Worker类的源码，发现启动的是新创建的线程t，
				// 而非execute方法的参数command指向的线程
				t.start();
				workerStarted = true;
			}
		}
	} finally {
		// 线程启动失败，需要移除刚添加工作线程并减去当前活动线程数
		if (! workerStarted)
			addWorkerFailed(w);
	}
	return workerStarted;
}

private void addWorkerFailed(Worker w) {
	final ReentrantLock mainLock = this.mainLock;
	mainLock.lock();
	try {
		// 移除工作线程
		if (w != null)
			workers.remove(w);
		// 减去当前活动线程数
		decrementWorkerCount();
		tryTerminate();
	} finally {
		mainLock.unlock();
	}
}

private void decrementWorkerCount() {
	do {} while (! compareAndDecrementWorkerCount(ctl.get()));
}

// 使用了CAS
private boolean compareAndDecrementWorkerCount(int expect) {
	return ctl.compareAndSet(expect, expect - 1);
}

public final boolean compareAndSet(int expect, int update) {
	return unsafe.compareAndSwapInt(this, valueOffset, expect, update);
}

private final class Worker
        extends AbstractQueuedSynchronizer
        implements Runnable
{
	final Thread thread;
	Runnable firstTask;

	Worker(Runnable firstTask) {
		// AbstractQueuedSynchronized 的方法
		setState(-1); // 在调用runWorker之前禁止线程被中断
		this.firstTask = firstTask;
		this.thread = getThreadFactory().newThread(this);
	}

	// 当thread被start()之后，执行runWorker
	public void run() {
		runWorker(this);
	}
}