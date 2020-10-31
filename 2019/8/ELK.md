 # ELK

## Elasticsearch之开启外网访问
```
#修改elasticsearch.yml
vi /opt/elasticsearch-6.8.1/config/elasticsearch.yml

#设定绑定的ip
network.host: 172.16.42.3
```

## 停止kibana
**原因：**
kibana启动后通过`jps`或`jobs`找不到对应的PID
**解决方法：**
可以通过`ps -ef|grep node`命令或`netstat -anltp|grep 5601`查找对应端口，最后`kill`掉对应端口的 pid 就可以了

## 远程访问kibana界面被拒绝
linux搭建kibana环境后，远程访问，被拒绝

解决办法：
1. 检查端口是否开放；
2. 修改config下面的配置文件，因为Kibana 6.x 默认占用的地址是localhost(127.0.0.1)，将`kibana-6.8.1-linux-x86_64/config/kibana.yml`下的`server.host: "localhost" `更改为`server.host: "0.0.0.0" `就可以了，顺便改了`elasticsearch.hosts: ["http://172.16.42.3:9200"]`，还能解决找不到节点的问题

## 配置 Logstash 为 Windows Service
使用(NSSM)[https://nssm.cc/usage?spm=a2c4g.11186623.2.12.7bd0825alReC5q]

## ElasticSearch 安装报错整理

#### 单机安装报错

**初次启动服务**

当使用root账户调用启动命令出现错误信息，错误提示信息如下：

```
[2017-08-30T13:32:17,003][WARN ][o.e.b.ElasticsearchUncaughtExceptionHandler] [ELK-node1] uncaught exception in thread [main]
org.elasticsearch.bootstrap.StartupException: java.lang.RuntimeException: can not run elasticsearch as root
    at org.elasticsearch.bootstrap.Elasticsearch.init(Elasticsearch.java:127) ~[elasticsearch-5.5.2.jar:5.5.2]
    at org.elasticsearch.bootstrap.Elasticsearch.execute(Elasticsearch.java:114) ~[elasticsearch-5.5.2.jar:5.5.2]
    at org.elasticsearch.cli.EnvironmentAwareCommand.execute(EnvironmentAwareCommand.java:67) ~[elasticsearch-5.5.2.jar:5.5.2]
    at org.elasticsearch.cli.Command.mainWithoutErrorHandling(Command.java:122) ~[elasticsearch-5.5.2.jar:5.5.2]
    at org.elasticsearch.cli.Command.main(Command.java:88) ~[elasticsearch-5.5.2.jar:5.5.2]
    at org.elasticsearch.bootstrap.Elasticsearch.main(Elasticsearch.java:91) ~[elasticsearch-5.5.2.jar:5.5.2]
    at org.elasticsearch.bootstrap.Elasticsearch.main(Elasticsearch.java:84) ~[elasticsearch-5.5.2.jar:5.5.2]
Caused by: java.lang.RuntimeException: can not run elasticsearch as root
    at org.elasticsearch.bootstrap.Bootstrap.initializeNatives(Bootstrap.java:106) ~[elasticsearch-5.5.2.jar:5.5.2]
    at org.elasticsearch.bootstrap.Bootstrap.setup(Bootstrap.java:194) ~[elasticsearch-5.5.2.jar:5.5.2]
    at org.elasticsearch.bootstrap.Bootstrap.init(Bootstrap.java:351) ~[elasticsearch-5.5.2.jar:5.5.2]
    at org.elasticsearch.bootstrap.Elasticsearch.init(Elasticsearch.java:123) ~[elasticsearch-5.5.2.jar:5.5.2]
    ... 6 more
```

**创建新用户**
由于Elasticsearch可以接收用户输入的脚本并且执行，为了系统安全考虑，不允许root账号启动，所以建议给Elasticsearch单独创建一个用户来运行Elasticsearch。
```shell
groupadd elk
#useradd [用户名] -g [所属组名] -p [密码]
useradd  elk -g elk -p elk
```

**授权访问组权限**

```shell
#chown -R [所属用户] : [所属用户组名] [要更改的文件路径]
chown -R elk : elk /opt/elasticsearch-6.8.1
chmod -R 777 /opt/elasticsearch-6.8.1
```

**授权 root 权限**

```shell
chmod 777 /etc/sudoers
vi /etc/sudoers
```
```shell
root    ALL=(ALL)       ALL

#给用户elk添加root权限，NOPASSWD即不用输密码
elk     ALL=(ALL)       NOPASSWD:ALL 
```
```shell
pkexec chmod 0440 /etc/sudoers
su elk
/opt/elasticsearch-6.8.1/bin/elasticsearch
```

**如果报如下错误，都切换到 root 用户进项修改：**

```
[1]: max file descriptors [4096] for elasticsearch process is too low, increase to at least [65536]
```
```shell
vi /etc/security/limits.conf 

#添加如下内容
* soft nofile 65536
* hard nofile 131072
* soft nproc 4096
* hard nproc 4096
```

-------------------

```
[2]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
```
```shell
vi /etc/sysctl.conf 

#在第一行加上如下内容
vm.max_map_count = 655360

# 执行
sysctl -p
```

-------------------
```java
//异常 IllegalStateException
Caused by: java.lang.IllegalStateException: failed to obtain node locks, tried [[/opt/elasticsearch-5.5.2/data/ymq]] with lock id [0]; maybe thes
//异常 RemoteTransportException
[2017-09-01T11:40:42,115][INFO ][o.e.d.z.ZenDiscovery     ] [ELK-node2] failed to send join request to master [{ELK-node1}{DKCwxkubTFufsBaOSXj9Nw}{UIMSNeuIT6m8SFGGTi4wSg}{192.168.252.121}{192.168.252.121:9300}], reason [RemoteTransportException[[ELK-node1][192.168.252.121:9300][internal:discovery/zen/join]]; nested: NotMasterException[Node [{ELK-node1}{DKCwxkubTFufsBaOSXj9Nw}{UIMSNeuIT6m8SFGGTi4wSg}{192.168.252.121}{192.168.252.121:9300}] not master for join request]; ], tried [3] times
```
```shell
#删除安装目录下的data
cd /opt/elasticsearch-6.8.1/data
rm -rf nodes
```

--------------------------

```java
//异常 ElasticsearchUncaughtExceptionHandler
//上次启动失败，占用了端口
[2017-08-30T22:02:14,463][WARN ][o.e.b.ElasticsearchUncaughtExceptionHandler] [ELK-node2] uncaught exception in thread [main]
org.elasticsearch.bootstrap.StartupException: BindHttpException[Failed to bind to [9200]]; nested: BindException[Address already in use];
```
```shell
jps 
2824 Elasticsearch
3165 Jps

kill -9 2824
```

-----------------------

```shell
#再次启动服务
su elk
/opt/elasticsearch-6.8.1/bin/elasticsearch  -d
#或者
cd /opt/elasticsearch-6.8.1
nohup bin/elasticsearch &
```

```shell
#jvm 内存内存修改
vi /opt/elasticsearch-6.8.1/config/jvm.options

#-Xms2g  修改为512m
#-Xmx2g  修改为512m

```
```shell
# 查看日志
less /opt/elasticsearch-6.8.1/logs/elk.log

```

## Elasticsearch 中文分词器配置

#### IK分词器

![1565774605270](E:\git_repo\Hao_Learn\2019\8\img\1565774605270.png)


## Elasticsearch 集群入门

![1565926699724](E:\git_repo\Hao_Learn\2019\8\img\1565926699724.png)

#### 索引管理

###### 创建索引
使用PUT方法加索引名的方式进行创建，且索引名称中不能出现大写字母，否则会报一个非法的索引名异常`invalid_index_name_exception`。
成功之后会响应以下消息：
```
{
	"acknowledged":true,
	"shards_acknowleged":true
}
```
索引的分片数一经指定后就不能再修改，副本数可以通过命令随时修改。
以创建3个分片0个副本命为blog的索引为例，命令如下：

```
PUT blog
{
	"setting":{
		"number_of_shards": 3,
		"number_of_replicas": 0
	}
}
```

###### 更新副本：

```
PUT blog/_settings
{
	"number_of_replicas": 2
}
```

###### 对索引的读写操作进行限制
下面是读写权限的参数：
- blocks.read_only:true	  设置当前索引值允许读不允许写或者更新。
- blocks.read:true		       禁止对当前索引进行读操作
- blocks.write:true		      禁止对当前索引进行写操作

违反设置之后会报索引锁定异常 `cluster_block_exception`，恢复索引的权限，只需把对应的属性设置为false即可。

###### 查看索引：
使用GET方法加上`_setting`参数可以查看一个索引的所有配置信息。

同时查看多个索引的setting信息，命令如下：
`GET [索引名1],[索引名2].../_settings`
查看集群中所有索引的setting信息，命令如下：
`GET _all/_settings`

###### 删除索引：
使用DELETE方法加 索引名 即可删除索引，一旦执行删除操作索引中的文档就不复存在，注意在删除重要数据之前做好备份工作。

如果删除成功，会有一下响应：
```
{
	"acknowledged":true
}
```
如果删除的索引名不存在，会报索引未找到异常`index_not_found_exception`。

###### 索引的打开与关闭
Elasticsearch 中的索引可以进行打开和关闭操作，一个关闭了的索引几乎不占用系统内存。
索引关闭后，Head插件中会显示关闭状态的索引，已关闭的索引不能进行读写操作。
索引打开/关闭的命令如下（可同时操作多个索引）：
```
POST [索引名1],[索引名2].../_open
POST [索引名1],[索引名2].../_close
```
如果Elasticsearch集群中不存在开启/关闭请求中的全部索引，将会抛出索引不存在错误，此时可以通过`ignore_unavailable`参数来操作只存在的索引，命令如下
`POST [索引名1],[索引名2].../_close?ignore_unavailable=true`
支持通配符和`_all`：
关闭集群中所有索引的命令如下： 
`POST _all/_close`
关闭以 test 开头的索引：
`POST test*/_close`

###### 复制索引
`_reindex`可以把文档从一个索引（源索引）复制到另一个索引（目标索引），目标索引不会复制源索引中的配置信息，`_reindex`操作之前需要摄者目标索引的分片数、副本数等信息，命令如下：
```
POST _reindex
{
	"source":{"index":"[旧索引名]"},
	"dest":{"index":"[新索引名]"}
}
```
上述命令会把源索引中的所有文档都复制到目标索引中，也可以在源索引中增加type和query来限制文档：
```
POST _reindex
{
	"source":{
		"index":"[旧索引名]"
		"type":"[类型]",
		"query":{
			"term":{"title":"[关键字]"}
		}
	},
	"dest":{"index":"[新索引名]"}
}
```

###### 收缩索引
一个索引的分片初始化以后是无法再做修改的，但可以使用 `shrink index`提供的缩小索引分片数机制，把一个索引变成一个更少分片的索引，但是收缩后的分片数必须是原始分片数的因子，比如有8个分片的索引可以收缩为4、2、1，如果分片数为素数（7、11等），那么只能收缩为1个分片。
收缩索引之前，索引中的每个分片都要在同一个节点上。收缩索引的完成过程如下：
1. 创建一个新的目标索引，设置与源索引相同，但新索引的分片数量较少。
2. 把源索引硬链接到目标索引。（如果文件系统不支持硬链接，那么所有段都被复制到新索引中，这个一个耗费更多时间的过程。）
3. 新的索引恢复使用。

在缩小索引之前，索引必须被标记为只读，所有分片都会复制到一个相同节点并节点健康值为绿色的。这个两个可以通过下列请求实现，命令如下：
```
PUT [索引名]/_settings
{
	"index_routing.allocation.require._name":"shrink_node_name",
	"blocks.write:true": true
}
```
在收缩时可指定目标索引的分片数、副本数等配置信息，命令如下：
```
PUT [旧索引名]/_shrink/[新索引名]
{
	"setting":{
		"index.number_of_replicas": 0,
		"index.number_of_shards": 1,
		"index.codec":"best_compression"
	},
	"aliases":{
		"my_search_indices":{}
	}
}
```
###### 索引别名

索引别名就是给一个索引或者多个索引起的另一个名字。命令如下

```
POST /_aliases
{
	"actions":[
		{"add":{"index":"[索引名]","alias":"[别名]"}}，
		{"add":{"indices":["[索引名1]","[索引名2]..."],"alias":"[别名]"}}，
		{"remove":{"index":"[索引名]","alias":"[别名]"}}，
		{"remove":{"indices":["[索引名1]","[索引名2]..."],"alias":"[别名]"}}，
		
	]
}
```

设置别名之后，对别名进行操作等价于对索引进行操作。
需要注意的是，如果别名和索引是一对一的，使用别名索引文档或者根据ID查询文档是可以的，但是如果别名和索引是一对多的，使用别名会发生错误，提示`illegal_argument_exception`，因为Elasticsearch不知道把文档写入哪个索引中去或者从哪个索引中读取文档。

Elasticsearch还支持通过通配符同时给多个索引设置别名。

如果想要查看某一个索引的别名或者某一个别名对应哪些索引的别名，可执行下列命令：
`GET /[索引名/别名]/_aliases`
查看Elasticsearch集群上所有的可用别名，执行命令：
`GET _aliases`

#### 文档管理

###### 新建文档

使用PUT创建文档，命令如下：
```
PUT [索引名]/[类型名]/[id]
{
	"字段名1":"字段值1",
	...
}
```
如果不指定id，则需要使用POST方法创建文档，使用PUT方法会出现异常，id是自动生成的字符串。

###### 获取文档
使用GET命令并指定文档所在的索引、类型和 id 即可返回一个JSON格式的文档，命令如下：
`GET [索引名]/[类型名]/[id]`

![1565927216910](E:\git_repo\Hao_Learn\2019\8\img\1565927216910.png)

返回结果中前四个属性表面文档的位置和版本信息，`found`属性用于表明是否查询到文档，`_source`字段中是文档的内容。

如果查看的文档不存在，则`found`属性值会为false，也没有版本信息和`_source`。

使用HEAD命令可以检查一个文档是否存在，命令如下：
`HEAD [索引名]/[类型名]/[id]`
存在则返回 `200 - OK`，反之返回 `400 - Not Found`。

如果想根据id一次获得多个文档，可以是用Multi GET API 根据索引名、类型名、id（或者路由）一次获取多个文档，返回一个文档数组。
p136

=== > 第八章 Java API

p247

------------------------

## ELK系统架构概述

使用ELK处理数据的前提：非敏感、不重要 

ELK是日志收集、存储、可视化的一套解决方案。
- Elasticsearch：易于部署（最小配置），垂直和水平缩放、API易于使用、对于大多数编程/脚本语言都可以模块化、好的在线文档、免费，支持Python API进行查询，使用JSON语言进行大量查询和过滤选项
- Logstash：类似于Flume，收集日志的。包含的日志数据源：window event logs、syslog、Bro(session data/dpi)、SiLK(flow)、SNMP()、PCAP(stored on disk,index information in ES )
- Kibana：可视化（类似于R语言），图表等。
总结，ELK具有以下特点：
1. 批量分析
2. 数据集关联
3. 生成图标进行显示
4. 报警，使用Python/R

------------------------

Flume + Kafka：高可用，存储量大，有数据缓冲功能的日志收集系统。Agent：Source（源）、channel（管道）、Sink（下沉）

ELK的关系 
Logstash(collect) ---> Elasticsearch(storage + index + search) ---> kibana(view)
flume                    ---> Kafka                                                            ---> R

FileBeat，类似于Flume中的 spooldir组件	



-------------------------------------------

Nginx整合Kibana

1. 添加epel仓库
>sudo yum -y install epel-release

2. 安装nginx和httpd-tools软件包
>sudo yum -y install nginx httpd-tools

3. 通过htpasswd命令创建访问kibana webui的账号
>sudo htpasswd -c /usr/local/nginx/htpasswd.users kibanaadmin

4.修改Nginx配置文件

>vi /usr/local/nginx/conf/nginx.conf