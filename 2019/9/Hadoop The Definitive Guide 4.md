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

#### 2.1~2.3 使用Hadoop分析数据 - 气象数据集

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

#### 2.4 横向扩展

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

#### 2.5 Hadoop Streaming

Hadoop Streaming 使用 Unix 标准流作为 Hadoop 和应用程序之间的接口，所以可以使用任何编程语言通过标准输入/输出来写 MapReduce 程序。

Streaming 天生适合用于文本处理。map 的输入数据通过标准输入流传递给 map 函数，并且是一行一行地传输，最后将结果行写到标准输出。map 输出的 KV 对是一个以制表符分割的行，reduce 函数的输入格式与之相同并通过标准输入流进行传输。reduce 函数从标准输入流中读取输入行，该输入已由 Hadoop 框架根据键排过序，最后将结果写入标准输出。

Streaming 和 Java MapReduce API 之间的设计差异：
Java API 控制的 map 函数一次只处理一条记录。针对输入数据中的每一条记录，该框架均需调用 Mapper 的 map() 方法来处理。然而在 Streaming 中，map 程序可以自己决定如何处理输入数据。

旧版 Java MapReduce API 使用“推”记录方式，新版中使用“拉”的方式来处理。

![1567064461868](E:\git_repo\Hao_Learn\2019\8\img\1567064461868.png)

## 第3章 HDFS

管理网络中跨多台计算机存储的文件系统成为分布式文件系统（Distributed File System）。该系统架构于网络之上，势必会引入网络编程的复杂性，因此分布式文件系统比普通磁盘文件系统更为复杂。

HDFS 是 Hadoop 的旗舰级文件系统，但实际上 Hadoop 是一个综合性的文件系统抽象。

#### 3.1 HDFS 的设计

HDFS 以**流式数据访问**（一次写入、多次读取）模式来存储**超大文件**（指具有几百 MB、几百 GB、甚至几百 TB 大小的文件），运行于商用硬件（即普通硬件）集群上。

对于**商用硬件**组成的庞大集群来说，节点故障的几率还是非常高的，但 HDFS 被设计成能够继续运行且不让用户察觉到明显的中断。

HDFS 是为高数据吞吐量应用优化的，这可能会以提高时间延迟为代价，因此**不适合低时间延迟数据访问应用**。

由于 namenode 将文件系统的元数据存储在内存中，因此该文件系统所能存储的文件总数受限于 namenode 的内存容量。根据经验，每个文件、目录和数据块的存储信息大约占 150 字节。因此对于 HDFS **不适用于存储大量的小文件**。

HDFS 中的文件写入只支持单个写入者，而且写操作总是以“只添加”方式在文件末尾写数据。**不支持多个写入者操作，也不支持在文件的任意位置进行修改**。

#### 3.2 HDFS 的概念

###### 数据块

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

###### namenode 和 datanode

HDFS 集群有两类节点以管理节点-工作节点模式运行，即一个 namenode（管理节点）和多个 datanode（工作节点）。namenode 管理文件系统的命名空间。它维护着文件系统树及整棵树内所有的文件和目录。这些信息以两个文件形式永久保存在本地磁盘上：命名空间镜像文件和编辑日志文件。namenode 也记录着每个文件中各个块所在的数据节点信息，但它并不永久保存块的位置信息，因为这些信息会在系统启动时根据数据节点信息重建。

客户端（client）代表用户通过与 namenode 和 datanode 交互来访问整个文件系统。客户端提供一个类似于 POSIX（可移植操作系统界面）的文件系统接口，使用户在编程时无需知道 namenode 和 datanode 也可以实现其功能。

datanode 使文件系统的工作节点。他们根据需要存储并检索数据库（受客户端或 namenode 调度），并且定期向 namenode 发送它们所存储的块的列表。

如果运行 namenode 服务的机器损坏，文件系统上所有的文件将会丢失，文件系统将无法使用，因为不知道如何根据 datanode 的块重建文件。为了实现 namenode 的容错性，Hadoop提供了两种机制：

- 备份那些组成文件系统元数据持久状态的文件。Hadoop 可以通过配置使 namenode 在多个文件系统上保存元数据的持久状态。这些写操作是实时同步的，且为原子操作。一般的配置是，将持久状态写入本地磁盘的同时，写入一个远程挂载的网络文件系统（NFS）。
- 运行一个辅助 namenode，但它不能被用作 namenode。这个辅助 namenode 的重要作用是定期合并并保存编辑日志与命名空间镜像，以防止编辑日志过大，并且会在 namenode 发生故障时启用。但由于辅助 namenode 保存的状态总是滞后于主节点，所以难免会丢失部分数据。在这种情况下，一般把存储在 NFS 上的 namenode 元数据复制到辅助 namenode 并作为新的主 namenode 运行。 辅助 namenode 一般在另一台单独的物理计算机上运行，因为需要占用大量 CPU 时间，并且需要与 namenode 一样多的内存来执行合并操作。

###### 块缓存

通常 datanode 从磁盘中读取块，但对于访问频繁的文件，其对应的块可能被显式地缓存在datanode 的内存中，以堆外块缓存（off-heap block cache）的形式存在。默认情况下，一个块仅缓存在一个 datanode 的内存中。作业调度器（用于 MapReduce、Spark 和其他框架的）通过在缓存块的 datanode 上运行任务，可以利用块缓存的优势提高读操作的性能。

用户或应用通过在缓存池（cache pool）中增加一个 cache directive 来告诉 namenode 需要缓存哪些文件及存多久。缓存池是一个用于管理缓存权限和资源使用的管理性分组。

###### HDFS 的高可用性

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

- namenode 之间需要通过高可用共享存储实现编辑日志的共享。
- datanode 需要同时向两个 namenode 发送数据块处理报告，因为数据块的映射信息存储在 nodename 的内存中。
- 客户端需要使用特定的机制来处理 namenode 的失效问题，这一机制对用户是透明的。
- 辅助 namenode 的角色被备用 namenode 所包含，备用 namenode 为活动的 namenode 命名空间设置周期性检查点。

两种高可用性共享存储：NFS 过滤器或群体日志管理器（QJM，quorum journal manager）。

QJM 是一个专用的 HDFS 实现，为提供一个高可用的编辑日志而设计。它以一组日志节点（journalnode）的形式运行，每一次编辑必须写入多数日志节点。QJM一般有三个 journalnode，所以系统可以能够忍受任何一个丢失。

在活动 namenode 失效之后，备用 namenode 能够快速（几十秒左右）实现任务接管，因为最新的状态存储在内存中：包括最新的编辑日志条目和数据块映射信息。实际观察到的失效时间略长一点（1 分钟左右），因为系统需要保守确定活动 namenode 是否真的失效了。

活动 namenode 和备用 namenode 都失效的情况发生的概率非常低，管理员依旧可以声明一个备用 namenode 并实现冷启动。

系统中有一个称为故障转移控制器（failover controller）的新实体，管理着将活动 namenode 转移为备用 namenode 的转换过程。有多种故障转移控制器，默认的是使用了 ZooKeeper 来确保有且仅有一个活动 namenode 。每一个 namenode 运行着一个轻量级的故障转移控制器，其工作就是监视宿主 namenode 是否失效（通过一个简单的心跳机制实现），并在namenode 失效时进行故障切换。

管理员也可以手动发起故障切换，例如在进行日常维护时，这称为“平稳的故障转移”。

同一时间 QJM 仅允许一个 namenode 向编辑日志中写入数据。然而，对于先前的活动 namenode 而言，仍有可能响应并处理客户过时的读请求，所以需要设置一个 SSH 规避命令用于杀死 namenode 的进程。而 NFS 过滤器由于不可能同一时间只允许一个 namenode 写入数据，因此需要更有力的规避方法。

规避机制包括：撤销 namenode 访问共享存储目录的权限（通常使用供应商指定的NFS命令）、通过远程管理命令屏蔽相应的网络接口。最后手段是通过一个特定的供电单元对相应主机进行断电操作。

客户端的故障转移通过客户端类库实现透明处理。最简单的实现是通过客户端的配置文件实现故障转移的控制。HDFS URI 使用一个逻辑主机名，该主机名映射到一对 namenode 地址，客户端类库会访问每一个 namenode 地址直至处理完成。

#### 3.3 命令行接口 - 操作 HDFS 的基本命令

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

#### 3.4 Hadoop 文件系统

