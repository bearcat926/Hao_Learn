# Redis

## 介绍

Redis 是一个使用 ANSIC 编写的开源、支持网络、基于内存、可选持久性的键值对存储数据库。
特点：开源；多种数据结构；基于键值的存储服务系统；高性能；功能服务；它可以存储键与 5 种不同类型的值之前的映射；可以进行持久化；可以使用复制来扩展读性能；还可以使用分片来扩展写性能。

## 与 Memcached 区别
1. Redis 不仅仅支持简单的 k/v 类型的数据，同时还提供 list，set，zset，hash 等数据结构
的存储。
2. Redis 支持数据的备份，即 master-slave 模式的数据备份。
Redis Cluster 是一个实现了分布式且允许单点故障的 Redis 高级版本，它没有中心节点，具有线性可伸缩的功能。
Memcached 本身并不支持分布式，因此只能在客户端通过像一致性哈希这样的分布式算法来实现 Memcached 的分布式存储。
3. Redis 支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用。
4. 内存管理机制不同：
Memcached 默认使用 Slab Allocation 机制管理内存，其主要思想是按照预先规定的大小，将分配的内存分割成特定长度的块以存储相应长度的 key-value 数据记录，以完全解决内存碎片问题。Memcached 的内存管理制效率高，而且不会造成内存碎片，但是它最大的缺点就是会导致空间浪费。因为每个 Chunk 都分配了特定长度的内存空间，所以变长数据无法充分利用这些空间。

Redis 采用的是包装的 malloc/free，相较于 Memcached 的内存管理方法来说，要简单很多。

## 优点
1. 数据类型丰富
2. 效率高
3. 支持集群
4. 支持持久化

## 缺点
1. 单进程单线程，长命令会导致 Redis 阻塞
2. 集群下多 key 操作（事务、MGET、MSET）无法使用
3. 无法自动迁移

## 数据类型

|key| 数据结构 |内部编码|
|---|---|---|
|	|string|raw|
|	|	|int|
|	|	|embstr|
|	|hash|hashtable|
|	|	|ziplist|
|	|list|linkedlist|
|	|	|ziplist|
|	|set|hashtable|
|	|	|intset|
|	|zset|skiplist|
|	|	|ziplist|

#### String
值可以是字符串、数字（整数、浮点数）或者二进制。
整数范围与系统的长整型的取值范围相同（32 位系统是 32 位，64 位系统是 64 位）
浮点数的精度与 double 相同
| 命令 |说明|时间复杂度|
|---|---|---|
|set key value [EX seconds] [PX milliseconds] [`NX|XX`]|设置 key value。NX 指只在键不存在时， 才对键进行设置操作。XX 指只在键已经存在时， 才对键进行设置操作。|O(1)|
|setnx key value|仅在键 key 不存在的情况下，将键 key 的值设置为 value 。若键 key 已经存在， 则 setnx命令不做任何动作。setnx是『SET if Not eXists』的简写。在命令设置成功时返回 1， 设置失败时返回 0。 |O(1)|
|setex key seconds value|将键 key 的值设置为 value ， 并将键 key 的生存时间设置为 seconds 。如果键 key 已经存在， 那么 setex 命令将覆盖已有的值。setex命令的效果和以下两个命令的效果类似：`SET key value EXPIRE key seconds  # 设置生存时间` <br>这两个命令的不同之处在于 setex是一个原子（atomic）操作**， 它可以在同一时间内完成设置值和设置过期时间这两个操作， 因此 setex命令在储存缓存的时候非常实用。 |O(1)|
|psetex key milliseconds value|这个命令和 setex命令相似， 但它以毫秒为单位设置 key 的生存时间， 而不是像 setex命令那样以秒为单位进行设置。 |O(1)|
|get key|获取key对应的value|O(1)|
|getset key newvalue|set key newvalue 并返回旧的 value |O(1)|
|del key|删除 key-value|O(1)|
|incr|key 自增 1，如果 key 不存在，自增后get(key) = 1|O(1)|
|decr|key 自减 1，如果 key 不存在，自增后get(key) = -1|O(1)|
|incrby key k|key 自增 k，如果 key 不存在，自增后get(key) = k|O(1)|
|incrbyfloat key f|增加 key 对应的值 f，返回修改之后的值 |O(1)|
|decrby key k|key 自减 k， 如果 key 不存在，自增后get(key) = -k|O(1)|
|mset key1 value1 [keyN valueN ...]|批量设置 key-value 。mset是一个原子性(atomic)操作， 所有给定键都会在同一时间内被设置， 不会出现某些键被设置了但是另一些键没有被设置的情况。|O(N)|
|msetnx key1 value1 [keyN valueN ...]|批量设置 key-value 。msetnx是一个原子性(atomic)操作， 所有给定键要么就全部都被设置， 要么就全部都不设置， 不可能出现第三种状态。|O(N)|
|mget key1 [keyN ...]|批量获取 key。如果给定的字符串键里面， 有某个键不存在， 那么这个键的值将以特殊值 nil 表示。|O(N)|
|append key value|将 value 追加到旧的 value 。如果 key 不存在， append 就简单地将键 key 的值设为 value ， 就像执行 SET key value 一样。追加 value 之后， 返回键 key 的值的当前长度。|O(1)|
|strlen key|返回字符串的长度（注意utf-8的中文占用 3 个字符）|O(1)|
|setrange key index value|设置指定下标所有对应的值，返回被修改之后， 字符串值的长度。 |O(1)|
|getrange key start end|获取字符串指定下标所有的值 |O(1)|


