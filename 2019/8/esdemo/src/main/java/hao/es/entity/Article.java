package hao.es.entity;

/**
 * Created by hao hao on 2019/8/12 0012.
 */
import java.util.Date;
import org.springframework.data.annotation.Id;
import org.springframework.data.elasticsearch.annotations.Document;
import lombok.Data;

@Data
@Document(indexName = "article_info", type = "doc")
public class Article {
    @Id
    private Integer id;

    private String title;

    private String text;

    private Date createtime;

    private String author;

}