Hadoop 有一个抽象的文件系统概念，HDFS 只是其中的一个实现。Java 抽象类 `org.apache.hadoop.fs.FileSystem`定义了 Hadoop 中一个文件系统的客户端接口，并且该抽象类有几个具体实现：

![1567135657608](E:\git_repo\Hao_Learn\2019\8\img\1567135657608.png)

###### HTTP

由 WebHDFS 协议提供的 HTTP REST API 则使得其他语言开发的应用能够更方便地与 HDFS 交互。注意，HTTP 接口比原生的 Java 客户端要慢，所以不到万不得已，尽量不要用它来传输特大数据。

通过 HTTP 来访问 HDFS 有两种方法：直接访问，HDFS 守护进程直接服务于来自客户端的 HTTP 请求；通过代理（一个或多个）访问，客户端通常使用 DistributedFileSystem API 访问 HDFS。两者都使用了 WebHDFS 协议。

![1567515162093](E:\git_repo\Hao_Learn\2019\9\img\1567515162093.png)

在第一种情况中， namenode 和 datanode 内嵌的 web 服务器作为 WebHDFS 的端节点运行。（由于 dfs.webhdfs.enabled 被设置为 true，WebHDFS 默认是启用状态。）文件元数据操作由 namenode 管理，文件读写操作首先被发往 namenode，由 namenode 发送一个 HTTP 重定向至某个客户端，指示以流方式传输文件数据的目的或源 datanode。

第二种方法依靠一个或多个独立代理服务器通过 HTTP 访问 HDFS。（由于代理服务是无状态的，因此可以运行在标准的负载均衡器之后。）所有到集群的网络通信都需要经过代理，因此客户端从来不直接访问 namenode 和 datanode。使用代理服务器后可以使用更严格的防火墙策略和带宽限制策略。通常情况下都通过代理服务器，实现在不同数据中心中部署的 Hadoop 集群之间的数据传输，或从外部网络访问云端运行的 Hadoop 集群。

HttpFS 代理提供和 WebHDFS 相同的 HTTP（和 HTTPS）接口，这样客户端能够通过 webhdfs（swebhdfs）URI 访问这两类接口。HttpFS 代理的启动独立于 namenode 和 datanode 的守护进程，使用httpfs.sh 脚本，默认在一个不同的端口上监听（端口号14000）。

#### 3.5 Java 接口

Hadoop 的 Filesystem 类是与 Hadoop 的某一文件系统进行交互的 API。通过集成 FileSystem 抽象类，并编写代码，可以使其在不同文件系统中可移植。

###### 从 Hadoop URL 读取数据

要从 Hadoop 文件系统读取文件，最简单的方法是使用 java.net.URL 对象打开数据流，从中读取数据。

范例 3-1.URLStreamHandler：

```Java
// cc URLCat Displays files from a Hadoop filesystem on standard output using a URLStreamHandler
import java.io.InputStream;
import java.net.URL;

import org.apache.hadoop.fs.FsUrlStreamHandlerFactory;
import org.apache.hadoop.io.IOUtils;

// vv URLCat
public class URLCat {

  static {
    /**
     * 通过FsUrlStreamHandlerFactory实例调用 
     * java.net.URL对象的setURLStreamHandlerFactory()方法
     * JVM只能调用一次这个方法，因此通常在静态方法中调用。
     * 这个限制意味着如果程序的其他组件声明了一个
     * UrlStreamHandlerFactory实例，
     * 则将无法再次使用这种方法从Hadoop中读取数据。
     */
    URL.setURLStreamHandlerFactory(new FsUrlStreamHandlerFactory());
  }
  
  public static void main(String[] args) throws Exception {
    InputStream in = null;
    try {
      in = new URL(args[0]).openStream();
      /**
       * 调用Hadoop中简洁的IOUtils类，并在finally字句中关闭数据
       * 流，同时也可以在输入/输出流之间复制数据。copyBytes的最后
       * 两个参数，第一个设置用于复制的缓冲区大小，第二个设置复制结
       * 束后是否关闭数据流。
       */
      IOUtils.copyBytes(in, System.out, 4096, false);
    } finally {
      IOUtils.closeStream(in);
    }
  }
}
// ^^ URLCat
```

运行测试：

```shell
export HADOOP_CLASSPATH=ch03-hdfs-4.0.jar
# 在core-site.xml中可以设置 namenode 端口
#<property>
#    <name>fs.default.name</name>
#    <value>hdfs://localhost:9000</value>
#</property>
hadoop URLCat hdfs://localhost:9000/user/root/input/1901.tx
```

###### 通过 FileSystem API 读取数据

Hadoop 文件系统中通过 Hadoop Path 对象（而非 java.io.File 对象，因为它的语义与本地文件系统联系太紧密）来代表文件。可以将路径视为一个 Hadoop 文件系统URI。

FileSystem 是一个通用的文件系统 API，所以第一步是检索我们需要使用的文件系统实例。获取 FileSystem 实例有下面这几个静态工程方法：

```Java
public static FileSystem get(Configuration conf) throws IOException {
    return get(getDefaultUri(conf), conf);
}

public static FileSystem get(URI uri, Configuration conf) throws IOException {
    String scheme = uri.getScheme();
    String authority = uri.getAuthority();

	// use default FS
    if (scheme == null && authority == null) {    
    	return get(conf);
    }

    if (scheme != null && authority == null) {     
    // no authority
    URI defaultUri = getDefaultUri(conf);
    // if scheme matches default & default has authority
    if (scheme.equals(defaultUri.getScheme())    
        && defaultUri.getAuthority() != null) {  
        // return default
        return get(defaultUri, conf);              
      }
    }
    
    String disableCacheName = String.format("fs.%s.impl.disable.cache", scheme);
    if (conf.getBoolean(disableCacheName, false)) {
      return createFileSystem(uri, conf);
    }

    return CACHE.get(uri, conf);
  }

public static FileSystem get(final URI uri, final Configuration conf,
        final String user) throws IOException, InterruptedException {
    String ticketCachePath =
      conf.get(CommonConfigurationKeys.KERBEROS_TICKET_CACHE_PATH);
    UserGroupInformation ugi =
        UserGroupInformation.getBestUGI(ticketCachePath, user);
    return ugi.doAs(new PrivilegedExceptionAction<FileSystem>() {
      @Override
      public FileSystem run() throws IOException {
        return get(uri, conf);
      }
    });
  }
```

Configuration 对象封装了客户端或服务器的配置，通过设置配置文件读取类路径来实现。第一个方法返回的是默认文件系统（默认为本地文件系统，可以在 core-site.xml 中指定）。第二个方法通过给定的 URI 方案和权限来确定要使用的文件系统，如果给定的 URI 中没有指定方案，则返回默认文件系统。第三个是作为给定用户来访问文件系统。

在某些情况下，可能希望获取本地文件系统的运行实例，此时可以使用一下方法获取：

```Java
public static LocalFileSystem getLocal(Configuration conf)
    throws IOException {
    return (LocalFileSystem)get(LocalFileSystem.NAME, conf);
  }
```

有了 FileSystem 实例之后，我们调用 open() 函数来获取文件的输入流：

```Java
public abstract FSDataInputStream open(Path f, int bufferSize)
    throws IOException;
    
/**
 * 默认的缓冲区大小为 4KB
 */
  public FSDataInputStream open(Path f) throws IOException {
    return open(f, getConf().getInt("io.file.buffer.size", 4096));
  }
```

范例 3-2.FileSystem ：

```Java
// cc FileSystemCat Displays files from a Hadoop filesystem on standard output by using the FileSystem directly
import java.io.InputStream;
import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;

// vv FileSystemCat
public class FileSystemCat {

  public static void main(String[] args) throws Exception {
    String uri = args[0];
    // 创建配置对象
    Configuration conf = new Configuration();
    // 通过get方法获取FileSystem
    FileSystem fs = FileSystem.get(URI.create(uri), conf);
    InputStream in = null;
    try {
        // 通过fileSystem.open方法获取输入流
        in = fs.open(new Path(uri));
        // 复制数据
        IOUtils.copyBytes(in, System.out, 4096, false);
    } finally {
        IOUtils.closeStream(in);
    }
  }
}
// ^^ FileSystemCat
```

运行测试：

```shell
hadoop FileSystemCat hdfs://localhost:9000/user/root/input/1901.txt
```

