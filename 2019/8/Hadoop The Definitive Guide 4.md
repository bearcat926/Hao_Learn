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

#### 横向扩展

为了实现横向扩展（scaling out），我们需要把数据存储在 DFS 中（典型的为 HDFS），通过使用 YARN ，Hadoop 可以将 MapReduce 计算转移到存储有部分数据的各台机器上。

###### 数据流

MapReduce 作业（job） 是客户端需要执行的一个工作单元，它包括：输入数据、MapReduce 程序和配置信息。Hadoop 将作业分成若干个任务（task）来执行，其中包括两类任务：map 任务和 reduce 任务。这些任务运行在集群的节点上，并通过 TARN 进行调度。如果一个任务失败，它将在另一个不同的节点上自动重新调度运行。

Hadoop 将 MapReduce 的输入数据划分成等长的小数据块，成为输入分片（input split）或简称 “分片”。Hadoop 为每个分片构建一个 map 任务，并由该任务来运行用户自定义的 map 函数从而处理分片中的每条记录。

拥有许多分片，意味着处理每个分片所需要的时间少于处理整个输入数据所花的时间。因此，如果我们并行处理每个分片且每个分片数据比较小，则整个处理过程将获得更好的负载平衡。而且随着分片被切分得更细，负载平衡的质量会更高。

如果分片切分得太小，那么管理分片的总时间和构建 map 任务的总时间将决定作业的整个执行时间。对大多数作业来说，一个合理的分片大小趋向于 HDFS 的一个块的大小，默认是 128 MB，不过可以针对集群调整这个默认值，或在每个文件创建时指定。大小相同的原因：他是确保可以存储在单个节点上的最大输入块的大小。如果分片跨越两个数据块，那么对于任何一个 HDFS 节点，基本上都不可能通常是存储这个两个数据块，因此分片中的部分数据需要通过网络传输到 map 任务运行的节点。与使用本地数据运行整个 map 任务相比，这种方法显然效率更低。Hadoop 在存储有输入数据（HDFS 中的数据）的节点上运行 map 任务可以获得最佳性能，因为无需使用宝贵的集群宽带资源，即“数据本地化优化”（data locality optimization）。

![1566998638099](E:\git_repo\Hao_Learn\2019\8\img\1566998638099.png)

map 任务将其输出写入本地硬盘，而非 HDFS 的原因是 map 的输出是中间结果，该中间结果由 reduce 任务处理后再产生最终输出结果，而且一旦作业完成，map 的输出结果就可以删除。因此如果把它存储在 HDFS 中并实现备份，难免有些小题大做。如果运行 map 任务的节点在将 map 中间结果传送给 reduce 任务之前失败，Hadoop 将在另一个节点上重新运行这个 map 任务以再次构建中间结果。

reduce 任务并不具备数据本地化的优势，单个 reduce 任务的输入通常来自于所有 mapper 的输出。

将 reduce 的输出写入 HDFS 确实需要占用网络带宽，但这于正常的 HDFS写入的消耗一样。

![1567059546301](E:\git_repo\Hao_Learn\2019\8\img\1567059546301.png)

reduce 任务的数量并非由输入数据的大小决定，相反是独立指定的。如果有好多个 reduce 任务，每个 map 任务就会针对输出进行分区（partition），即为每个 reduce 任务建一个分区。每个分区有许多键（及其对应的值），但每个键对应的 KV 对记录都在同一分区中。分区可由用户定义的分区函数控制，但通常用默认的 partitioner 通过哈希函数来分区，很高效。

map 任务和 reduce 任务之间的数据流成为 shuffle（混洗），因为每个 reduce 任务的输入都来自许多 map 任务。shuffle 一般比图中所示的更复杂，而且调整混洗参数对作业总执行时间的影响非常大。

![1567059949789](E:\git_repo\Hao_Learn\2019\8\img\1567059949789.png)

最后，当数据处理可以完全并行（即无需混洗时），可能会出现无 reduce 任务的情况。在这种情况下，唯一的非本地节点数据传输是 map 任务将结果写入 HDFS。

![1567060120155](E:\git_repo\Hao_Learn\2019\8\img\1567060120155.png)

###### combiner 函数