#### Hash
| 命令    | 说明               | 时间复杂度 |
| ------- | ------------------ | ---------- |
|hset key field value |设置 hash key 对应的 field 的 value。当 hset命令在 hash 中新创建 field 域并成功为它设置值时， 命令返回 1 ； 如果域 field 已经存在于 hash， 并且 hset 命令成功使用新值覆盖了它的旧值， 那么命令返回 0 。 |O(1)|
|hsetnx key field value|设置 has key 对应的 field 的 value。如果给定域已经存在，则放弃执行设置操作，并返回 0 。|O(1)|
|hget key field |获取 hash key 对应 field 的 value 。 |O(1)|
|hexists key field |判断 hash key 是否有 field 。HEXISTS 命令在给定域存在时返回 1 ， 在给定域不存在时返回 0 。|O(1)|
|hlen key |获取 hash key field 的数量 |O(1)|
|hstrlen key field |返回hash key 中， 与给定域 field 相关联的值的字符串长度。 |O(1)|
|hmset key field1 value1 [fieldN valueN ...]|批量设置 hash key 的一批 field value |O(N)|
|hmget key field1 [fieldN ...]|批量获取 hash key 的一批 field 对应的值|O(N)|
|hgetall key|返回 hash key 对应所有的 field 和 value。**小心使用 hgetall（牢记单线程）**|O(N)|
|hkeys key |返回 hash key 对应所有的 field |O(N)|
|hvals key|返回 hash key 对应所有的 field 的 value|O(N)|
|hincrby key field increment|hash key 对应的 field 的 value 自增 increment。增量也可以为负数，相当于对给定域进行减法操作。如果 key 不存在，一个新的hash被创建并执行 hincrby命令。如果域 field 不存在，那么在执行命令前，域的值被初始化为 0 。对一个储存字符串值的域 field 执行 hincrby命令将造成一个错误。返回值为执行命令后，hash key 中域 field 的值。|O(1)|
|hincrbyfloat key field increment |浮点数版本 |O(1)|
|hdel key field [field ...]|删除hash key 中的一个或多个指定域，不存在的域将被忽略。返回值为被成功移除的域的数量，不包括被忽略的域。|O(N)|

#### List
**特点：**
1. 有序
2. 可以重复
3. 左右两边插入弹出
1. LRUSH + LPOP = Stack
2. LPUSH + RPOP = Queue
3. LPUSH + LTRIM = Capped Collection 	固定大小
4. LPUSH + BRPOP = Message  Queue	  消息队列

