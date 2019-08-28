// cc MaxTemperature Application to find the maximum temperature in the weather dataset
// vv MaxTemperature
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
// ^^ MaxTemperature
