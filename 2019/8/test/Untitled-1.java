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