| 命令    | 说明               | 时间复杂度 |
| ------- | ------------------ | ---------- |
|lpush key value [value …]|将一个或多个值 value 插入到列表 key 的表头，即左边。原子操作。返回值为执行 lpush 命令后，列表的长度。|O(1)|
|lpushx key value|将值 value 插入到列表 key 的表头，当且仅当 key 存在并且是一个列表。和 lpush key value [value …] 命令相反，当 key 不存在时， lpushx 命令什么也不做。lpushx 命令执行之后，列表的长度。|O(1)|
|rpush key value [value …]|将一个或多个值 value 插入到列表 key 的表尾，即右边。原子操作。返回值为执行 lpush 命令后，列表的长度。|O(1)|
|rpushx key value|将值 value 插入到列表 key 的表尾，当且仅当 key 存在并且是一个列表。和 rpush key value [value …] 命令相反，当 key 不存在时， rpushx 命令什么也不做。rpushx 命令执行之后，列表的长度。|O(1)|
|lpop key|移除并返回列表 key 的头元素。返回值为列表的头元素， 当 key 不存在时，返回 nil 。|O(1)|
|rpop key|移除并返回列表 key 的尾元素。返回值为列表的尾元素。 当 key 不存在时，返回 nil 。|O(1)|
|rpoplpush source destination|在一个原子时间内，执行以下两个动作：1. 将列表 source 中的最后一个元素(尾元素)弹出，并返回给客户端。2. 将 source 弹出的元素插入到列表 destination ，作为 destination 列表的的头元素。如果 source 不存在，值 nil 被返回，并且不执行其他动作。如果 source 和 destination 相同，则列表中的表尾元素被移动到表头，并返回该元素，可以把这种特殊情况视作列表的**旋转(rotation)**操作。|O(1)|
|lrem key count value|根据参数 count 的值，移除列表中与参数 value 相等的元素。count 的值可以是以下三种之一：1. count > 0 : 从表头开始向表尾搜索，移除与 value 相等的元素，数量为 count 。2. count < 0 : 从表尾开始向表头搜索，移除与 value 相等的元素，数量为 count 的绝对值。3. count = 0 : 移除表中所有与 value 相等的值。返回值为被移除元素的数量。|O(N)|
|llen key|返回列表 key 的长度。|O(1)|
|lindex key index|返回列表 key 中，下标为 index 的元素。|O(N)，N 为到达下标 index 过程中经过的元素数量。|
|linsert key `before|after` pivot value |将值 value 插入到列表 key 当中，位于值 pivot 之前或之后。当 pivot 不存在于列表 key 时，不执行任何操作。|O(N)， N 为寻找 pivot 过程中经过的元素数量。|
|lset key index value|将列表 key 下标为 index 的元素的值设置为 value 。|O(N)|
|lrange key start stop|返回列表 key 中指定区间内的元素，区间以偏移量 start 和 stop 指定。超出范围的下标值不会引起错误。如果 start 下标比列表的最大下标 end ( LLEN list 减去 1 )还要大，那么 LRANGE 返回一个空列表。如果 stop 下标比 end 下标还要大，Redis将 stop 的值设置为 end 。|O(S+N)， S 为偏移量 start ， N 为指定区间内元素的数量。|
|ltrim key start stop|对一个列表进行修剪(trim)，就是说，让列表只保留指定区间内的元素，不在指定区间之内的元素都将被删除。超出范围的下标值不会引起错误。如果 start 下标比列表的最大下标 end ( LLEN list 减去 1 )还要大，或者 start > stop ， LTRIM 返回一个空列表(因为 LTRIM 已经将整个列表清空)。如果 stop 下标比 end 下标还要大，Redis将 stop 的值设置为 end 。命令执行成功时，返回OK|O(N)|
|blpop key [key ...] timeout|blpop 是列表的阻塞式(blocking)弹出原语。它是 lpop key 命令的阻塞版本，当给定列表内没有任何元素可供弹出的时候，连接将被 blpop 命令阻塞，直到等待超时或发现可弹出元素为止。当给定多个 key 参数时，按参数 key 的先后顺序依次检查各个列表，弹出第一个非空列表的头元素。超时参数 timeout 接受一个以秒为单位的数字作为值。超时参数设为 0 表示阻塞时间可以无限期延长(block indefinitely) 。如果列表为空，返回一个 nil 。 否则，返回一个含有两个元素的列表，第一个元素是被弹出元素所属的 key ，第二个元素是被弹出元素的值。|O(1)|
|brpop key [key ...] timeout|brpop 是列表的阻塞式(blocking)弹出原语。它是 rpop key 命令的阻塞版本，当给定列表内没有任何元素可供弹出的时候，连接将被 brpop 命令阻塞，直到等待超时或发现可弹出元素为止。当给定多个 key 参数时，按参数 key 的先后顺序依次检查各个列表，弹出第一个非空列表的尾元素。假如在指定时间内没有任何元素被弹出，则返回一个 nil 和等待时长。 反之，返回一个含有两个元素的列表，第一个元素是被弹出元素所属的 key ，第二个元素是被弹出元素的值。|O(1)|
|brpoplpush source destination timeout|brpoplpush 是 rpoplpush source destination 的阻塞版本，当给定列表 source 不为空时， brpoplpush 的表现和 rpoplpush source destination 一样。假如在指定时间内没有任何元素被弹出，则返回一个 nil 和等待时长。 反之，返回一个含有两个元素的列表，第一个元素是被弹出元素的值，第二个元素是等待时长。|O(1)|

#### Set
Redis 的 Set 是 String 类型的无序集合。集合成员是唯一的，这就意味着集合中不能出现
重复的数据。Redis 中集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。
**特点：**
1. 无序
2. 无重复
3. 集合间操作