实际上，FileSystem 对象中的 open() 方法返回的是 FSDataInputStream 对象，而不是标准的 java.io 类对象。这个类是继承了 java.io.DataInputStream 的一个特殊类，并支持随机访问，由此可以从流的任意位置读取数据。

```Java
package org.apache.hadoop.fs;

public class FSDataInputStream extends DataInputStream
    implements Seekable, PositionedReadable, 
      ByteBufferReadable, HasFileDescriptor, CanSetDropBehind, CanSetReadahead,
      HasEnhancedByteBufferAccess { ... }
```

Seekable 接口支持在文件中找到指定位置，并提供一个查询当前位置相对于文件起始位置偏移量的查询方法 getPos()。

```Java
public interface Seekable {
  
  void seek(long pos) throws IOException;
  
  long getPos() throws IOException;
}
```

调用 seek() 来定位大于文件长度的位置会引发 IOException。与 java.io.InputStream 的 skip() 不同，seek() 可以移到文件中任意一个绝对位置，skip() 则只能现对于当前位置定位到另一个新位置。 

范例 3-3.使用 seek() 方法：

```Java
// cc FileSystemDoubleCat Displays files from a Hadoop filesystem on standard output twice, by using seek
import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;

// vv FileSystemDoubleCat
public class FileSystemDoubleCat {

  public static void main(String[] args) throws Exception {
    String uri = args[0];
    Configuration conf = new Configuration();
    FileSystem fs = FileSystem.get(URI.create(uri), conf);
    // FSDataInputStream 类支持随机访问
    FSDataInputStream in = null;
    try {
      in = fs.open(new Path(uri));
      IOUtils.copyBytes(in, System.out, 4096, false);
      // 通过 seek 方法返回到文件开头
      in.seek(0); 
      IOUtils.copyBytes(in, System.out, 4096, false);
    } finally {
      IOUtils.closeStream(in);
    }
  }
}
// ^^ FileSystemDoubleCat

```

测试结果：

```shell
hadoop FileSystemDoubleCat hdfs://localhost:9000/user/root/input/test.txt
```

PositionedReadable 接口可以从一个指定偏移量处读取文件的一部分。

```Java
public interface PositionedReadable {
   
  public int read(long position, byte[] buffer, int offset, int length)
    throws IOException;
  
  public void readFully(long position, byte[] buffer, int offset, int length)
    throws IOException;
  
  public void readFully(long position, byte[] buffer) throws IOException;
}
```

read() 方法从文件的指定 position 处读取至多为 length 字节的数据并存入缓冲区 buffer 的指定偏移量 offset 处。返回值是实际读到的字节数：调用者需要检查这个值，它有可能小于指定的 length 长度。

readFully() 方法将指定 length 长度的字节数数据读取到 buffer 中（或在只接受 buffer 字节数组的版本中，读取 buffer.length 长度字节数据），除非已经读到文件末尾，这种情况下将抛出 EOFException。

所有的这些方法会保留文件当前偏移量，并且是线程安全的（FSDataInputStream 并不是为并发访问设计的，因此最好为此新建多个实例），因此它们提供了在读取文件主体时，访问文件其他部分（可能是元数据）的便利方法。

seek() 方法是一个相对高开销的操作，需要慎重使用。建议用流数据来构建应用的访问模式（比如使用 MapReduce），而非执行大量 seek() 方法。

###### 写入数据

FileSystem 类有一系列新建文件的方法。最简单的方法是给准备建的文件指定一个 Path 对象，然后返回一个用于写入数据的输出流：

```Java
public FSDataOutputStream create(Path f) throws IOException
```
此方法有多个重载版本，可以指定是否需要强制覆盖现有文件，文件备份数量、写入文件时所用缓冲区的大小、文件块大小以及文件权限。

create() 方法能够为需要写入且当前不存在的文件创建父目录。如果希望父目录不存在就导致文件写入失败，则应该先调用 exists() 方法检查父目录是否存在。另一种方案是使用 FileContext ，可以控制是否创建父目录。

还有一个重载方法 Progressable 用于传递回调接口，如此一来，可以把数据写入 datanode 的进度通知给应用。

```Java
package org.apache.hadoop.util;

public interface Progressable {
  public void progress();
}
```

另一种新建文件的方法是使用 append() 方法在一个现有文件末尾追加数据（还有其他一些重载版本）：

```Java
public FSDataOutputStream append(Path f) throws IOException
```

这样的追加操作允许一个 writer 打开文件后再访问该文件的最后偏移量处追加数据。有了这个 API，某些应用可以创建无边界文件，例如，应用可以在关闭日志文件之后继续追加日志。该追加操作是可选的，并非所有 Hadoop 文件系统都实现了该操作。例如，HDFS 支持追加，但 S3 文件系统就不支持。

每次 Hadoop 调用 progress() 方法时，也就是每次将 64KB 数据包写入 datanode 管线后，打印一个时间点来显示整个运行过程。

范例 3-4.将本地文件复制到 Hadoop 文件系统：

```Java
// cc FileCopyWithProgress Copies a local file to a Hadoop filesystem, and shows progress
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.util.Progressable;

// vv FileCopyWithProgress
public class FileCopyWithProgress {
  public static void main(String[] args) throws Exception {
    String localSrc = args[0];
    String dst = args[1];
    
    // 通过 FileInputStream 构造方法创建文件输入流，并包装缓冲流
    InputStream in = new BufferedInputStream(new FileInputStream(localSrc));
    
    Configuration conf = new Configuration();
    
    FileSystem fs = FileSystem.get(URI.create(dst), conf);
    // 通过create创建OutputStream
    OutputStream out = fs.create(new Path(dst), new Progressable() {
        // progress 方法用于在单行处理完成之后进行回调
        public void progress() {
          System.out.print(".");
        }
    });
    // 最后一个参数为true，则结束后关闭数据流
    IOUtils.copyBytes(in, out, 4096, true);
  }
}
// ^^ FileCopyWithProgress

```

```shell
hadoop FileCopyWithProgress test.txt hdfs://localhost:9000/user/root/output/test.txt
```

FIleSystem 实例的 create() 方法返回 FSDataOutputStream 对象，与 FSDataInputStream 类相似，它也有一个查询文件当前位置的方法。

```Java
package org.apache.hadoop.fs;

public class FSDataOutputStream extends DataOutputStream
    implements Syncable, CanSetDropBehind {
    
    public long getPos() throws IOException {
    	// return cached position
		return position;  
    }
    // implementation elided
}
```

但与 FSDataInputStream 类不同的是，FSDataOutputStream 类不允许在文件中定位。这是因为 HDFS 只允许对一个已打开的文件顺序写入，或在现有文件的末尾追加数据，因为定位写入位置确实没有什么意义。

###### 目录

Filesystem 实例提供了创建目录的方法：

```Java
public boolean mkdirs(Path f) throws IOException
```

这个方法可以一次性新建所有需要创建但不存在的父目录。如果目录（以及所有父目录）都已经创建成功，则返回true。

###### 查询文件系统

1. 文件元数据：FileStatus

任何文件系统的一个重要特征都是提供其目录结构浏览和检索它所存文件和目录相关信息的功能。FIleStatus 类封装了文件系统中文件和目录的元数据，包括文件长度、块大小、复本、修改时间、所有者以及权限信息。

FileSystem 的 getFIleStatus() 方法用于获取文件或目录的 FileStatus 对象。

范例 3-5.展示文件状态信息：

