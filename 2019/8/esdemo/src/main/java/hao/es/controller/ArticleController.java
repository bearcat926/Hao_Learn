package hao.es.controller;

import cn.hutool.core.util.RandomUtil;
import com.alibaba.fastjson.JSONObject;
import lombok.extern.slf4j.Slf4j;
import org.elasticsearch.index.query.BoolQueryBuilder;
import org.elasticsearch.index.query.QueryBuilder;
import org.elasticsearch.index.query.QueryBuilders;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.elasticsearch.core.ElasticsearchTemplate;
import org.springframework.data.elasticsearch.core.query.NativeSearchQuery;
import org.springframework.data.elasticsearch.core.query.NativeSearchQueryBuilder;
import org.springframework.data.web.PageableDefault;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import hao.es.entity.Article;
import hao.es.repository.ArticleRepository;


import java.util.Date;
import java.util.List;

/**
 * Created by hao hao on 2019/8/12 0012.
 */
@RestController
@Slf4j
public class ArticleController {
    @Autowired
    private ElasticsearchTemplate elasticsearchTemplate;

    @Autowired
    private ArticleRepository articleRepository;

    @GetMapping("new")
    public JSONObject newArticle(@RequestParam(defaultValue = "SpringBootElasticSearch") String title, @RequestParam(defaultValue = "`Elasticsearch` 是一个`开源`的`分布式`、`高扩展`、`高实时`的RESTful `搜索和分析引擎`，基于`Lucene`......") String text){
        //构建并保存Article
        Article article = new Article();
        article.setId(RandomUtil.randomInt(10000,99999));
        article.setTitle(title);
        article.setText(text);
        article.setCreatetime(new Date());
        article.setAuthor("hao hao");
        log.info("new > {}",article.getId());

        JSONObject result = new JSONObject();
        result.put("data",article);
        return  result;
    }

    @GetMapping("save")
    public Object save(@RequestParam(defaultValue = "SpringBootElasticSearch") String title, @RequestParam(defaultValue = "`Elasticsearch` 是一个`开源`的`分布式`、`高扩展`、`高实时`的RESTful `搜索和分析引擎`，基于`Lucene`......") String text){
        //构建并保存Article
        Article article = new Article();
        article.setId(RandomUtil.randomInt(10000,99999));
        article.setTitle(title);
        article.setText(text);
        article.setCreatetime(new Date());
        article.setAuthor("hao hao");
        articleRepository.save(article);
        log.info("save > {}",article.getId());

        JSONObject result = new JSONObject();
        result.put("data",article);
        return  result;
    }

    /**
     * ElasticSearch之Search封装查询
     * @author  hao hao
     * @param title   搜索标题
     * @param pageable page = 第几页参数(第一页是0), value = 每页显示条数
     */
    @GetMapping("search")
    public Object search(@RequestParam(defaultValue = "Spring Boot") String title, @PageableDefault(page = 0, value = 10) Pageable pageable){
        //以下查询等同于封装了{"query":{"bool":{"must":[{"wildcard":{"title.keyword":{"wildcard":"*SpringBoot*","boost":1}}}],"disable_coord":false,"adjust_pure_negative":true,"boost":1}}}
        //按标题进行模糊查询
        QueryBuilder queryBuilder = QueryBuilders.wildcardQuery("title.keyword", "*"+title+"*");
        //按照顺序构建builder,bool->must->wildcard ,有了上文的JSON,顺序就很好理解了
        BoolQueryBuilder must = QueryBuilders.boolQuery().must(queryBuilder);
        //封装pageable分页
        Page<Article> queryResult =  articleRepository.search(must,pageable);

        log.info("search ,查询结果为 {} 条",queryResult.getNumber());

        //返回
        JSONObject result = new JSONObject();
        result.put("data",queryResult.getContent());
        return  result;
    }
    /**
     * ElasticSearch之elasticsearchTemplate查询
     * @author  hao hao
     * @param title   搜索标题
     */
    @GetMapping("originSearch")
    public Object originSearch(@RequestParam(defaultValue = "SpringBoot") String title) {
        BoolQueryBuilder boolQuery = QueryBuilders.boolQuery();
        QueryBuilder queryBuilder = QueryBuilders.wildcardQuery("title.keyword", "*SpringBoot*");
        BoolQueryBuilder must = boolQuery.must(queryBuilder);
        NativeSearchQueryBuilder nativeSearchQueryBuilder = new NativeSearchQueryBuilder();
        NativeSearchQuery build = nativeSearchQueryBuilder.withQuery(must).build();
        List<Article> queryForList = elasticsearchTemplate.queryForList(build, Article.class);
        log.info("originSearch ,查询结果为 {} 条",queryForList.size());
        JSONObject result = new JSONObject();
        result.put("data",queryForList);
        return  result;
    }
}