集群上的可用带宽限制了 MapReduce 作业的数量，因此尽量避免 map 和 reduce 任务之间的数据传输是有利的。Hadoop 允许用户针对 map 任务的输出指定一个 combiner，其输出作为 reduce 函数的输入。由于 combiner 属于优化方案，所以 Hadoop 无法确定要对一个指定的 map 任务输出记录调用多少次 combiner ，但是不管调用 combiner 多少次，reducer 的输出结果都是一样的。

combiner 的规则制约着可用的函数类型。

combiner 函数不能取代 reduce 函数。因为需要 reduce 函数来处理不同 map 输出中具有相同键的记录。但 combiner 函数能帮助减少 mapper 和 reducer 之间的数据传输量。

```Java
// cc MaxTemperatureWithCombiner Application to find the maximum temperature, using a combiner function for efficiency
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

// vv MaxTemperatureWithCombiner
public class MaxTemperatureWithCombiner {

  public static void main(String[] args) throws Exception {
    if (args.length != 2) {
      System.err.println("Usage: MaxTemperatureWithCombiner <input path> " +
          "<output path>");
      System.exit(-1);
    }
    
    Job job = new Job();
    job.setJarByClass(MaxTemperatureWithCombiner.class);
    job.setJobName("Max temperature");

    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    
    job.setMapperClass(MaxTemperatureMapper.class);
    // combiner 需要通过 Reducer 类来设置job.setCombinerClass()
    job.setCombinerClass(MaxTemperatureReducer.class);
    job.setReducerClass(MaxTemperatureReducer.class);

    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
// ^^ MaxTemperatureWithCombiner
```

这个程序用不着修改便可以在一个完整的数据集上直接运行。这是 MapReduce 的优势：他可以根据数据量的大小和硬件规模进行扩展。

#### Hadoop Streaming

Hadoop Streaming 使用 Unix 标准流作为 Hadoop 和应用程序之间的接口，所以可以使用任何编程语言通过标准输入/输出来写 MapReduce 程序。

Streaming 天生适合用于文本处理。map 的输入数据通过标准输入流传递给 map 函数，并且是一行一行地传输，最后将结果行写到标准输出。map 输出的 KV 对是一个以制表符分割的行，reduce 函数的输入格式与之相同并通过标准输入流进行传输。reduce 函数从标准输入流中读取输入行，该输入已由 Hadoop 框架根据键排过序，最后将结果写入标准输出。

Streaming 和 Java MapReduce API 之间的设计差异：
Java API 控制的 map 函数一次只处理一条记录。针对输入数据中的每一条记录，该框架均需调用 Mapper 的 map() 方法来处理。然而在 Streaming 中，map 程序可以自己决定如何处理输入数据。

旧版 Java MapReduce API 使用“推”记录方式，新版中使用“拉”的方式来处理。

![1567064461868](C:\Users\HAOHAOA\AppData\Roaming\Typora\typora-user-images\1567064461868.png)

## 第3章 HDFS

管理网络中跨多台计算机存储的文件系统成为分布式文件系统（Distributed File System）。该系统架构于网络之上，势必会引入网络编程的复杂性，因此分布式文件系统比普通磁盘文件系统更为复杂。

HDFS 是 Hadoop 的旗舰级文件系统，但实际上 Hadoop 是一个综合性的文件系统抽象。

#### HDFS 的设计

HDFS 以**流式数据访问**（一次写入、多次读取）模式来存储**超大文件**（指具有几百 MB、几百 GB、甚至几百 TB 大小的文件），运行于商用硬件（即普通硬件）集群上。

对于**商用硬件**组成的庞大集群来说，节点故障的几率还是非常高的，但 HDFS 被设计成能够继续运行且不让用户察觉到明显的中断。

HDFS 是为高数据吞吐量应用优化的，这可能会以提高时间延迟为代价，因此**不适合低时间延迟数据访问应用**。

由于 namenode 将文件系统的元数据存储在内存中，因此该文件系统所能存储的文件总数受限于 namenode 的内存容量。根据经验，每个文件、目录和数据块的存储信息大约占 150 字节。因此对于 HDFS **不适用于存储大量的小文件**。

HDFS 中的文件写入只支持单个写入者，而且写操作总是以“只添加”方式在文件末尾写数据。**不支持多个写入者操作，也不支持在文件的任意位置进行修改**。

#### HDFS 的概念

1. 数据块

磁盘块是磁盘进行数据读/写的最小单位，一般为 512B。

