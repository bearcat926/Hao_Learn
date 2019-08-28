# 第一部分 Hadoop基础知识


## 第1章 初识 Hadoop

Hadoop 为我们提供了一个可靠的且可扩展的存储和分析平台。此外，由于 Hadoop 运行在商用软件上且是开源的，因而可以说 Hadoop 的使用成本是在可承受范围内的。

要对多个硬盘中的数据并行进行读写数据，有两个问题要解决：
1. 硬件故障问题。
解决方式：复制（replication）-> 系统保存数据的复本（replica） ，一旦有系统发生鼓掌，就可以使用另外保存的复本。冗余硬盘阵列（RAID）就是按这个原理实现的。

2. 大多数分析任务需要以某种方式结合大部分数据来共同完成分析，各种分布式系统允许结合不同来源的数据进行分析，但保证其正确性是一个非常大的挑战。MapReduce 提出一个编程模型，抽象出这些硬盘读写问题并将其转换为对一个数据集的计算。

MapReduce 是一个批量查询处理器，能够在合理的时间范围内处理针对整个数据集的动态查询。从 MapReduce 的所有长处来看，它基本上是一个批处理系统，并不适合交互式分析，更适合离线使用场景。

第一个提供在线访问的组件是HBase，一种使用 HDFS 做底层存储的键值存储模型。HBase 不仅提供对单行的在线读写访问，还提供对数据块读写的批处理。

Hadoop 2 中 YARN（Yet Another Resource Negotiator）的出现意味着 Hadoop 有了新处理模型，它是一个集群资源管理系统，允许任何一个分布式程序（不仅仅是 MapReduce）基于 Hadoop 集群的数据而运行。

Interactive SQL（交互式 SQL）：利用 MapReduce 进行分发并使用一个分布式查询引擎，使得在 Hadoop 上获得 SQL 查询低延迟响应的同时还能保持对大数据集规模的可扩展性。

Iterative Processing（迭代处理）：许多算法自身具有迭代性，因此和那种每次迭代都从硬盘加载的方式相比，这种在内存中保存每次中间结果集的方式更加高效。但MapReduce 的架构不允许这样。

Stream Processing（流处理）：流系统，例如 Storm，Spark Streaming 或 Samza 使得在无边界数据流上运行实时、分布式的计算，并向 Hadoop 存储系统或外部系统发布结果成为可能。

Search（搜索）：Solr 搜索平台能够在 Hadoop 集群上运行，当文档加 HDFS 后就可对其进行索引，且根据 HDFS 中存储的索引为搜索查询提供服务。

为什么不能用配有大量硬盘的数据库来进行大规模数据分析？为什么需要Hadoop？
计算机硬盘的发展趋势：寻址时间的提升远远不敌传输速率的提升。寻址是将磁头移动到特定硬盘位置进行读写操作的过程，它导致了硬盘操作的延迟，而传输速率取决于硬盘的带宽。

![1566894063310](E:\git_repo\Hao_Learn\2019\8\img\1566894063310.png)

Hadoop 和关系型数据库的另一个区别在于它们所操作的数据集的结构化程度。

结构化数据（structured data）是具有既定格式的实体化数据，如 XML 文档或满足特定预定义格式的数据库表。这是 RDBMS 包括的内容。

半结构化数据（semi-structured data）比较松散，虽然可能有格式，但经常被忽略，所以它只能作为对数据结构的一般性指导。例如电子表格。

非结构化数据（unstructured data）没有什么特别的内部结构。例如纯文本或图像数据。Hadoop 对非结构化或半结构化数据非常有效，因为他是在处理数据时才对数据进行解释（即所谓的“读时模式”）。这种模式在提供灵活性的同时避免了 RDBMS 数据加载阶段带来的高开销，因为在 Hadoop 中仅仅是一个文件拷贝系统。