```Java
// cc ShowFileStatusTest Demonstrates file status information
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.Matchers.lessThanOrEqualTo;

import java.io.*;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.hdfs.MiniDFSCluster;
import org.junit.*;

// vv ShowFileStatusTest
public class ShowFileStatusTest {
  
  // 使用进程内的HDFS集群进行测试
  private MiniDFSCluster cluster; 
  private FileSystem fs;

  @Before
  public void setUp() throws IOException {
    Configuration conf = new Configuration();
    if (System.getProperty("test.build.data") == null) {
      System.setProperty("test.build.data", "/tmp");
    }
    cluster = new MiniDFSCluster.Builder(conf).build();
    fs = cluster.getFileSystem();
    OutputStream out = fs.create(new Path("/dir/file"));
    out.write("content".getBytes("UTF-8"));
    out.close();
  }
  
  @After
  public void tearDown() throws IOException {
    if (fs != null) { fs.close(); }
    if (cluster != null) { cluster.shutdown(); }
  }
  
  @Test(expected = FileNotFoundException.class)
  public void throwsFileNotFoundForNonExistentFile() throws IOException {
    fs.getFileStatus(new Path("no-such-file"));
  }
  
  @Test
  public void fileStatusForFile() throws IOException {
    Path file = new Path("/dir/file");
    
    FileStatus stat = fs.getFileStatus(file);
    // 获取文件目录：Path.URL(分层URI).decodedPath(此URI的解码路径组件)
    assertThat(stat.getPath().toUri().getPath(), is("/dir/file"));
    // 是否是目录
    assertThat(stat.isDirectory(), is(false));
    // 获取长度
    assertThat(stat.getLen(), is(7L));
    // 获取修改时间
    assertThat(stat.getModificationTime(), is(lessThanOrEqualTo(System.currentTimeMillis())));
    // 获取文件的复本
    assertThat(stat.getReplication(), is((short) 1));
     // 获取文件的块大小
    assertThat(stat.getBlockSize(), is(128 * 1024 * 1024L));
    // 获取文件的拥有者
    assertThat(stat.getOwner(), is(System.getProperty("user.name")));
     // 获取文件的拥有组
    assertThat(stat.getGroup(), is("supergroup"));
     // 获取文件的权限
    assertThat(stat.getPermission().toString(), is("rw-r--r--"));
  }
  
  @Test
  public void fileStatusForDirectory() throws IOException {
    Path dir = new Path("/dir");
    FileStatus stat = fs.getFileStatus(dir);
    assertThat(stat.getPath().toUri().getPath(), is("/dir"));
    assertThat(stat.isDirectory(), is(true));
    assertThat(stat.getLen(), is(0L));
    assertThat(stat.getModificationTime(),
        is(lessThanOrEqualTo(System.currentTimeMillis())));
    assertThat(stat.getReplication(), is((short) 0));
    assertThat(stat.getBlockSize(), is(0L));
    assertThat(stat.getOwner(), is(System.getProperty("user.name")));
    assertThat(stat.getGroup(), is("supergroup"));
    assertThat(stat.getPermission().toString(), is("rwxr-xr-x"));
  }
  
}
// ^^ ShowFileStatusTest
```

2. 列出文件

FileSystem.listStatus() 查找一个文件或目录相关的相关的信息很实用，但通常还需要能够列出目录的中的内容。

```Java
public abstract FileStatus[] listStatus(Path f) throws FileNotFoundException, IOException;
  
public FileStatus[] listStatus(Path f, PathFilter filter) 
        throws FileNotFoundException, IOException {
    ArrayList<FileStatus> results = new ArrayList<FileStatus>();
    listStatus(results, f, filter);
    return results.toArray(new FileStatus[results.size()]);
}

public FileStatus[] listStatus(Path[] files)
        throws FileNotFoundException, IOException {
    return listStatus(files, DEFAULT_FILTER);
}

public FileStatus[] listStatus(Path[] files, 
    PathFilter filter) throws FileNotFoundException,           IOException {
    ArrayList<FileStatus> results = new ArrayList<FileStatus>();
    for (int i = 0; i < files.length; i++) {
      listStatus(results, files[i], filter);
    }
    return results.toArray(new 	
        FileStatus[results.size()]);
}
```

当传入的参数是一个文件时，它会简单转变成以数组方式返回长度为 1 的 FileStatus 对象。当传入参数是一个目录时，则返回 0 或多个 FileStatus 对象，表示此目录中包含的文件和目录。

它的重载方法允许使用 PathFilter 来限制匹配的文件和目录。如果指定一组路径，其执行结果相当于依次轮流传递每条路径并对其调用 listStatus() 方法，再将所有 FileStatus 对象存入同一数组中，该方法更为方便。这个方法在从文件系统树的不同分支构建输入文件列表时非常管用。

范例 3-6.显示Hadoop 文件系统中一组路径的文件信息：

```Java
// cc ListStatus Shows the file statuses for a collection of paths in a Hadoop filesystem 
import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.Path;

// vv ListStatus
public class ListStatus {

  public static void main(String[] args) throws Exception {
    String uri = args[0];
    System.out.println(args[0]);
    Configuration conf = new Configuration();
    FileSystem fs = FileSystem.get(URI.create(uri), conf);
    
    Path[] paths = new Path[args.length];
    for (int i = 0; i < paths.length; i++) {
      paths[i] = new Path(args[i]);
    }
    
    //fileSystem.listStatus(Path[] paths) 通过一个Path对象数组获取FileStaus对象数组
    FileStatus[] status = fs.listStatus(paths);
    // FileUtil.stat2Paths(FileStatus[] stats)) 将一个FIleStaus对象数组转换为一个Path对象数组
    Path[] listedPaths = FileUtil.stat2Paths(status);
    for (Path p : listedPaths) {
      System.out.println(p);
    }
  }
}
// ^^ ListStatus
```

测试结果：

```shell
# 显示一组路径集目录列表的并集
hadoop ListStatus hdfs://localhost:9000/ hdfs://localhost:9000/user/root/

hdfs://localhost:9000/opt
hdfs://localhost:9000/root
hdfs://localhost:9000/user
hdfs://localhost:9000/user/root/-p
hdfs://localhost:9000/user/root/input
hdfs://localhost:9000/user/root/output
```

3. 文件模式

Hadoop 可以执行通配（globbing），并由 FileSystem 提供的两个 globStatus 方法实现：

```Java
public FileStatus[] globStatus(Path pathPattern) throws IOException {
    return new Globber(this, pathPattern, DEFAULT_FILTER).glob();
  }

public FileStatus[] globStatus(Path pathPattern, PathFilter filter)
      throws IOException {
    return new Globber(this, pathPattern, filter).glob();
  }
```

globStatus() 方法返回是有路径格式与指定模式匹配的所有 FIleStatus 对象组成的数组，并按路径排序。PathFilter 参数作为可选项可以进一步对匹配结果进行限制。

表 3-2.通配符及其含义（Hadoop 支持的通配符与 Unix bash shell 支持的相同）：

![1567391692179](E:\git_repo\Hao_Learn\2019\9\img\1567391692179.png)

4. PathFilter

FileSystem 中的 listStatus() 和 globStatus() 方法提供了可选的 PathFilter 对象，已编程方式控制通配符：

```Java
package org.apache.hadoop.fs;

import org.apache.hadoop.classification.InterfaceAudience;
import org.apache.hadoop.classification.InterfaceStability;

@InterfaceAudience.Public
@InterfaceStability.Stable
public interface PathFilter {
 
    boolean accept(Path path);
}

// FileFilter 与 PathFilter 相似，但 accept 方法的参数是 File
package java.io;

@FunctionalInterface
public interface FileFilter {

    boolean accept(File pathname);
}
```

范例 3-7.PathFilter：

```Java
// cc RegexExcludePathFilter A PathFilter for excluding paths that match a regular expression
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.PathFilter;

// vv RegexExcludePathFilter
public class RegexExcludePathFilter implements PathFilter {
  
  private final String regex;

  public RegexExcludePathFilter(String regex) {
    this.regex = regex;
  }

  public boolean accept(Path path) {
    // 匹配则返回 false
    return !path.toString().matches(regex);
  }
}
// ^^ RegexExcludePathFilter
```

这个过滤器只传递不匹配于正则表达式的文件。在通配符选出一组初始文件之后，可使用过滤器优化结果。

![1567393765813](E:\git_repo\Hao_Learn\2019\9\img\1567393765813.png)

以 Path 为例，过滤器只能作用于文件名，不能针对文件的属性来构建过滤器。

###### 删除数据

使用 FileSystem 的 delete() 方法可以永久性删除文件或目录。

```Java
public boolean delete(Path f, boolean recursive) throws IOException
```

如果 f 是一个文件或空目录，那么 recursive 的值就会被忽略。只有在 recursive 为 true 时，非空目录及其内容才会被删除（否则会抛出 IOException 异常）。

#### 3.6 数据流

###### 剖析（anatomy）文件读取

读取文件时事件的发生顺序：

客户端通过调用 FileSystem 对象的 open() 来打开要读取的文件，对于 HDFS 来说，这个对象是 DistributedFileSystem 的一个实例。它通过使用 RPC（远程过程调用）来调用 namenode，以确定文件起始块的位置。对于每一个块，namenode 返回存有该块复本的 datanode 地址。此外 datanode 根据它们与客户端的距离来排序（根据集群的网络拓扑）。如果 该客户端本身就是一个 namenode（比如在一个 MapReduce 任务中），那么该客户端将会从保存有相应数据块复本的本地 namenode 读取数据。