构建于单个磁盘之上的文件系统通过磁盘块来管理该文件系统中的块，该文件系统块的大小可以是磁盘块的整数倍，一般为几千字节。

HDFS 的块(block)，默认为 128MB，为什么这么大？目的是为了最小化寻址开销。如果块足够大，从磁盘传输数据的时间会明显大于这个块开始位置所需的时间，即传输一个由多个块组成的大文件的时间取决于磁盘传输速率。

很多情况下 HDFS 安装时使用更大的块，但是这个参数也不会设置的过大。map 任务通常一次只处理一个块中的数据，因此如果任务数少于集群中节点的数量，作业的运行速度就会比较慢。

HDFS 上的文件也被划分为块大小的多个分块（chunk），作为独立的存储单元。

对块进行抽象而带来的好处：

- 一个文件的大小可以大于网络中任意一个磁盘的容量。
- 使用抽象块而非整个文件作为存储单元，大大简化了存储子系统的设计。将存储子系统的处理对象设置为块，可简化存储管理，同时也消除了对文件元数据的顾虑，并不需要与块一同存储，其他系统可以单独管理这些元数据。
- 适合数据备份，进而提供数据容错能力和提高可用性。

与磁盘文件系统相似，HDFS 中 `hadoop fsck`指令可以显示块信息。

```shell
hadoop fsck / -files -blocks

FSCK started by root from /172.16.42.3 for path / at Thu Aug 29 16:22:09 CST 2019
/ <dir>
/opt <dir>
/opt/hadoop-1.2.1 <dir>
/opt/hadoop-1.2.1/tmp <dir>
/opt/hadoop-1.2.1/tmp/mapred <dir>
/opt/hadoop-1.2.1/tmp/mapred/staging <dir>
/opt/hadoop-1.2.1/tmp/mapred/staging/root <dir>
/opt/hadoop-1.2.1/tmp/mapred/staging/root/.staging <dir>
/opt/hadoop-1.2.1/tmp/mapred/staging/root/.staging/job_201908281020_0001 <dir>
/opt/hadoop-1.2.1/tmp/mapred/staging/root/.staging/job_201908281020_0001/job.jar 13115 bytes, 1 block(s):  Under replicated blk_-6130025783369441984_1002. Target Replicas is 10 but found 1 replica(s).
0. blk_-6130025783369441984_1002 len=13115 repl=1

/opt/hadoop-1.2.1/tmp/mapred/staging/root/.staging/job_201908281020_0002 <dir>
/opt/hadoop-1.2.1/tmp/mapred/staging/root/.staging/job_201908281020_0002/job.jar 13115 bytes, 1 block(s):  Under replicated blk_-14591262224782312_1003. Target Replicas is 10 but found 1 replica(s).
0. blk_-14591262224782312_1003 len=13115 repl=1

/opt/hadoop-1.2.1/tmp/mapred/system <dir>
/opt/hadoop-1.2.1/tmp/mapred/system/jobtracker.info 4 bytes, 1 block(s):  OK
0. blk_-3753673992170444692_1015 len=4 repl=1

/root <dir>
/root/hadoop <dir>
/user <dir>
/user/root <dir>
/user/root/-p <dir>
/user/root/input <dir>
/user/root/input/1901.txt 888190 bytes, 1 block(s):  OK
0. blk_-6913416553042151769_1004 len=888190 repl=1

/user/root/output <dir>
/user/root/output/_SUCCESS 0 bytes, 0 block(s):  OK

/user/root/output/_logs <dir>
/user/root/output/_logs/history <dir>
/user/root/output/_logs/history/job_201908281020_0003_1566975986978_root_Max+temperature 13887 bytes, 1 block(s):  OK
0. blk_-6416820537601840496_1014 len=13887 repl=1

/user/root/output/_logs/history/job_201908281020_0003_conf.xml 48513 bytes, 1 block(s):  OK
0. blk_9117670473230446324_1012 len=48513 repl=1

/user/root/output/part-r-00000 9 bytes, 1 block(s):  OK
0. blk_396238703654203438_1013 len=9 repl=1

Status: HEALTHY
 Total size:	976833 B
 Total dirs:	20
 Total files:	8
 Total blocks (validated):	7 (avg. block size 139547 B)
 Minimally replicated blocks:	7 (100.0 %)
 Over-replicated blocks:	0 (0.0 %)
 Under-replicated blocks:	2 (28.571428 %)
 Mis-replicated blocks:		0 (0.0 %)
 Default replication factor:	1
 Average block replication:	1.0
 Corrupt blocks:		0
 Missing replicas:		18 (257.14285 %)
 Number of data-nodes:		1
 Number of racks:		1
FSCK ended at Thu Aug 29 16:22:09 CST 2019 in 3 milliseconds


The filesystem under path '/' is HEALTHY
```