关系型数据往往是规范的（normalized），以保持其数据的完整性且不含冗余。规范给 Hadoop 处理带来了问题，因为它使记录读取成为非本地操作，而 Hadoop 的核心假设之一偏偏就是可以进行（高速的）流读写操作。

Web 服务器日志是典型的非规范化数据记录，这也是Hadoop 非常适用于分析各种日志文件的原因之一。注意，Hadoop 也能够做连接（join）操作，只不过这种操作没有在关系型数据库中用的多。

MapReduce 以及 Hadoop 中其他的处理模型是可以随着数据规模线性伸缩的。对数据分区后，函数原语（如 map 和 reduce）能够在各个分区上并行工作。这意味着，如果输入的数据量是原来的两倍，那么作业的运行时间也需要两倍。但如果集群规模扩展为原来的两倍，那么作业的运行速度却仍然与原来一样快。SQL 查询一般不具备该特性。

Hadoop 尽量在计算节点上存储数据，以实现数据的本地快速访问。数据本地化（data locality）特性是 Hadoop 数据处理的核心，并因此而获得良好的性能。意识到网络带宽是数据中心环境最珍贵的资源（到处复制数据很容易耗尽网络带宽）之后，Hadoop 通过显式网络拓扑结构在保留网络带宽，这种排列方式并没有降低 Hadoop 对计算密集型数据进行分析的能力。

MapReduce 有三大设计目标：
1. 为只需要短短几分钟或几个小时就可以完成的作业提供服务；
2. 运行于同一个内部有高速网络连接的数据中心内；
3. 数据中心内的计算机都是可靠的、专门的硬件。

Hadoop 是 Apache Lucene 创始人 Doug Cutting创建的，Lucene 是一个应用广泛的文本搜索系统库。Hadoop 起源于开源网络搜索引擎 Apache Nutch，后者本身也是 Lucene 项目的一部分。

## 第2章 关于MapReduce

MapReduce 是一种可用于数据处理的编程模型。该模型比较简单，但要想要写出有用的程序却不太容易。

MapReduce 程序本质上是并行运行的，因此可以将大规模的数据分析任务分发给任何一个拥有足够多机器的数据中心。

MapReduce 任务过程分为两个处理阶段：map 阶段和 reduce 阶段。每阶段都以键值对作为输入和输出，其类型由程序员来选择。程序员还需要写两个函数：map 函数和 reduce 函数。

#### 使用Hadoop分析数据 - 气象数据集

map函数由 Mapper 类来表示，后者声明一个抽象的 map() 方法。
```Java
import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MaxTemperatureMapper
  extends Mapper<LongWritable, Text, Text, IntWritable> {

  private static final int MISSING = 9999;
  
  @Override
  public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {
    
    String line = value.toString();
    String year = line.substring(15, 19);
    int airTemperature;
    if (line.charAt(87) == '+') { // parseInt doesn't like leading plus signs
      airTemperature = Integer.parseInt(line.substring(88, 92));
    } else {
      airTemperature = Integer.parseInt(line.substring(87, 92));
    }
    String quality = line.substring(92, 93);
    if (airTemperature != MISSING && quality.matches("[01459]")) {
      context.write(new Text(year), new IntWritable(airTemperature));
    }
  }
}
```

Hadoop 本身提供了一套可优化网络序列化传输的基本类型，而不直接使用Java内嵌的类型。这些类型都在 `org.apache.hadoop.io` 包中。LongWritable 相当于Long，Text 相当于String，IntWritable 相当于Integer。

map() 提供了 Context 实例用于输出内容的写入。

reduce 函数由 Reducer 来定义。

```Java
import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MaxTemperatureReducer
  extends Reducer<Text, IntWritable, Text, IntWritable> {
  
  @Override
  public void reduce(Text key, Iterable<IntWritable> values,
      Context context)
      throws IOException, InterruptedException {
    
    int maxValue = Integer.MIN_VALUE;
    for (IntWritable value : values) {
      maxValue = Math.max(maxValue, value.get());
    }
    context.write(key, new IntWritable(maxValue));
  }
}
```