![1567408442514](E:\git_repo\Hao_Learn\2019\9\img\1567408442514.png)

DistributedFileSystem 类调用 open()方法会返回一个 FSDataInputStream 对象（一个支持文件定位的输入流）给客户端以便读取数据。FSDataInputStream 继而封装了一个 DFSInputStream，用于管理 datanode	和 namenode 的 I/O。

客户端随之在流中调用 read() 方法。为文件起始块存储了 datanode 地址的 DFSInputStream 随后为第一个文件起始块连接第一个（最近的一个）的 datanode。数据从 datanode 被传输回到重复调用 read() 的客户端。当到达块的末尾时，DFSInputStream 将关闭对该 datanode 的连接，然后为下一个块找到最佳的 datanode 。所有这些对于客户端都是透明的，在它看来只是在读取一个连续的流。

如同客户端从流中读取数据，随着 DFSInputStream 对 datanode 打开新的连接，块被按顺序读取。在必要时（as needed），为了下一批块，它也将调用 namenode 去检索 datanode 位置 。当客户端完成读取，它对 FSDataInputStream 中调用 close() 。

读取数据中，如果 DFSInputStream 在于 datanode 通信时遇到错误，会尝试从这个块的下一个最邻近的 datanode 读取数据。它也将记住那些发生故障的 datanode，因此它为了后来的块不是不必要的重试它们。DFSInputStream 也会通过校验和确认从 datanode 发来的数据是否完整。如果发现有损坏的块，DFSInputStream 会试图从其他的 datanode 读取其复本，也会将损坏的块通知给 namenode。

这个设计的一个重要方面是，客户端可以直接连接到 datanode 检索数据，且通过 namenode，客户端被引导到每个块所在的最佳 datanode。由于数据流分散（spread across）在集群中的所有 datanode，所以这种设计允许 HDFS 扩展到大量的并发客户端。同时，namenode 仅仅（merely）需要服务块位置的请求（这些信息存储在内存，因此非常高效），例如，namenode不服务数据，随着客户机数量的增长，数据很快就会成为瓶颈。

###### 剖析文件写入

![1567408487422](E:\git_repo\Hao_Learn\2019\9\img\1567408487422.png)

客户端通过在 DistributedFileSystem 对象中调用 create() 来新建文件。DistributedFileSystem 创建一个 RPC 调用 namenode 在文件系统的命名空间中新建一个文件，此时该还没有数据块与文件进行联系。namenode 执行各种不同的检查以确保这个文件不存在，并且客户端有创建该文件的权限。如果这些检查均通过，namenode 就会为创建新文件记录一条记录；否则，文件创建失败并客户端抛出一个 IOException。DistributedFileSystem 为客户端返回一个 FSDataOutputStream 对象，由此客户端可以开始写入数据。就像读取一样，FSDataOutputStream 封装一个 DFSOutputStream 对象，该对象负责处理 datanode 和 namenode 之间的通信。

如同客户端写入数据，DFSOutputStream 将它分成一个个的数据包，并写入内部队列，称为“数据队列”（data queue）。数据队列被 DataStreamer 消耗，DataStreamer的责任是挑选出一组合适的datanode去存储数据副本 ，并据此来合理的要求 namenode 分配新的数据块。这一组 datanode 组成了一个管线（pipeline），在这里我们假设复本数为 3，所以管线中有 3 个节点。DataStreamer 将数据包流式传输到管线中的第 1 个 datanode，该 datanode 存储数据包并将它发送到管线中的第 2 个 datanode。同样，第 2 个 datanode 存储该数据包并且发送给管线中的第 3 个 （最后一个）datanode。

DFSOutputStream 也维护着一个正在等待被 datanode 确认的数据包内部队列，称为”确认队列“（ack queue）。只有当被管道中所有 datanode 确认后，该数据包才会从确认队列中被删除。

如果在数据被写入时，任何 datanode 发生故障，则以下操作（对客户端写入数据来说是透明的）会被执行。第一，管线被关闭，而且任何在确认队伍中的数据包会被添加到数据队列的前面，以便故障节点下游的 datanode 不会丢失任何数据包。在正常 datanode 中的当前块将被给予一个新的联系 namenode 的身份，以便如果故障 datanode 后来被恢复，可以删除其中的部分块。故障 datanode 被从管线删除，而且一个新的管线被在两个正常 datanode之间构造。剩下的（The remainder of）数据块被写入管线中的正常 datanode 中。namenode 注意到块是复制不足的， 会安排在另一个节点上创建另一个（a further replica）副本。然后后续块被当做正常块对待。

在一个块被写入期间可能会有多个 datanode 同时发生故障，但非常少见。只要写入了 dfs.namenode.replication.min 的复本数（默认为 1），写操作就会成功，而且这个块可以在集群范围内被异步复制，直到达到其目标副本数（dfs.replication 的 默认值为 3）。

客户端完成数据的写入后，会在数据流调用 close() 方法。该操作将剩余的所有数据包写入 datanode 管线，并在联系 namenode 表示文件已完成之前等待确认。namenode 已经知道文件由哪些块组成（因为 DataStreamer 请求数据块分配），所以它在返回成功前只需要等待数据块进行最小量的复制。

###### 一致模型

一致模型（coherency model）为文件系统描述了文件读/写的数据可见性。HDFS 为了性能牺牲了一些 POSIX 要求，因此一些操作与你期望的可能不同。



新建一个文件之后，它在文件系统命名空间中是可见的，例如：

```Java
Path p = new Path("p");
fs.create(p);
assertThat(fs.exists(p), is(true));
```

然而，写入文件的任何内容不被保证是可见的，即使数据流已经刷新。所以文件长度显示为 0：

```Java
Path p = new Path("p");
OutputStream out = fs.create(p);
out.write("content".getBytes("UTF-8"));
out.flush();
assertThat(fs.getFileStatus(p).getLen(), is(0L));
```

当超过一个块的数据被写入，第一个数据块对新的 reader 就是可见的。之后的块也不例外。总之，当前正在被写入的块对其他的 reader 不可见。

HDFS 提供了一种强行将所有缓存刷新到 datanode 中的手段，即通过在 FSDataOutputStream 中调用 hflush() 方法。当 hflush() 方法返回成功后，HDFS 能保证文件中写到该点的数据已经到达在写入管线中的所有 datanode 并且对所有新的 reader 均可见：

```Java
Path p = new Path("p");
FSDataOutputStream out = fs.create(p);
out.write("content".getBytes("UTF-8"));
out.hflush();
assertThat(fs.getFileStatus(p).getLen(), 
				is(((long) "content".length())));
```

注意（Note that），hflush() 并不保证 datanode 已经将数据写到磁盘上，数据只是在 datanode 的内存中（所以如果发生（in the event of ）数据中心断电（outage），数据会丢失）。为了数据写入到磁盘上这个更有力的保证，使用 hsync() 代替。

hsync() 的操作类似于在 POSIX 中的 fsync() 系统调用，该调用提交的是一个关于文件描述符的缓冲数据。例如，利用标准 Java API 数据写入本地文件，在刷新数据流且同步之后我们保证能看到文件内容：

```Java
FileOutputStream out = new FileOutputStream(localFile);
out.write("content".getBytes("UTF-8"));
out.flush(); // flush to operating system
out.getFD().sync(); // sync to disk
assertThat(localFile.length(), is(((long) "content".length())));
```

```Java
Path p = new Path("p");
FSDataOutputStream out = fs.create(p);
out.write("content".getBytes("UTF-8"));
out.hsync();
assertThat(fs.getFileStatus(p).getLen(), 
				is(((long) "content".length())));
out.close();
assertThat(fs.delete(p, true), is(true));
```

在 HDFS 中关闭文件其实也隐含了执行 hflush() 方法：

```Java
Path p = new Path("p");
OutputStream out = fs.create(p);
out.write("content".getBytes("UTF-8"));
out.close();
assertThat(fs.getFileStatus(p).getLen(),
				is(((long)"content".length())));
```

**对应用设计的重要性**

