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