运行 MapReduce 作业：

```Java
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class MaxTemperature {

  public static void main(String[] args) throws Exception {
    if (args.length != 2) {
      System.err.println("Usage: MaxTemperature <input path> <output path>");
      System.exit(-1);
    }

    /**
     * 1. 构建 Job 对象
     * Job 对象指定作业规范。
     * 我们可以用它来控制整个作业的运行。
     * 我们在 Hadoop 集群上运行这个作业时，要把代码打包成一个 JAR 文件。
     * 不必明确指定 JAR 文件的名称，在 Job 对象的 setJarByClass() 方法中传递一个类即可，
     * Hadoop 利用这个类来查找包含它的 JAR 文件，进而找到相关的 JAR 文件。
     */
    Job job = new Job();
    job.setJarByClass(MaxTemperature.class);
    job.setJobName("Max temperature");

    /**
     * 2. 指定输入和输出数据的路径
     * 输入路径可以是单个的文件、一个目录（将该目录下所有文件当做输入）
     * 或符合特定文件模式的一系列文件。
     * 由函数名可知，可多次调用该方法来实现多路径的输入。
     *
     * 输出路径只能有一个，是指定输出文件的写入目录。
     * 在运行作业前，该目录是不应该存在的，否则 Hadoop 会报错并拒绝运行作业。
     * 这种预防措施的目的是防止数据丢失
     */
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));

    /**
     * 3. 指定要用的 map 类型和 reduce 类型
     */
    job.setMapperClass(MaxTemperatureMapper.class);
    job.setReducerClass(MaxTemperatureReducer.class);

    /**
     * 4. 控制 reduce 函数的输出类型，并且必须和 Reduce 类产生的相匹配。
     * map 函数的输出类型默认情况下和 reduce函数是一样的，
     * 但是如果不同，则必须通过job.setMapOutputKeyClass() 和 job.setMapOutputValueClass()
     * 来设置 map 函数的输出类型。
     */
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);

    /**
     * 5. Job 中的 waitForCompletion() 提交作业并等待执行完成。
     * 该方法唯一的参数是一个标识，指示是否已生成详细输出。
     * 当标识为 true（成功）时，作业会把其进度信息写到控制台。
     * 方法返回一个布尔值，被转换成 System.exit() 的参数 0 或者 1。
     */
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
```

运行测试：