这个一致模型对你设计应用程序的方式有指示。随着不调用 hflush() 或 hsync() ，如果客户端或系统发生故障，你应该做好准备丢失数据块。对大部分应用程序来说，这是不可接受的，所以你应该在合适的点调用 hflush() 方法，例如在写入一定数量的（a certain number of）记录或字节之后。尽管 hflush() 操作被设计成不过度的使 HDFS 负载，但它有许多额外开销（hsync() 的开销更大），所以在数据鲁棒性（robustness）和吞吐量（throughput）之间就会有权衡。怎样被算作（constitute）一个可以接受的权衡是依赖于应用程序的，通过测量应用程序和不同 hflush() 或 hsync() 调用频率（frequency）所呈现出的性能，最终选择一个合适的值。

#### 3.7 通过 distcp 并行复制

我们看到的 HDFS 访问模式（pattern）到目前为止都聚焦于单线程访问 。例如，通过指定文件通配符，可能对一系列文件（a collectionof）有作用，但是关于这些文件的高效并行处理，你需要自己写一个程序。Hadoop 自带一个有用的程序 distcp，该程序可以以并行方式复制大量数据从（到） Hadoop 文件系统。

distcp 的一种用法是高效的代替 `hadoop fs -cp`。例如，我们可以将文件复制到另一个文件中，也可以复制目录：

```shell
hadoop distcp file1 file2
# or
hadoop distcp dir1 dir2
```

如果 dir2 不存在，将新建 dir2，目录 dir1 的内容全部复制到 dir2 下。可以指定多种源路径，所有内容都将被复制到目标路径（destination）下。

如果 dir2 已经存在，那么目录 dir1 复制到 dir2 下，形成目录结构 dir2/dir1。使用`-overwrite`选项可以在保持同样的目录结构的同时强制覆盖原有文件。使用`-update`选项，仅更新发生变化的文件。即如果我们在 dir1 的子树中改变了一个文件，通过运行这个命令，我们可以同步命令到 dir2。

TIP：如果不确定 distcp 操作的效果，最好先现在一个小的测试目录树下试运行。

即使对于单个文件复制，由于`hadoop fs -cp`通过运行命令的客户端进行文件复制，因此更倾向于使用 distcp 变种复制大文件。

distcp 是作为一个 MapReduce 作业来实现的，该复制作业是通过集群中并行运行的 map 来完成。这里没有 reducer。每个文件通过一个 map 进行复制，而且 distcp 通过将文件放入大致（roughly）相等的分配（allocation），试图为每一个 map 分配大约（approximately）相等数量的数据来执行。默认情况下，将近 20 个 map 被使用，但是可以通过为 distcp 指定 `-m`参数来修改 map 的数量。

关于 distcp 的一个常见使用实例实在两个 HDFS 集群间传送数据。例如，以下命令在第二个集群上为第一个集群创建了一个备份：

```shell
hadoop distcp -update -delete -p hdfs://namenode1/src hdfs://namenode2/back-src
```

`-delete`选项导致（cause） distcp 从目标路径删除没在源路径中出现的任意文件或目录，`-P` 选项意味着文件状态属性如权限、块大小和复本数被保留。当你运行不带参数的 distcp 时，能够看到准确（precise）的使用说明。

如果两个集群运行的是 HDFS 的不兼容（incompatible）版本，你可以将 webhdfs 协议用于它们之间的 distcp：

```shell
hadoop distcp -update -delete -p webhdfs://namenode1:50070/src webhdfs://namenode2:50070/back-src
```
另一个变种是使用 HttpFS 代理作为 distcp 源或目标（有一次使用了 webhdfs协议），这样具有设置防火墙策略和控制带宽策略的优点。

**保证 HDFS 集群的均衡**

向 HDFS 复制数据时，考虑集群的均衡性是相当重要的。当文件块在集群中均匀分布时，HDFS 能达到最佳工作状态，因此要想确保 distcp 不会破坏这点：

1. 最好首先使用默认的每个节点 20 个 map 来运行 distcp 命令
2. 或者以使用均衡器（balancer）工具进而改善集群中块分布的均匀程度

## 第4章 关于 YARN

Apache YARN(Yet Another Resource Negotiator) 是 Hadoop的集群资源管理系统。YARN 在 Hadoop 2 中被介绍为提高 MapReduce 实现。

YARN 提供了请求和使用集群资源的 API，但是这些 API 一般（typically）不直接被用户代码使用。相反，用户代码中用的是分布式计算框架提供的更高层 API，这些 API 建立在 YARN 之上且向用户隐藏了资源管理细节。

![1567561767223](E:\git_repo\Hao_Learn\2019\9\img\1567561767223.png)

还有一层应用是建立在上图所示的框架之上。如 Pig，Hive 和 Crunch 都是运行在 MapReduce，Spark 或 Tez（或三个都可）之上的处理框架，它们不和 YARN 直接打交道。

#### 4.1 剖析 YARN 应用运行机制

YARN 通过两类长期运行的守护进程提供自己的核心服务：管理集群上资源使用的资源管理器（resource manager）、运行在集群中所有节点上且能启动和监控容器（container）的节点管理器（node manager）。容器用于执行特定应用程序的进程，每个容器都有资源限制（内存、CPU等）。一个容器可以是一个 Unix 进程，也可以是一个 Linux cgroup，取决于 YARN 的配置。下图描述了 YARN 是如何运行一个应用的。

![1567584232117](E:\git_repo\Hao_Learn\2019\9\img\1567584232117.png)

为了在 YAEN 上运行一个应用，首先，客户端联系资源管理器，要求它运行一个 application master 进程。然后，资源管理器找到一个能够在容器中启动 application master 的节点管理器（2a，2b）。准确地说，application master 一旦运行起来后能做些什么依赖于应用本身。有可能是在所处的容器中简单地运行一个计算，并将结果返回给客户端；或是向资源管理器请求更多的容器（3），以用于运行一个分布式计算（4a，4b）。

YARN 本身不会为应用的各部分（客户端、master 和进程）彼此之间通信提供任何手段。大多数重要的 YARN 应用使用某种形式的远程通信机制（例如 Hadoop 的 RPC层）来向客户端传递状态更新和返回结果，但是这些通信机制都是专属于各应用的。

###### 资源请求

YARN 有一个灵活的资源请求模型。当请求多个容器时，可以指定每个容器需要的计算机资源数量（内存和 CPU），还可以指定对容器的本地限制要求。

在确保分布式数据处理算法高效使用集群带宽中，本地化是极重要的（critical），因此，YARN允许一个应用为正在申请的容器指定（specify）本地限制（constraints）。本地限制能被使用与申请一个位于指定节点或 rack，或集群中任何位置（off-rack）的容器。

有时候本地限制不能被满足，在这种情况下（in which case），要么没有应用被创建，要么随意地（optionally），限制被放松（loosen）。

通常情况下，当启动一个容器用于处理 HDFS 数据块时，应用将会向这样的节点申请容器：存储该数据块三个复本的节点，或是存储这些复本的 rack 中的一个节点。如果都申请失败，则申请集群中的任意节点。

YARN 应用可以在运行中的任意时刻提出资源申请。例如，可以在最开始提出所有请求，或者为了满足不断变化的应用需要，采取更为动态的方式在需要更多资源时提出请求。

Spack 采用了上述第一种方式（approach，n.），在集群上启动固定数量的执行器。另一方面，MapReduce 则分两步走，在最开始时申请 map 任务容器，reduce 任务容器的启动则放在后期。同样，如果任何任务出现失败，将会另外申请容器已重新运行失败的任务。

###### 应用生命期

YARN 应用的生命期差异性很大：有几秒的短期应用，也有连续运行几天甚至几个月的长期应用。

按照应用到用户运行的作业之间的映射关系对应用进行分类：
1. 最简单的模型是一个用户作业对应一个应用，这也是 MapReduce 采取的方式。
2. 作业的每个工作流或每个用户对话（可能并无关联性）对应一个应用。容器可以在作业之间重用，并且有可能缓存作业之间的中间数据。Spark采取了这种模型。
3. 多个用户共享一个长期运行的应用。这种应用通常是作为一种协调者的角色长期运行的 applicaiotn master。由于避免了启动新 applicaiotn master 带来的开销，一个总是开启的 applicaiotn master 意味着用户将获得非常低延迟的查询响应。

###### 构建 YARN 应用

从无到有编写一个 YARN 应用是一件相当复杂的事，但在很多情况下不必这样。有很多现成的应用，在符合要求的情况下通常可以直接使用。

#### 4.2 YARN 与 MapReduce 1 相比

