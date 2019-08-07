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
|setex key seconds value|将键 key 的值设置为 value ， 并将键 key 的生存时间设置为 seconds 。如果键 key 已经存在， 那么 setex 命令将覆盖已有的值。setex命令的效果和以下两个命令的效果类似：`SET key value EXPIRE key seconds  # 设置生存时间`</br>**这两个命令的不同之处在于 setex是一个原子（atomic）操作**， 它可以在同一时间内完成设置值和设置过期时间这两个操作， 因此 setex命令在储存缓存的时候非常实用。 |O(1)|
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
List特点：有序，可以重复，左右两边插入弹出
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