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
     * 这个限制意味着如果程序的其他组件声明了一个UrlStreamHandlerFactory实例，
     * 则将无法再次使用这种方法从Hadoop中读取数据。
     */
    URL.setURLStreamHandlerFactory(new FsUrlStreamHandlerFactory());
  }
  
  public static void main(String[] args) throws Exception {
    InputStream in = null;
    try {
      in = new URL(args[0]).openStream();
      /**
       * 调用Hadoop中简洁的IOUtils类，并在finally字句中关闭数据流，
       * 同时也可以在输入/输出流之间复制数据。copyBytes的最后两个参数，
       * 第一个设置用于复制的缓冲区大小，第二个设置复制结束后是否关闭数据流。
       */
      IOUtils.copyBytes(in, System.out, 4096, false);
    } finally {
      IOUtils.closeStream(in);
    }
  }
}
// ^^ URLCat