###### 集合内操作
| 命令    | 说明               | 时间复杂度 |
| ------- | ------------------ | ---------- |
|sadd key member [member …]|将一个或多个 member 元素加入到集合 key 当中，已经存在于集合的 member 元素将被忽略。假如 key 不存在，则创建一个只包含 member 元素作成员的集合。返回值为被添加到集合中的新元素的数量，不包括被忽略的元素。|O(N)|
|srem key member [member …]|移除集合 key 中的一个或多个 member 元素，不存在的 member 元素会被忽略。 |O(N)|
|scard key |返回集合 key 的基数(集合中元素的数量)。 |O(1)|
|sismember key member |判断 member 元素是否集合 key 的成员。 |O(1)|
|srandmember key [count] |返回集合中的 count 个随机元素。count 为可选参数，默认为1。如果 count 为正数，且小于集合基数，那么命令返回一个包含 count 个元素的数组，数组中的元素**各不相同**。如果 count 大于等于集合基数，那么返回整个集合。如果 count 为负数，那么命令返回一个数组，数组中的元素**可能会重复出现多次**，而数组的长度为 count 的绝对值。|O(1)|
|spop key |移除并返回集合中的一个随机元素。 |O(1)|
|smembers key |返回集合 key 中的所有成员。 |O(1)|

###### 集合间操作
| 命令    | 说明               | 时间复杂度 |
| ------- | ------------------ | ---------- |
|sinter key [key …]|返回一个集合的全部成员，该集合是所有给定集合的交集。不存在的 key 被视为空集。当给定集合当中有一个空集时，结果也为空集(根据集合运算定律)。 |O(N * M)， N 为给定集合当中基数最小的集合， M 为给定集合的个数。|
|sunion key [key …] |返回一个集合的全部成员，该集合是所有给定集合的并集。 |O(N)|
|sdiff key [key …]|返回一个集合的全部成员，该集合是所有给定集合之间的差集。 |O(N)|
|sinter/sunion/sdiff + store destination|将交集、并集、差集将结果保存到 destination 集合，而不是简单地返回结果集。如果 destination 集合已经存在，则将其覆盖。destination 可以是 key 本身。返回值为结果集中的成员数量。|时间复杂度同前指令|
|smove source destination member|将 member 元素从 source 集合移动到 destination 集合。原子操作。如果 source 集合不存在或不包含指定的 member 元素，则 SMOVE 命令不执行任何操作，仅返回 0 。否则， member 元素从 source 集合中被移除，并添加到 destination 集合中去，返回 1 。当 destination 集合已经包含 member 元素时， SMOVE 命令只是简单地将 source 集合中的 member 元素删除，返回 1 。|O(1)|