```shell
# 运行
hadoop dfs -mkdir -p /root/hadoop
hadoop dfs -mkdir input
hadoop dfs -put /opt/bak/1901/1901.txt input
export HADOOP_CLASSPATH=ch02-mr-intro-4.0.jar
hadoop MaxTemperature input/1901.txt output

# 输出日志
19/08/28 15:06:26 WARN mapred.JobClient: Use GenericOptionsParser for parsing the arguments. Applications should implement Tool for the same.
19/08/28 15:06:26 INFO input.FileInputFormat: Total input paths to process : 1
19/08/28 15:06:26 INFO util.NativeCodeLoader: Loaded the native-hadoop library
19/08/28 15:06:26 WARN snappy.LoadSnappy: Snappy native library not loaded
19/08/28 15:06:27 INFO mapred.JobClient: Running job: job_201908281020_0003
19/08/28 15:06:28 INFO mapred.JobClient:  map 0% reduce 0%
19/08/28 15:06:34 INFO mapred.JobClient:  map 100% reduce 0%
19/08/28 15:06:42 INFO mapred.JobClient:  map 100% reduce 33%
19/08/28 15:06:44 INFO mapred.JobClient:  map 100% reduce 100%
19/08/28 15:06:45 INFO mapred.JobClient: Job complete: job_201908281020_0003
19/08/28 15:06:45 INFO mapred.JobClient: Counters: 29
19/08/28 15:06:45 INFO mapred.JobClient:   Map-Reduce Framework
19/08/28 15:06:45 INFO mapred.JobClient:     Spilled Records=13128
19/08/28 15:06:45 INFO mapred.JobClient:     Map output materialized bytes=72210
19/08/28 15:06:45 INFO mapred.JobClient:     Reduce input records=6564
19/08/28 15:06:45 INFO mapred.JobClient:     Virtual memory (bytes) snapshot=3970043904
19/08/28 15:06:45 INFO mapred.JobClient:     Map input records=6565
19/08/28 15:06:45 INFO mapred.JobClient:     SPLIT_RAW_BYTES=111
19/08/28 15:06:45 INFO mapred.JobClient:     Map output bytes=59076
19/08/28 15:06:45 INFO mapred.JobClient:     Reduce shuffle bytes=72210
19/08/28 15:06:45 INFO mapred.JobClient:     Physical memory (bytes) snapshot=251985920
19/08/28 15:06:45 INFO mapred.JobClient:     Reduce input groups=1
19/08/28 15:06:45 INFO mapred.JobClient:     Combine output records=0
19/08/28 15:06:45 INFO mapred.JobClient:     Reduce output records=1
19/08/28 15:06:45 INFO mapred.JobClient:     Map output records=6564
19/08/28 15:06:45 INFO mapred.JobClient:     Combine input records=0
19/08/28 15:06:45 INFO mapred.JobClient:     CPU time spent (ms)=1040
19/08/28 15:06:45 INFO mapred.JobClient:     Total committed heap usage (bytes)=160501760
19/08/28 15:06:45 INFO mapred.JobClient:   File Input Format Counters 
19/08/28 15:06:45 INFO mapred.JobClient:     Bytes Read=888190
19/08/28 15:06:45 INFO mapred.JobClient:   FileSystemCounters
19/08/28 15:06:45 INFO mapred.JobClient:     HDFS_BYTES_READ=888301
19/08/28 15:06:45 INFO mapred.JobClient:     FILE_BYTES_WRITTEN=255550
19/08/28 15:06:45 INFO mapred.JobClient:     FILE_BYTES_READ=72210
19/08/28 15:06:45 INFO mapred.JobClient:     HDFS_BYTES_WRITTEN=9
19/08/28 15:06:45 INFO mapred.JobClient:   Job Counters 
19/08/28 15:06:45 INFO mapred.JobClient:     Launched map tasks=1
19/08/28 15:06:45 INFO mapred.JobClient:     Launched reduce tasks=1
19/08/28 15:06:45 INFO mapred.JobClient:     SLOTS_MILLIS_REDUCES=9389
19/08/28 15:06:45 INFO mapred.JobClient:     Total time spent by all reduces waiting after reserving slots (ms)=0
19/08/28 15:06:45 INFO mapred.JobClient:     SLOTS_MILLIS_MAPS=6373
19/08/28 15:06:45 INFO mapred.JobClient:     Total time spent by all maps waiting after reserving slots (ms)=0
19/08/28 15:06:45 INFO mapred.JobClient:     Data-local map tasks=1
19/08/28 15:06:45 INFO mapred.JobClient:   File Output Format Counters 
19/08/28 15:06:45 INFO mapred.JobClient:     Bytes Written=9

# 查看结果
hadoop fs -cat /user/root/output/part-r-00000
1901	317
```

#### 操作 HDFS 的基本命令

1. 打印文件列表（ls）

```shell
# 标准写法
    # hdfs: 明确说明是 HDFS 系统路径
    hadoop fs -ls hdfs:/ 

# 简写
    # 默认是 HDFS 系统下的根目录
    hadoop fs -ls / 

#打印指定子目录
    # HDFS 系统下某个目录
    hadoop fs -ls /package/test/ 
```

2. 上传文件、目录（put、copyFromLocal）