MapReduce 在Hadoop的初始版本中的分布式实现有时被描述为`MapReduce 1` ，以区分（distinguish）使用了 YARN 的 MapReduce 2。

新旧版本 MapReduce API 之间的区别在于不同于 MapReduce 1/2 执行框架的区别。API 具有面向用户的、客户端的特性，并且决定着用户怎样写 MapReduce 程序；而执行机制只是运行 MapReduce 程序的不同途径而已。新旧版本 API 在 MapReduce 1/2 运行的四种组合都是支持的。

在 MapReduce 1 中，有两类守护进程控制着作业执行过程：一个 jobtracker 及一个或多个 tasktracker。jobtracker 通过安排（schedule）tasktracker 上运行的任务协调所有运行在系统上的作业。tasktracker 在运行任务的同时将运行进度报告发送给 jobtracker，jobtracker 由此记录每项作业任务的整体进度情况。如果其中一个任务失败，jobtracker 可以在另一个 tasktracker 节点上重新安排（reschedule）该任务。

MapReduce 1 中，jobtracker 关心作业安排（将任务与 tasktracker 匹配）和任务进度监控（保持跟踪任务、重启失败或迟缓的任务；记录任务记账（bookkeeping），如维护计数器的计数）。相比之下（By contrast），在YARN 中，这些责任是由独立的（separate）实体处理的：资源管理器和 application master（每个 MapReduce 作业有一个）。虽然为了卸下 jobtracker 的负载而运行一个作为独立守护线程的作业历史服务器是便捷的，但关于存储已完成作业的历史，jobtracker 也是有责任的。在 YARN 中，相等的（equivalent）角色是存储应用历史的时间线服务器（timeline）。

**Tip**：在 Hadoop 2.5.1 中，timeline依旧不存储 MapReduce 作业历史，仍需要
MapReduce 作业历史服务器守护线程。

在 YARN 中与 tasktracker 的相等的角色是节点管理器。映射关系被下表总结：

![1567602708294](E:\git_repo\Hao_Learn\2019\9\img\1567602708294.png)

###### 可扩展性（Scalability）

YARN 能在比 MapReduce 1 更的集群上运行。MapReduce 1 在4000节点和40000任务的区域中触及了可扩展性的阻碍，这个阻碍阻止（stem）了jobtracker 管理全部的作业和任务的事实。YARN 
通过分隔资源管理器和 application master 结构（architecture）优点（virtue）克服了这个限制：它被设计成扩展上限为10000节点和100000任务。

jobtracker正相反（In contrast），application 的每一个实例（这里指一个 MapReduce 作业）都有一个专用的（dedicated）application master ，该master 在 application 的持续时间内运行。这个模型实际上更为接近初始的 Google MapReduce 论文，论文中描述了如何启动一个 master 进程以协调运行在一系列工作（worker）上的 map 和 reduce 任务。

###### 可用性（Availability）

当服务守护进程失败时，通过为另一个守护进程复制接管工作所需的状态以便其继续提供服务，从而可以获得高可用性（High Availability，HA）。然而，jobtracker 内存中大量快速变化的复杂状态（例如，每个人物状态每几秒会更新一次）使得改进 jobtracker 服务获得高可用性非常困难。

YARN 策略：先为资源管理器提供高可用性，再为 YARN 应用（针对每个应用）提供高可用性。实际上，对于资源管理器和 application master，Hadoop 2 都支持 MapReduce 作业的高可用性。

###### 利用率（Utilization）

在 MapReduce 1 中，每个 tasktracker 都配置有若干固定长度的slot，这些 slot 是静态分配的，在配置的时候就被划分为 map slot 和 reduce slot。一个 slot 仅能同于运行一个任务。

在 YARN 中，一个节点管理器管理一个资源池，而不是指定的固定数目的 slot。YARN 上运行的 MapReduce 不会出现由于集群中仅有 map slot 可用导致 reduce 任务必须等待的情况，而 MapReduce 1 则会有这样的问题。如果能够获得运行任务的资源，那么应用就会正常进行。

更进一步，YARN 中的资源时精细化管理的，这样一个应用能够按需请求资源，而不是请求一个不可分割的、对于特定任务而要可能会太大（浪费资源）或太小（可能会导致失败）的 slot。

###### 多租户（Multitenancy）

YRAN向 MapReduce 以外的其他类型的分布式应用开放了 Hadoop。用户甚至可以在同一个 YARN 集群上运行不同版本的 MapReduce，这使得升级 MapReduce 的过程更好管理。

#### 4.3 YARN 的调度

YARN 调度器的工作就是根据既定策略为应用分配资源。

###### 调度选项

YARN 中有三种可用的调度器：FIFO调度器（FIFO Scheduler），容量调度器（Capacity Scheduler），公平调度器（Fair Scheduler）。

FIFO 调度器：将应用放置在一个队列中，然后按照提交的顺序（先进先出）运行应用。优点是简单易懂，不需要任何配置，但不适合共享集群。

在一个共享集群中，更适合使用容量调度器或公平调度器。这两种调度器都允许长时间运行的作业能及时完成。这两种调度器都允许长时间运行的作业能及时完成，也允许正在进行较小临时查询的用户能够在合理时间内得到返回结果。

![1567665984225](E:\git_repo\Hao_Learn\2019\9\img\1567665984225.png)

FIFO 调度器：后启动的小作业一直被阻塞，直至大作业完成。

容量调度器：一个独立的（separate）专用（dedicated）队列保证小作业一提交就可以启动。该策略牺牲了整个集群的利用率，即大作业的执行时间会比 FIFO 长。

公平调度器：在所有运行的作业之间动态平衡资源。但是在第二个作业启动到获得公平共享资源之间会有时间滞后（lag），因为它必须等待第一个作业使用的容器完全的（complete）释放资源。最终效果是：既得到了较高的集群利用率，又能保证小作业及时完成。

###### 容量调度器配置

Hadoop集群 -> 组织（一对多），组织分配到全部集群资源的一部分。
组织 -> 专门队列（一对一），队列使用一定的集群资源。
每个组织的不同用户能够共享该组织队列所分配的资源。
在一个队列内，使用 FIFO 调度策略对应用进行调度。

单个作业使用的资源不会超过其队列内容。

弹性队列（queue elasticity）：如果仍有可用的空闲资源，容量调度器可能会将空余的资源分配给队列中的作业。

缓解队列间抢占资源的方法是为队列设置一个最大容量限制。当然，这样做是以牺牲队列弹性为代价的，因此需要在不断尝试和失败中找到一个合理的折中。

范例 4-1.容量调度器的基本配置文件 capacity-scheduler.xml

```xml
<?xml version="1.0"?>
<configuration>
    <property>
        <name>yarn.scheduler.capacity.root.queues</name>
        <value>prod,dev</value>
    </property>
    <property>
        <name>yarn.scheduler.capacity.root.dev.queues</name>
        <value>eng,science</value>
    </property>
    <property>
        <name>yarn.scheduler.capacity.root.prod.capacity</name>
        <value>40</value>
    </property>
    <property>
        <name>yarn.scheduler.capacity.root.dev.capacity</name>
        <value>60</value>
    </property>
    <property>
        <name>yarn.scheduler.capacity.root.dev.maximum-capacity</name>
        <value>75</value>
    </property>
    <property>
        <name>yarn.scheduler.capacity.root.dev.eng.capacity</name>
        <value>50</value>
    </property>
    <property>
        <name>yarn.scheduler.capacity.root.dev.science.capacity</name>
        <value>50</value>
    </property>
</configuration>
```

由于 dev 队列的最大容量被设置为 75%，因此即使 prod 队列空闲，dev 也不会占用全部集群资源。由于没有对其他队列设置最大容量限制，eng 或 science 中的作业可能会占用 dev 队列的所有容量，而 prod 队列实际则可能会占用全部集群资源。

**队列放置**

将应用放置在哪个队列中，取决于应用本身。例如，在 MapReduce 中，可以通过设置属性 mapreduce.job.queuename 来指定要用的队列。如果队列不存在，则在提交时会发送错误。如果不指定队列，那么应用将被放在一个名为 default 的默认队列中。

**Tip**：对于容量调度器，队列名应该是层次结构名的最后一部分，因为全部的层次结构名是不能被识别的。例如，对于上述配置范例，prod 和 eng 是合法的队列名，但 root.dev.eng 和 dev.eng 作为队列名是无效的。

###### 公平调度器配置