2. namenode 和 datanode

HDFS 集群有两类节点以管理节点-工作节点模式运行，即一个 namenode（管理节点）和多个 datanode（工作节点）。namenode 管理文件系统的命名空间。它维护着文件系统树及整棵树内所有的文件和目录。这些信息以两个文件形式永久保存在本地磁盘上：命名空间镜像文件和编辑日志文件。namenode 也记录着每个文件中各个块所在的数据节点信息，但它并不永久保存块的位置信息，因为这些信息会在系统启动时根据数据节点信息重建。

客户端（client）代表用户通过与 namenode 和 datanode 交互来访问整个文件系统。客户端提供一个类似于 POSIX（可移植操作系统界面）的文件系统接口，使用户在编程时无需知道 namenode 和 datanode 也可以实现其功能。

datanode 使文件系统的工作节点。他们根据需要存储并检索数据库（受客户端或 namenode 调度），并且定期向 namenode 发送它们所存储的块的列表。

如果运行 namenode 服务的机器损坏，文件系统上所有的文件将会丢失，文件系统将无法使用，因为不知道如何根据 datanode 的块重建文件。为了实现 namenode 的容错性，Hadoop提供了两种机制：

- 备份那些组成文件系统元数据持久状态的文件。Hadoop 可以通过配置使 namenode 在多个文件系统上保存元数据的持久状态。这些写操作是实时同步的，且为原子操作。一般的配置是，将持久状态写入本地磁盘的同时，写入一个远程挂载的网络文件系统（NFS）。
- 运行一个辅助 namenode，但它不能被用作 namenode。这个辅助 namenode 的重要作用是定期合并并保存编辑日志与命名空间镜像，以防止编辑日志过大，并且会在 namenode 发生故障时启用。但由于辅助 namenode 保存的状态总是滞后于主节点，所以难免会丢失部分数据。在这种情况下，一般把存储在 NFS 上的 namenode 元数据复制到辅助 namenode 并作为新的主 namenode 运行。 辅助 namenode 一般在另一台单独的物理计算机上运行，因为需要占用大量 CPU 时间，并且需要与 namenode 一样多的内存来执行合并操作。

3. 块缓存

通常 datanode 从磁盘中读取块，但对于访问频繁的文件，其对应的块可能被显式地缓存在datanode 的内存中，以堆外块缓存（off-heap block cache）的形式存在。默认情况下，一个块仅缓存在一个 datanode 的内存中。作业调度器（用于 MapReduce、Spark 和其他框架的）通过在缓存块的 datanode 上运行任务，可以利用块缓存的优势提高读操作的性能。

用户或应用通过在缓存池（cache pool）中增加一个 cache directive 来告诉 namenode 需要缓存哪些文件及存多久。缓存池是一个用于管理缓存权限和资源使用的管理性分组。

4. HDFS 的高可用性

namenode 是唯一存储元数据与文件到数据块映射的地方。

namenode 依旧存在单点失效（SPOF，single point of failure）。

想要从一个失效的 namenode 恢复，新的 namenode 直到满足以下情形才能响应服务：

- 将命名空间的映像导入内存中
- 重演编辑日志
- 接受到足够多的来自 datanode 的数据块报告并退出安全模式

对于一个大型并拥有大量文件和数据块的集群，namenode 的冷启动需要 30 分钟，甚至更长时间，进而影响到日常维护。

事实上，预期外的 namenode 失效出现的概率很低，所以在现实中，计划内的系统失效时间实际更为重要。

Hadoop2 针对上述问题增加了对 HDFS 高可用性（HA）的支持。在这一实现中，配置了一对活动-备用（active - standby） namenode。当活动 namenode 失效，备用 namenode 就会接管它的任务并开始服务于来自客户端的请求，不会有任何明显中断。

实现这一目标需要在架构上做如下修改：

- p71

#### 命令行接口 - 操作 HDFS 的基本命令

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