#### Sorted set
| 命令    | 说明               | 时间复杂度 |
| ------- | ------------------ | ---------- |
|zadd key score member `[[score member][score member] ...]`|将一个或多个 member 元素及其 score 值加入到有序集 key 当中。如果某个 member 已经是有序集的成员，那么更新这个 member 的 score 值，并通过重新插入这个 member 元素，来保证该 member 在正确的位置上。score 值可以是整数值或双精度浮点数。返回值为被成功添加的新成员的数量，不包括那些被更新的、已经存在的成员。|O(M * log(N))， N 是有序集的基数， M 为成功添加的新成员的数量。|
|zscore key member|返回有序集 key 中，成员 member 的 score 值。如果 member 元素不是有序集 key 的成员，或 key 不存在，返回 nil 。|O(1)|
|zincrby key increment member|为有序集 key 的成员 member 的 score 值加上增量 increment 。可以通过传递一个负数值 increment ，让 score 减去相应的值。当 key 不存在，或 member 不是 key 的成员时， zincrby key increment member 等同于 zadd key increment member 。返回值为member 成员的新 score 值，以字符串形式表示。|O(log(N))|
|zcard key|返回有序集 key 的基数。|O(1)|
|zrange key start stop [withscores]|返回有序集 key 中，指定区间内的成员。其中成员的位置按 score 值递增(从小到大)来排序。具有相同 score 值的成员按字典**顺序**来排列。可以通过使用 withscores 选项，来让成员和它的 score 值一并返回。|O(log(N)+M)， N 为有序集的基数，而 M 为结果集的基数。|
|zrevrange key start stop [withscores]|返回有序集 key 中，指定区间内的成员。其中成员的位置按 score 值递减(从大到小)来排列。 具有相同 score 值的成员按字典**逆序**排列。返回值为指定区间内，带有 score 值(可选)的有序集成员的列表。|O(log(N)+M)|
|zrangebyscore key min max `[withscores] [limit offset count]`|返回有序集 key 中，所有 score 值介于 min 和 max 之间(包括等于 min 或 max )的成员。有序集成员按 score 值递增(从小到大)次序排列。具有相同 score 值的成员按字典**顺序**来排列。可选的 LIMIT 参数指定返回结果的数量及区间(就像SQL中的 LIMIT offset, count )，注意当 offset 很大时，定位 offset 的操作可能需要遍历整个有序集，此过程最坏复杂度为 O(N) 时间。min 和 max 可以是 `-inf` 和 `+inf` ，这样一来，你就可以在不知道有序集的最低和最高 score 值的情况下，使用 ZRANGEBYSCORE 这类命令。默认情况下，区间的取值使用闭区间 (小于等于或大于等于)，你也可以通过给参数前增加` (` 符号来使用可选的开区间 (小于或大于)。|O(log(N)+M)|
|zrevrangebyscore key max min `[withscores] [limit offset count]`|返回有序集 key 中，所有 score 值介于 max 和 min 之间(包括等于 max 或 min )的成员。有序集成员按 score 值递增(从大到小)次序排列。具有相同 score 值的成员按字典**逆序**来排列。|O(log(N)+M)|
|zcount key min max|返回有序集 key 中， score 值在 min 和 max 之间(默认包括 score 值等于 min 或 max )的成员的数量。| O(log(N))|
|zrank key member|返回有序集 key 中成员 member 的排名。其中有序集成员按 score 值递增(从小到大)顺序排列，因此排名以 0 为底，也就是说， score 值最小的成员排名为 0 。如果 member 不是有序集 key 的成员，返回 nil 。|O(log(N))|
|zrevrank key member|返回有序集 key 中成员 member 的排名。其中有序集成员按 score 值递减(从大到小)排序，因此排名以 0 为底，也就是说， score 值最大的成员排名为 0 。| O(log(N))|
|zrem key member [member …]|移除有序集 key 中的一个或多个成员，不存在的成员将被忽略。返回值为被成功移除的成员的数量，不包括被忽略的成员。返回值为被成功移除的成员的数量，不包括被忽略的成员。|O(M * log(N))，N 为有序集的基数，而 M 为被移除成员的数量。|
|zremrangebyrank key start stop|移除有序集 key 中，指定排名(rank)区间内的所有成员。|O(log(N)+M)|
|zremrangebyscore key min max|移除有序集 key 中，所有 score 值介于 min 和 max 之间(包括等于 min 或 max )的成员。|O(log(N)+M)|
|zrangebylex key min max [limit offset count]|当有序集合的所有成员都具有相同的分值时， 有序集合的元素会根据成员的字典顺序来进行排序， 而这个命令则可以返回给定的有序集合键 key 中， 值介于 min 和 max 之间的成员。合法的 min 和 max 参数必须包含 ( 或者 [ ， 其中 ( 表示开区间， 而 [ 则表示闭区间。特殊值 + 和 - 在 min 参数以及 max 参数中具有特殊的意义， 其中 + 表示正无限， 而 - 表示负无限。|O(log(N)+M)， 其中 N 为有序集合的元素数量， 而 M 则是命令返回的元素数量。 |
|zlexcount key min max|对于一个所有成员的分值都相同的有序集合键 key 来说， 这个命令会返回该集合中， 成员介于 min 和 max 范围内的元素数量。|O(log(N))|
|zremrangebylex key min max|对于一个所有成员的分值都相同的有序集合键 key 来说， 这个命令会移除该集合中， 成员介于 min 和 max 范围内的所有元素。返回值为被移除的元素数量。|O(log(N)+M)|
|zunionstore destination numkeys key `[key …] [weights weight [weight …]] [aggregate sum|min|max]`|计算给定的一个或多个有序集的并集，其中给定 key 的数量必须以 numkeys 参数指定，并将该并集(结果集)储存到 destination 。默认情况下，结果集中某个成员的 score 值是所有给定集下该成员 score 值之 和 。使用 weights 选项，你可以为 每个 给定有序集 分别 指定一个乘法因子(multiplication factor)，每个给定有序集的所有成员的 score 值在传递给聚合函数(aggregation function)之前都要先乘以该有序集的因子。如果没有指定 weights 选项，乘法因子默认设置为 1 。使用 aggregate 选项，你可以指定并集的结果集的聚合方式。默认使用的参数 sum ，可以将所有集合中某个成员的 score 值之 和 作为结果集中该成员的 score 值；使用参数 min ，可以将所有集合中某个成员的 最小 score 值作为结果集中该成员的 score 值；而参数 max 则是将所有集合中某个成员的 最大 score 值作为结果集中该成员的 score 值。返回值为保存到 destination 的结果集的基数。|O(N)+O(M * log(M))， N 为给定有序集基数的总和， M 为结果集的基数。|
|zinterstore destination numkeys `key [key …] [weights weight [weight …]] [aggregate sum|min|max]`|计算给定的一个或多个有序集的交集，其中给定 key 的数量必须以 numkeys 参数指定，并将该交集(结果集)储存到 destination 。默认情况下，结果集中某个成员的 score 值是所有给定集下该成员 score 值之和。返回值为保存到destination 的结果集的基数。|O(N * K)+O(M * log(M))， N 为给定 key 中基数最小的有序集， K 为给定有序集的数量， M 为结果集的基数。|

>Redis Sorted Sets are, similarly to Redis Sets, non repeating collections of Strings. The difference is that every member of a Sorted Set is associated with score, that is used in order to take the sorted set ordered, from the smallest to the greatest score. While members are 
unique, scores may be repeated.

有序集合与集合一样，也是String类型元素的集合，且不允许重复的成员。不同之处在于，有序集合中的每一个成员都与分数相关，Redis 正是通过分数来为集合中的成员进行从小到大的排序成员是独一无二的，然而评分可能重复。

>With sorted sets you can add, remove, or update elements in a very fast way (in a time proportional to the logarithm of the number of elements). Since elements are *taken in order* and not ordered afterwards, you can also get ranges by score or by rank (position) in a very fast way. Accessing the middle of a sorted set is also very fast, so you can use Sorted Sets as a smart list of non repeating elements where you can quickly access everything you need: elements in order, fast existence test, fast access to elements in the middle!

使用有序集合，你能以非常快速的方式添加，删除或者更新元素（时间与元素数量的对数成比例）。由于元素按顺序排列，而不是之后排列，所以您也可以很快地按分数或按等级（位置）获得范围。访问有序集合的中间也是非常快的，所以你能使用有序集合作为一个元素不重复的智能列表当你快速的访问任何你需要的东西：排序元素，快速存在测试，快速访问中间的元素。

>In short with sorted sets you can do a lot of tasks with great performance that are really hard to model in other kind of databases.

总之，使用有序集合，你能执行许多具有出色表现的任务，而这在其他类型的数据库中很难复制。

>With Sorted Sets you can:
>
>- Take a leader board in a massive online game, where every time a new score is submitted you update it using [ZADD](https://redis.io/commands/zadd). You can easily take the top users using [ZRANGE](https://redis.io/commands/zrange), you can also, given an user name, return its rank in the listing using [ZRANK](https://redis.io/commands/zrank). Using ZRANK and ZRANGE together you can show users with a score similar to a given user. All very *quickly*.

在大型在线游戏中占据领先地位，当每次提交新分数时，您都可以使用ZADD进行更新。您可以轻松地使用ZRANGE吸引顶级用户，您也可以使用ZRANK在给定用户名的情况下返回其在列表中的排名。同时使用ZRANK和ZRANGE可以向用户显示与给定用户类似的分数。一切都非常快。

>- Sorted Sets are often used in order to index data that is stored inside Redis. For instance if you have many hashes representing users, you can use a sorted set with elements having the age of the user as the score and the ID of the user as the value. So using [ZRANGEBYSCORE](https://redis.io/commands/zrangebyscore) it will be trivial and fast to retrieve all the users with a given interval of ages.

有序集合通常用于对索引存储在Redis中的数据排序。例如，如果您有许多代表用户的哈希值，则可以使用具有用户年龄的元素作为分数的排序集，用户的ID作为值。因此，使用ZRANGEBYSCORE，以给定的年龄间隔检索所有用户将是微不足道的。

## 事务

#### MULTI & EXEC（原子执行，并非互斥）

| 命令    | 说明               | 时间复杂度 |
| ------- | ------------------ | ---------- |
|MULTI|标记一个事务块的开始。事务块内的多条命令会按照先后顺序被放进一个队列当中，最后由 EXEC 命令原子性(atomic)地执行。总是返回 OK 。|O(1)。|
|EXEC|执行所有事务块内的命令。假如某个(或某些) key 正处于 WATCH 命令的监视之下，且事务块中有和这个(或这些) key 相关的命令，那么 EXEC 命令只在这个(或这些) key 没有被其他命令所改动的情况下执行并生效，否则该事务被打断(abort)。事务块内所有命令的返回值，按命令执行的先后顺序排列。当操作被打断时，返回空值 nil 。|事务块内所有命令的时间复杂度的总和。|

基本事务只需要 `MULTI` 和 `EXEC` 命令，这种事务可以让一个客户端在不被其他客户端打断的
情况下执行多个命令。被 `multi` 和 `exec` 命令包围的所有命令会一个接一个地执行，直到所
有命令都执行完毕为止。（注意，是原子执行，但其他客户端仍可能会修改正在操作的数据）
在输入命令时如果中间有一个命令有语法错误（类似于编译时异常），那么该命令及其之后
的命令都不会被执行，之前的命令会被执行。

#### WATCH & UNWATCH（原子执行 + 乐观锁）

在事务开启前 `watch` 了某个 key，在事务提交时会检查 key 的值与 watch 的时候其值是否发
生变化，如果发生变化，那么事务的命令队列不会被执行。

如果使用 `unwatch` 命令，那么之前的对所有 key 的监控一律取消，哪怕之前检测到 watch
的 key 的值发生变化，也不会对之后的事务产生影响。

#### 分布式锁
`watch & multi & exec `并不是一个好的主意，因为可能会不断循环重试，在竞争激烈时性能很差。

为了确保分布式锁可用吗，且具有**可靠性**，我们至少要确保锁的实现同时满足以下四个条件：

1. **互斥性。**在任意时刻，只有一个客户端能持有锁。
2. **不会发生死锁。**即使有一个客户端在持有锁的期间崩溃而没有主动解锁，也能保证后续其他客户端能加锁。
3. **具有容错性。**只要大部分的`Redis`节点正常运行，客户端就可以加锁和解锁。
4. **解铃还须系铃人。**加锁和解锁必须是同一个客户端，客户端自己不能把别人加的锁给解了。

###### 加锁代码

```Java
package hao.redis.utils;

import redis.clients.jedis.Jedis;

/**
 * Created by hao hao on 2019/8/8 0008.
 */


public class RedisTool {

    private static final String LOCK_SUCCESS = "ok";
    private static final String SET_IF_NOT_EXIST = "NX";
    private static final String SET_WITH_EXPIRE_TIME = "PX";

    /** 
     * 尝试获取分布式锁
     * @param jedis Redis客户端
     * @param lockKey 锁
     * @param requestId 请求标识
     * @param expireTime 超期时间
     * @return 是否获取成功
     */
    public static boolean tryGetDistributedLock(Jedis jedis, String lockKey,String requestId, int expireTime) {
        String result = jedis.set(lockKey, requestId, SET_IF_NOT_EXIST,SET_WITH_EXPIRE_TIME, expireTime);

        if (LOCK_SUCCESS.equals(result)) {
            return true;
        }
        return false;

    }
}

```

方法`jedis.set(String key, String value, String nxxx, String expx, int time)`一共有五个形参：

- 第一个为 key ，我们使用 key 来当锁，因为 key 是唯一的。
- 第二个为 value ，我们传的是 requestId ，很多童鞋可能不明白，有 key 作为锁不就够了吗，为什么还要用到 value ？原因就是我们在上面讲到可靠性时，分布式锁要满足第四个条件**解铃还须系铃人**，通过给 value 赋值为 requestId ，我们就知道这把锁是哪个请求加的了，在解锁的时候就可以有依据。 requestId 可以使用 UUID.randomUUID().toString() 方法生成。
- 第三个为 nxxx ，这个参数我们填的是 NX ，意思是 SET IF NOT EXIST ，即当 key 不存在时，我们进行set操作；若key已经存在，则不做任何操作；
- 第四个为 expx ，这个参数我们传的是 PX ，意思是我们要给这个 key 加一个过期的设置，具体时间由第五个参数决定。
- 第五个为 time ，与第四个参数相呼应，代表 key 的过期时间。

总的来说，执行上面的set()方法就只会导致两种结果：

1.  当前没有锁（key不存在），那么就进行加锁操作，并对锁设置个有效期，同时value表示加锁的客户端。 
2.  已有锁存在，不做任何操作。

在此加锁代码满足我们**可靠性**里描述的三个条件：

1. 首先，set()加入了 NX 参数，可以保证如果已有 key 存在，则函数不会调用成功，也就是只有一个客户端能持有锁，满足**互斥性**。

2. 其次，由于我们对锁设置了过期时间，即使锁的持有者后续发生崩溃而没有解锁，锁也会因为到了过期时间而自动解锁（即 key 被删除），**不会发生死锁**。
3. 最后，因为我们将value赋值为 requestId ，代表加锁的客户端请求标识，那么在客户端在解锁的时候就可以进行校验是否是**同一个客户端**。
4. 由于我们只考虑 Redis 单机部署的场景，所以**容错性**我们暂不考虑。

###### 加锁错误示例1

比较常见的错误示例就是使用`jedis.setnx()`和`jedis.expire()`组合实现加锁，代码如下：

```Java
public static void wrongGetLock1(Jedis jedis, String lockKey, String requestId, int expireTime) {

        Long result = jedis.setnx(lockKey, requestId);
        if (result == 1) {
            // 若在这里程序突然崩溃，则无法设置过期时间，将发生死锁
            jedis.expire(lockKey, expireTime);
        }

    }
```

setnx() 方法作用就是`SET IF NOT EXIST`，expire() 方法就是给锁加一个过期时间。乍一看好像和前面的 set() 方法结果一样，然而由于这是两条Redis命令，**不具有原子性**，如果程序在执行完 setnx() 之后突然崩溃，导致锁没有设置过期时间。那么将会发生死锁。网上之所以有人这样实现，是因为**低版本的jedis并不支持多参数的set()方法。**

###### 加锁错误示例2

这一种错误示例就比较难以发现问题，而且实现也比较复杂。实现思路：使用`jedis.setnx()`命令实现加锁，其中 key 是锁，value 是锁的过期时间。执行过程：1. 通过 setnx() 方法尝试加锁，如果当前锁不存在，返回加锁成功。2. 如果锁已经存在则获取锁的过期时间，和当前时间比较，如果锁已经过期，则设置新的过期时间，返回加锁成功。代码如下：

```Java
public static boolean wrongGetLock2(Jedis jedis, String lockKey, int expireTime) {

        long expires = System.currentTimeMillis() + expireTime;
        String expiresStr = String.valueOf(expires);

        // 如果当前锁不存在，返回加锁成功
        if (jedis.setnx(lockKey, expiresStr) == 1) {
            return true;
        }

        // 如果锁存在，获取锁的过期时间
        String currentValueStr = jedis.get(lockKey);
        if (currentValueStr != null && Long.parseLong(currentValueStr) < System.currentTimeMillis()) {
            // 锁已过期，获取上一个锁的过期时间，并设置现在锁的过期时间
            String oldValueStr = jedis.getSet(lockKey, expiresStr);
            if (oldValueStr != null && oldValueStr.equals(currentValueStr)) {
                // 考虑多线程并发的情况，只有一个线程的设置值和当前值相同，它才有权利加锁
                return true;
            }
        }

        // 其他情况，一律返回加锁失败
        return false;

    }
```

那么这段代码问题在哪里？
1. 由于是客户端自己生成过期时间，所以需要强制要求分布式下每个客户端的时间必须同步。
2. 当锁过期的时候，如果多个客户端同时执行`jedis.getSet()`方法，那么虽然最终只有一个客户端可以加锁，但是这个客户端的锁的过期时间可能被其他客户端覆盖。
3. 锁**不具备拥有者标识**，即任何客户端都可以解锁。

#### 解锁代码

```Java
private static final Long RELEASE_SUCCESS = 1L;

    /**
     * 释放分布式锁
     * @param jedis Redis客户端
     * @param lockKey 锁
     * @param requestId 请求标识
     * @return 是否释放成功
     */
    public static boolean releaseDistributedLock(Jedis jedis, String lockKey, String requestId) {

		//Lua脚本代码，首先获取锁对应的value值，检查是否与requestId相等，如果相等则删除锁（解锁）。
		//为什么要使用Lua语言来实现呢？因为要确保上述操作是原子性的。
        String script = "if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end";
        //将Lua代码传到jedis.eval()方法里，并使参数KEYS[1]赋值为lockKey，ARGV[1]赋值为requestId。eval()方法是将Lua代码交给Redis服务端执行。
        //jedis.eval(java.lang.String script, java.util.List<java.lang.String> keys, java.util.List<java.lang.String> args)
        Object result = jedis.eval(script, Collections.singletonList(lockKey), Collections.singletonList(requestId));

        if (RELEASE_SUCCESS.equals(result)) {
            return true;
        }
        return false;

    }
```

为什么执行eval()方法可以确保原子性，源于Redis的特性，官网对eval命令的部分解释是在eval命令执行Lua代码的时候，Lua代码将被当成一个命令去执行，并且直到eval命令执行完成，Redis才会执行其他命令。

###### 错误示例1

最常见的解锁代码就是直接使用 jedis.del() 方法删除锁，这种不先判断锁的拥有者而直接解锁的方式，会导致任何客户端都可以随时进行解锁，即使这把锁不是它的。

```Java
public static void wrongReleaseLock1(Jedis jedis, String lockKey) {
        jedis.del(lockKey);
    }
```

###### 错误示例2

这种解锁代码乍一看也是没问题，甚至我之前也差点这样实现，与正确姿势差不多，唯一区别的是分成两条命令去执行，代码如下：

```Java
public static void wrongReleaseLock2(Jedis jedis, String lockKey, String requestId) {

        // 判断加锁与解锁是不是同一个客户端
        if (requestId.equals(jedis.get(lockKey))) {
            // 若在此时，这把锁突然不是这个客户端的，则会误解锁
            jedis.del(lockKey);
        }

    }
```

如代码注释，问题在于如果调用 jedis.del() 方法的时候，这把锁已经不属于当前客户端的时候会解除他人加的锁。那么是否真的有这种场景？答案是肯定的，比如客户端A加锁，一段时间之后客户端A解锁，在执行 jedis.del() 之前，锁突然过期了，此时客户端B尝试加锁成功，然后客户端A再执行del()方法，则将客户端B的锁给解除了。

