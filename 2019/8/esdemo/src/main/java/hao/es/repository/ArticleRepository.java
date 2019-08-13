package hao.es.repository;

import hao.es.entity.Article;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;
import org.springframework.stereotype.Repository;


/**
 * Created by hao hao on 2019/8/12 0012.
 */
@Repository
public interface ArticleRepository extends ElasticsearchRepository<Article, Integer> {

}