公平调度器旨在为所有运行的应用公平分配资源。

![1567671792914](E:\git_repo\Hao_Learn\2019\9\img\1567671792914.png)

1. 启用公平调度器

默认是使用容量调度器（尽管在一些 Hadoop 分布式项目，如 CDH 中，默认使用公平调度器），如果要使用公平调度器，需要将`yarn-site.xml`文件中的`yarn.resourcemanager.scheduler.class`设置为公平调度器的完全限定名：`org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler`

2. 队列配置

通过一个名为 fair-scheduler.xml  的分配文件对公平调度器进行配置，该文件位于类路径下（可以通过设置属性 `yarn.scheduler.fair.allocation.file`来修改文件名）。当没有该分配文件时，公平调度器的工作策略同先前所描述的一样：每个应用放置在一个以用户名命名的队列中，队列是在用户提交第一个应用是动态创建的。

通过分配文件可以为每个队列进行配置。这样允许对容量调度器支持的层次队列进行配置。

范例 4-2.公平调度器的分配文件：

```xml
<?xml version="1.0"?>
<allocations>
    <defaultQueueSchedulingPolicy>fair</defaultQueueSchedulingPolicy>
    <queue name="prod">
        <weight>40</weight>
        <schedulingPolicy>fifo</schedulingPolicy>
    </queue>
    <queue name="dev">
        <weight>60</weight>
        <queue name="eng" />
        <queue name="science" />
    </queue>
    <queuePlacementPolicy>
        <rule name="specified" create="false" />
        <rule name="primaryGroup" create="false" />
        <rule name="default" queue="dev.eng" />
    </queuePlacementPolicy>
</allocations>

```

队列的层次使用嵌套 queue 元素来定义。所有的队列都是 root 队列的孩子，即使实际上并没有嵌套进 root queue 元素里。

队列中有权重元素，用于公平共享计算。集群认为按照权重比例分配是公平的，否则会按平均分配。权重并不是百分百，若用 2：3 代替例子中的 40：60，效果是一样的。

**Tip**：当设置权重时，要考虑默认队列和动态创建的队列（例如以用户名命名的队列）。虽然没有在分配文件中为它们指定权重，但它们仍有值为 1 的权重。

每个队列可以有不同的调度策略。队列的默认调度策略可以通过顶层元素 defaultQueueSchedulingPolicy 进行设置，如果省略，默认使用公平调度。

使用 schedulingPolicy 可以给队列设置指定的策略。在上述例子中，由于希望每个生产性作业能够按顺序运行且在最短可能的时间内结束，所以 prod 队列使用了 FIFO 调度策略。

每个队列可配置最大/最小资源数量及最大可运行的应用数量。其中，最小资源数不是一个硬性的限制，但是调度器常用它对资源分配进行有限排序。即如果两个队列的资源都低它们的公平共享额度，那么最远低于最小资源数量的那个队列优先被分配资源。

3. 队列放置

公平调度器使用一个基于规则的系统来确定应用应该放到哪个队列。在范例 4-2 中，queuePlacementPolicy 元素包含了一个规则列表，每条规则会被依次尝试直到匹配成功。

specified 表示把应用放进所指明的队列中，没有则不匹配。
primaryGroup 会试着把应用放在以用户的主 Unix 组名命名的队列中，没有则不匹配。
default 是一条底线，之前的规则都不匹配时启用，把应用放进指定的队列中。

忽略 queuePlacementPolicy 元素时的默认队列放置为：

```xml
<queuePlacementPolicy>
	<rule name="specified" />
	<rule name="user" />
</queuePlacementPolicy>
```

换言之，除非明确定义队列，否则必要时会以用户名为队列名创建队列。

另一个简单的队列放置策略是将所有应用放进 default 中，这样可以在应用间公平共享资源，而不是在用户之间共享。这等价于：

```xml
<queuePlacementPolicy>
	<rule name="default" />
</queuePlacementPolicy>
```

通过将属性 yarn.scheduler.fair.user-as-default-queue 设置为 false 也可以做到上述策略的效果，而且不需要使用分配文件。另外，将 yarn.scheduler.fair.user-as-default-queue 设置为 false，用户便不能随意创建队列了。

4. 抢占

由于新提交给空队列的作业需要等集群上已经运行的作业释放资源之后才会启动，所以公平调度器提供了抢占（preemption）功能，用于预测作业从提交到执行所需的时间。

所谓抢占，就是允许调度器终止那些占用资源超过了其公平共享份额的队列的容器，这些容器资源释放后可以分配给资源数量低于应得份额的队列。注意，抢占会降低整个集群的效率，因为被终止的 containers 需要重新执行。

通过将 yarn.scheduler.fair.preemption 设置为 true，可以全面启用抢占功能。有两个相关的抢占超时设置：一个用于最小共享（minimum share preempted timeout），另一个用于公平共享（fair share preempted timeout），两者设定时间均为秒级。默认情况下，两个超时参数均不设置，但为了允许抢占，至少要设置其中一个。

如果队列在 minimum share preempted timeout 指定的时间内未获得被承诺的最小共享资源，调度器就会抢占其他容器。可以通过分配文件中的顶层元素 defaultMinSharePreemptionTimeout 为所有队列设置默认的超时时间，还可以通过设置每个队列的 minSharePreemptionTimeout 元素来为单个队列设置指定超时时间。

如果队列在 fair share preempted timeout 指定的时间内获得的资源仍然低于其公平共享份额的一半，那么调度器就会抢占其他容器。可以通过分配文件中的顶层元素defaultFairSharePreemptionTimeout 为所有队列设置默认的超时时间，还可以通过设置每个队列的 fairSharePreemptionTimeout 元素来为单个队列指定超时时间。

通过设置 defaultFairSharePreemptionThreshold 和 fairSharePreemptionThreshold 可以修改超时阈值，默认值是0.5。

###### 延迟调度

所有的 YARN 调度器都试图以本地请求为重。在一个繁忙的集群上，如果一个应用请求某个节点，那么极有可能此时有其他容器正在该节点上运行。最明显的做法是立即放宽本地要求，在同一 rack 上分配一个容器。然而，通过实践发现，等待很短的时间（不超过几秒），可以显著的增加在请求节点上分配容器的机会，从而提高集群的效率。这个特性称之为延迟调度（delay scheduling）。容器调度器和公平调度器都支持延迟调度。

YARN 中每个节点管理器周期性的（默认每秒一次）向资源管理器发送心跳请求。心跳中携带了节点管理器中正运行的容器、新容器可用的资源等信息，所以对于一个应用运行一个容器而言，每个心跳就是一个潜在的（potential ）调度机会（scheduling opportunity）。

当使用延迟调度时，调度器不会简单的使用它收到的第一个调度机会，而是在放宽本地限制并接受下一个调度机会之前，等待指定的最大数目的调度机会发生。

对于容量调度器，可以设置 yarn.scheduler.capacity.node-locality-delay 来配置延迟调度。设置为正整数，表示调度器在放宽节点限制、改为匹配同一 rack 上的其他节点前，准备错过的调度机会的数量。

公平调度器也使用调度机会的数量来决定延迟时间，尽管它表示为集群大小的比例。例如将  yarn.scheduler.fair.locality.threshold.node 设置为 0.5，表示调度器在接受同一机架中的其他节点之前，将一直等待直到集群中的一半节点都已经给过调度机会。而 yarn.scheduler.fair.locality.threshold.rack 表示在接受另一个机架替代所申请的机架之前需要等待的时长阈值。

###### 主导资源公平性

YARN 中调度器解决多种资源调度问题的思路是，观察每个用户的主导资源。并将其作为对集群资源使用的一个度量，即“主导资源公平性”（Dominant Resource Fairness，DRF）。

应用请求的每份容器资源占据对应集群总资源的比值决定了应用的主导资源。

应用之间的主导资源比值决定了它们在公平调度下获得的容器数比值。

默认情况下不用DRF，因此在资源计算期间，只需考虑内存，不需考虑CPU。将 capacity-scheduler.xml 文件中的`org.apache.hadoop.yarn.util.resource.DominantResourceCalculator`设为`yarn.scheduler.capacity.resource-calculator`即可在容器调度器中使用 DRF；将分配文件中的顶层元素 defaultQueueSchedulingPolicy 设为 drf 即可在公平调度器中使用 DRF。

## 第5章 Hadoop 的 I/O 操作

#### 5.1 数据完整性



















 