```shell
# put 用法

# 上传新文件
    # 上传本地 test.txt 文件到 HDFS 根目录，HDFS根目录须无同名文件，否则“File exists”
    hadoop fs -put file:/root/test.txt hdfs:/ 
    # 上传并重命名文件。
    hadoop fs -put test.txt /test2.txt 
    # 一次上传多个文件到 HDFS 路径。
    hadoop fs -put test1.txt test2.txt hdfs:/ 

# 上传文件夹
    # 上传并重命名了文件夹。
    hadoop fs -put mypkg /newpkg 

# 覆盖上传
    # 如果 HDFS 目录中有同名文件会被覆盖
    hadoop fs -put -f /root/test.txt /

# copyFromLocal 用法

# 上传文件并重命名
hadoop fs -copyFromLocal file:/test.txt hdfs:/test2.txt

# 覆盖上传
hadoop fs -copyFromLocal -f test.txt /test.txt
```

3. 下载文件、目录（get、copyToLocal）

```shell
# get 用法

# 拷贝文件到本地目录
hadoop fs -get hdfs:/test.txt file:/root/

# 拷贝文件并重命名，可以简写
hadoop fs -get /test.txt /root/test.txt
	
# copyToLocal 用法

# 拷贝文件到本地目录
hadoop fs -copyToLocal hdfs:/test.txt file:/root/
# 拷贝文件并重命名，可以简写
hadoop fs -copyToLocal /test.txt /root/test.txt
```

4. 拷贝文件、目录（cp）

```shell
#从本地到 HDFS，同 put
hadoop fs -cp file:/test.txt hdfs:/test2.txt
	
#从 HDFS 到 HDFS
hadoop fs -cp hdfs:/test.txt hdfs:/test2.txt
hadoop fs -cp /test.txt /test2.txt
```

5. 移动文件（mv）

```shell
hadoop fs -mv hdfs:/test.txt hdfs:/dir/test.txt
hadoop fs -mv /test.txt /dir/test.txt
```

6. 删除文件、目录（rm）

```shell
# 删除指定文件
hadoop fs -rm /a.txt
# 删除全部 txt 文件
hadoop fs -rm /*.txt
# 递归删除全部文件和目录
hadoop fs -rm -R /dir/
```

7. 读取文件（cat、tail）

```shell
#以字节码的形式读取
hadoop fs -cat /test.txt 
hadoop fs -tail /test.txt
```

8. 创建空文件（touchz）

```shell
hadoop fs -touchz /newfile.txt
```

9. 创建文件夹（mkdir）

```shell
#可以同时创建多个
hadoop fs -mkdir /newdir /newdir2 
#同时创建父级目录
hadoop fs -mkdir -p /newpkg/newpkg2/newpkg3 
```

10. 获取逻辑空间文件、目录大小（du）

```shell
#显示 HDFS 根目录中各文件和文件夹大小
hadoop fs -du / 
#以最大单位显示 HDFS 根目录中各文件和文件夹大小
hadoop fs -du -h / 
#仅显示 HDFS 根目录大小。即各文件和文件夹大小之和
hadoop fs -du -s / 
```

#### 横向扩展

MapReduce 作业（job） 是客户端需要执行的一个工作单元，它包括：输入数据、MapReduce 程序和配置信息。Hadoop 将作业分成若干个任务（task）来执行，其中包括两类任务：map 任务和 reduce 任务。这些任务运行在集群的节点上，并通过 TARN 进行调度。如果一个任务失败，它将在另一个不同的节点上自动重新调度运行。

Hadoop 将 MapReduce 的输入数据划分成等长的小数据块，成为输入分片（input split）或简称 “分片”。Hadoop 为每个分片构建一个 map 任务，并由该任务来运行用户自定义的 map 函数从而处理分片中的每条记录。

拥有许多分片，意味着处理每个分片所需要的时间少于处理整个输入数据所花的时间。因此，如果我们并行处理每个分片且每个分片数据比较小，则整个处理过程将获得更好的负载平衡。而且随着分片被切分得更细，负载平衡的质量会更高。

如果分片切分得太小，那么管理分片的总时间 

p54