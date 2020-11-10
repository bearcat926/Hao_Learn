1-2

- 【3小时】南京大学项目专利报账第二阶段功能 - 分析专利报账第二阶段功能的开发流程及需要时间
- 【5小时】南京大学项目专利报账第二阶段功能 - 解决专利报账功能开发后数据库数据问题导致的场景错误

1-3

- 【3小时】南京大学项目专利报账第二阶段功能 - 开始开发级联展示费用科目功能
- 【5小时】南京大学项目专利报账第二阶段功能 - 完成级联展示费用科目的开发


遇到的问题并解决：


总结：

    适逢元旦，本周工作量不算大，主要是数据处理的问题比较多，比较繁琐需要耐心


bug：

1. 场景子表缺少主键导致可插入多条 -> 查看场景时会出现错误


===============================

1-6

- 【3小时】南京大学项目专利报账第二阶段功能 - 专利费用科目模块（创建了临时专利类型数据字典，不使用原本的专利类型字典）及审核通过后生成凭单号的功能
- 【6小时】南京大学项目专利报账第二阶段功能 - 开发流水号模块用于流水号报账中凭单号的生成；手动填写申请号时需进行规则校验

1-7

- 【2小时】南京大学项目专利报账第二阶段功能 - 阅读打印案例的代码
- 【6.5小时】南京大学项目专利报账第二阶段功能 - 开发专利报账的打印建账单功能

导出SQL
-- 1.模块管理：专利报账，专利报账费用
-- 2.模块分类：专利报账，专利报账费用
-- 3.菜单配置：专利报账列表    
-- 4.元数据：专利报账，专利报账费用
-- 5.数据字典：专利费用类型
-- 6.角色菜单分配
-- 7.场景：提案查找；专利报账，专利报账费用

经费卡号从经费卡表中带出，经费卡负责人必须是申请人本人

经费卡号带出规则，所有经费卡号都可以选择，暂不限制
经费卡号余额不能大于报账总额（财务对接后体现该限制）

1-8

- 【3小时】南京大学项目专利提案模块 - 梳理打印申请表的业务
- 【5小时】南京大学项目专利提案模块 - 开发并测试打印申请表

1-9

- 【3小时】修改专利报账的代理公司部分，添加报账单字体设置；提交功能更新SQL文件
- 【5小时】
    1. 重名人员没有标记 -> 配置字典，修改Patent类的AllAuthor字段的查询SQL
    2. 认领后成员丢失 -> 维护关联关系的代码被注释，取消注释后恢复正常
    3. 不应存在校内老师单位信息不存在的记录 -> 原本认领部分的代码逻辑有误，修改成从对接后的数据库中拿取作者信息
    4. 费用科目列表的排序问题 -> 添加ORDERID字段（int）用于排序 -> 修改实体类 -> 添加元数据 -> 修改相关场景 

1-10

- 【3小时】软件著作权建账模块 - 著作权建账模块数据库设计和业务
- 【5小时】软件著作权建账模块 - 著作权建账模块接口和页面开发；解决专利报账不在菜单中显示的问题

===============================

1-14

- 【3小时】软件著作权建账模块 - 著作权建账模块根据需求修改数据库字段，根据著作权模块带出著作信息
- 【5小时】软件著作权建账模块 - 打印建账单功能

1-15

- 【5小时】软件著作权建账模块 - 确定不明确的业务需求并修改代码

问题：
    关于申请人，申请时间和完成人字段：
    1. 申请人字段是著作权人 
    2. 申请日期？  著作权加字段
    3. 完成人需要字段 打印时不要区分 显示完成人  
    4. 证书获得日期是出版日期吗？ 是
    5. 经办人是否是当前用户？ 是
    6. 申请单位(签章)的电子是什么意思？当前处理方式是留空，这样合理吗？ 留空
    7. 总金额需要js自动计算吗？需要

导出SQL：

0. 表（本地库复制时丢失主键需要补充）：SERIAL_NUMBER（模块流水号），BIZ_COPY_RIGHT（新加了两个字段）,BIZ_COPY_RIGHT_ACCOUNT
1. 模块配置：著作权（新加了两个字段），著作权建账
2. 模块分类: 著作权建账（根据正式库分类sql确定目录顺序）
3. 字典：PRODUCT_TYPE
6. 角色管理：科研人员，秘书，管理员


问题：
    专利提案在审核通过之后是有流水号的，但是这流水号当前是四位的，而申请单上的例子是六位的，需不需要改成六位

1-16

- 【3小时】导出软著建账的相关SQL（过程中出现表丢失主键问题，已解决）及专利相关优化的SQL
- 【5小时】与张森确认上线功能，出现SQL版本不同导致的场景错误问题，梳理并修改SQL后解决

1-17

- 【3小时】处理数据库文件，获取历史表
- 【5小时】修复更新定时任务更新发明人时，重名人员的署名顺序都为1的BUG

任务：

1、根据历史数据初始化专利库数据的所属单位（需要解决当前专利库问题1）

2、根据历史数据明确专利的第一发明人信息的职工号，绑定具体的人员。（历史表中无人员表信息，只能按原逻辑处理）

3、导入历史专利报账数据（完成）

4、导入历史专利申请数据（完成）

历史表问题：
1. 申请号中, . / 空格 - 删除；还有首位PCT、ZL、CN、EP、US、JP、Au、中文的情况
2. 有两条数据的所属单位为系统管理员
3. 历史表，表名中有'-'的表作用不明确
4. 没有申请号的数据(640条)

当前专利库问题：
1. 第一发明人为教师但是并未更新署名的专利字段 -> 当前专利作者表中的原始数据所属单位ID错误，原因是BIZ_UNIT表修改过部分所属单位的ID
2. 名称重复的专利(当前专利库) 752条

bug：定时任务更新发明人时，重名人员的署名顺序都为1

完成效果：
1. 把历史数据转移到新表，确保数据不丢失
2. 确保作者数据可被管理角色（个人、秘书、管理员）查询，通知 -> 保证人员与作者关联
3. 无法确认关联关系的数据需要进行记录

需要使用代码完善的部分：
FIRST_AUTHOR_ID, FIRST_AUTHOR_NAME, FIRST_AUTHOR_ACCOUNT
专利提案：INVENTOR_ID, INVENTOR , ACCEPTED_STATE（有申请号，则yes）, AGENT_TYPE(ACGENCY_NAME);作者
专利报账费用

1-19

- 【3小时】分析历史库数据，编写相关SQL
- 【5小时】分析历史库数据，编写相关SQL

1-20

- 【5小时】分析历史库数据，编写相关SQL

1-21

- 【3小时】开始任务 - 导入历史专利报账数据
- 【5小时】完成任务 - 导入历史专利报账数据; 开始任务 - 导入历史专利申请数据

1-22

- 【3小时】完成任务 - 导入历史专利申请数据
- 【5小时】分析并给出任务解决方案 - 根据历史数据明确专利的第一发明人信息的职工号，绑定具体的人员。（由于含有无法确认关联关系（即校内第一作者为空）的数据）；根据历史数据初始化专利库数据的所属单位（需要解决修改过部分所属单位的数据问题）

1-23

- 【3小时】开始编写定时任务用于解决SQL代码不易更新的部分字段
- 【5小时】完成定时任务的编写工作；整理SQL文件

===========================

2-4

- 【3小时】确保远程办公环境正常使用；返回办公室，提交代码到svn，此备份数据库文件
- 【5小时】汇报节前工作情况；再次检查历史数据完整性，确保无误；整理SQL文件中，预计今日晚上完成服务器更新工作

额外补充：
0. 两份不同方式备份的数据库应对数据丢失问题
1. 修改专利提案 所有发明人 字段
2. 删除专利提案列表页面 删除按钮的bindCheck="true"属性
3. 修改专利报账新增时，填写专利费用类型的代码
4. 修改专利报账查看，编辑，审核时，专利费用类型场景中的费用名称字段配置
5. 修复专利提案第一发明人不正确的BUG 


2-5 

- 【3小时】汇报工作；在服务器数据库上更新SQL -> 出现问题：1. 开始更新数据库时，因为使用了事务语句，速度慢了太多，后改为修改或删除数据时使用事务，新增数据不用 2. 更新报账费用时出现问题，后分成多份更新即可
- 【5小时】在服务器上完成SQL和程序的更新；测试上线功能


2-6

1. 统计未展示的数据字段 -> 整理中
2. 在报账列表上显示总金额 -> 新增元数据，修改场景
3. 审核状态 -> 分析历史网页的审核状态，调整数据 -> 修改提案场景，使用SQL更新审核状态值
4. 重复的添加按钮 -> patentPaymentAdd.jsp
5. 费用字段不显示，部分专利类型 -> 字典问题，执行SQL后无误
6. 软著建账更新完成

问题：
1. 历史数据没有代理状态字段，但是当前专利提案库中有，且列表快捷查询上显示，是否需要删除
2. 审核状态并未完全对应，更换策略，暂时匹配，后续等待与校方确认


2-7

专利报账问题
1. 列表的总金额和查看界面明细不一致 -> 费用明细表数据问题，修改表数据解决
2. 列表的打印预览应在线打开，不应是附件下载 -> 已修改代码
3. 报账新增、查看界面，报账经费缺少单位 -> 修改场景
4. 入账打印单没有显示费用名称 -> 修改代码
   入账打印单表文字应上下居中对齐 -> 修改word文件
5. 报账新增界面，专利报账信息区域的添加操作应该和专利报账信息在同一行显示； -> 修改页面patentPaymentAdd.jsp
6. 报账新增保存无反应：测试专利【一种基于深度学习的覆盖网络路由决策方法】，怀疑与该提案没有申请号有关 -> 修改页面patentPaymentAdd.jsp
7. 报账新增时费用名称和费用金额需设置必填 -> 修改场景
8. 专利报账新增后单据号没有生成，总金额没有生成 -> 单据号是审核完成后生成的，总金额在后台设置时出现问题，已修改代码

专利提案问题
1. 专利提案的提交时间没有体现 -> 提交时间为空字段，内部无数据，后将列表修改为与历史页面的对应字段 -> 添加授权时间字段元数据，修改场景

其他问题
1. 统计未展示的数据字段 -> 整理中
2. 有部分数据为1753-01-01，其值应为空 -> 更新对应字段的数据为null 
3. 修改专利报账列表场景后，修改制单时间生成策略 -> 修改代码
4. 历史数据中的发明人之间的分隔符为、而不是;（申请人之间也是）-> 修改代码，添加分隔适配
5. 对于时间格式不正确的数据，修改专利提案列表显示的时间字段类型的元数据类型为日期
6. 当前数据是否可进行打印预览操作是受审核状态影响的，暂时未放开权限

周总结：

本周是春节复工后的第一周，本周的工作主要是对节前工作的修改与提交。
由于在节前的单元测试较为粗心，开发产生的漏洞的确比较多，而且因为后发现了漏洞没有及时提交和修改，
积攒了不少的任务出来，希望在下周的工作中避免发生这种事情。

-------------------------------------

2-10

- 【3小时】早上提交周末的问题修改，汇报上周工作情况；由于更新代码后项目不能启动，之后的工作进度被延误了很多
- 【5小时】解决项目启动问题，但是没法整个模块导出，只能逐个导出场景，预计今晚上线



查看


3. 报账新增、查看界面，报账经费缺少单位 
7. 报账新增时费用名称和费用金额需设置必填


添加授权时间字段元数据，修改场景
修改专利提案列表显示的时间字段类型的元数据类型为日期

提案 列表

报账 新增、查看、列表、编辑
报账信息 新增、查看、编辑
元数据 专利提案 授权时间等时间


2-11

- 【5小时】中午汇报工作之后，下午开始产品这边的BUG修改


mongod --dbpath "D:\work\mongodb-win32-x86_64-2012plus-4.2.3\data" --logpath "D:\work\mongodb-win32-x86_64-2012plus-4.2.3\data\logs\mongod.log" --install --serviceName "MongoDB"


已修改完两个BUG，明日与测试人员确认后，提交代码:
4433 科研人员可查看不是自己的获奖申报信息 
4434 审核通过的获奖申报材料，个人无法登记获奖 


2-12

已修改BUG：
4427 申报材料列表导入并查看，点击“全部”报错
4417 科研秘书新增申报材料，成员信息界面提示申报数量已达单位限额
4417（科研秘书新增申报材料，成员信息界面提示申报数量已达单位限额）与测试沟通后，确认为设计如此

4457（考核机构和考核人员导出界面存在多余属性），已找到修改方法，在和测试确认业务是否需要进行

2-13

已修改BUG：
4500 秘书合同投标列表，点击下载导入模板报错
4447 纵向项目变更导出的Excel表中，部分变更类型为空
4446 横向项目变更导出的Excel表中，项目分类为空值
修改完，但是需要测试：
4419 校级申报材料批准立项后，完善时非负责人的项目成员的承担类型应有默认值

2-14

已修改BUG：
 4511 校级项目变更导出，导出内容显示不全
 4510 校级项目查看，切换项目经费页签时，无法点击关闭按钮
 4507 进账合同投标导入，导入后负责人显示待确认	   
 4493 秘书新增的合同供方单位，新增出账合同时无法选择
 4471 项目文档上传后，继续编辑后，页面显示标签页
 4467 项目变更导出，留校预算变更、成员变更、项目委托不显示

下列BUG修改单一场景不能满足需要，尝试增加场景，预计明天完成：
 4502 合同类别导入，导入项及模板出现多余的项
 4501 合同类别设置列表，快捷查询出现多余的查询项


 -- 4493 更新场景SQL

delete from SYS_CFG_SQL_TABLE where sceneid='4028802763dd7b090163dd8d2fb8255c';
delete from SYS_CFG_SCENE_SQLTABLE where sceneid='4028802763dd7b090163dd8d2fb8255c';
delete from SYS_CFG_SCENE where id='4028802763dd7b090163dd8d2fb8255c';
delete from SYS_CFG_SQL_TABLE where sceneid='4028802763dd7b090163dd8d2c84252d';
delete from SYS_CFG_SCENE_SQLTABLE where sceneid='4028802763dd7b090163dd8d2c84252d';
delete from SYS_CFG_SCENE where id ='4028802763dd7b090163dd8d2c84252d';


-- 表[SYS_CFG_SCENE]的数据如下:
insert into SYS_CFG_SCENE(ID,DATA_TYPE,REQACTION,BEANID,JSP,NAME,ROLE,PROMPTMSG,BINDSCENEID,EADPDATATYPE,CODE,SCENE_USE,CHANGED,LAST_EDIT_USER_ID,LAST_EDIT_DATE) values('4028802763dd7b090163dd8d2fb8255c','sqlTable','unitAptitudeAction!to_selectPage','unitAptitude','/system/commons/selectOne.jsp','配置-[科研处管理员]','4',NULL,NULL,'V8.3.0_105',NULL,'to_selectPage',NULL,'4028826f687369b80168736aaaab0003',to_date('2020-02-14 16:24:08','yyyy-mm-dd hh24:mi:ss'));


-- 表[SYS_CFG_SCENE]的数据如下:
insert into SYS_CFG_SCENE(ID,DATA_TYPE,REQACTION,BEANID,JSP,NAME,ROLE,PROMPTMSG,BINDSCENEID,EADPDATATYPE,CODE,SCENE_USE,CHANGED,LAST_EDIT_USER_ID,LAST_EDIT_DATE) values('4028802763dd7b090163dd8d2c84252d','sqlTable','unitAptitudeAction!to_selectPage','unitAptitude','/system/commons/selectOne.jsp','配置-[科研秘书]','3',NULL,'4028802763dd7b090163dd8d2fb8255c','V8.3.1_010',NULL,'to_selectPage','changing','4028826f687369b80168736aaaab0003',to_date('2020-02-14 16:24:23','yyyy-mm-dd hh24:mi:ss'));


-- 表[SYS_CFG_SCENE_SQLTABLE]的数据如下:
insert into SYS_CFG_SCENE_SQLTABLE(SCENEID,QUERYSQL,DATAPROCCLASSPATH,DATASOURCE) values('4028802763dd7b090163dd8d2fb8255c','select id,code as yfCode ,name,unit.buyer_Type as buyerType,contacts,telephone,province,city from BIZ_UNIT_APTITUDE unit where name like ''%^{q}%'' and unit.valid_type=''0''  and CURRENT_DATE() < unit.VALID_DATE + 1',NULL,NULL);


-- 表[SYS_CFG_SCENE_SQLTABLE]的数据如下:
insert into SYS_CFG_SCENE_SQLTABLE(SCENEID,QUERYSQL,DATAPROCCLASSPATH,DATASOURCE) values('4028802763dd7b090163dd8d2c84252d','select id,code as yfCode ,name,unit.buyer_Type as buyerType,contacts,telephone,province,city from BIZ_UNIT_APTITUDE unit where name like ''%^{q}%'' and unit.valid_type=''0''  and CURRENT_DATE() < unit.VALID_DATE + 1',NULL,NULL);


-- 表[SYS_CFG_SQL_TABLE]的数据如下:
insert into SYS_CFG_SQL_TABLE(ID,NAME,ORDERNO,DATA_TYPE,CATEGORYNAME,CATEGORYNAMELAB,AFFECTEDPROPERTY,LISTWIDTH,LISTFORMAT,ALIGN,COLOR,COLORENABLEDTEST,ORDERMODE,SCENEID,EADPDATATYPE,TITLE,TITLE_LOCAL) values('4028802763dd7b090163dd8d2fb8255d','name',0,NULL,NULL,NULL,NULL,30,'单行部分','left','000000',NULL,-1,'4028802763dd7b090163dd8d2fb8255c',NULL,'单位名称','Unit name');
insert into SYS_CFG_SQL_TABLE(ID,NAME,ORDERNO,DATA_TYPE,CATEGORYNAME,CATEGORYNAMELAB,AFFECTEDPROPERTY,LISTWIDTH,LISTFORMAT,ALIGN,COLOR,COLORENABLEDTEST,ORDERMODE,SCENEID,EADPDATATYPE,TITLE,TITLE_LOCAL) values('4028802763dd7b090163dd8d2fb8255e','province',1,NULL,'JF_LOCATION','甲方地区',NULL,15,'单行部分','left','000000',NULL,-1,'4028802763dd7b090163dd8d2fb8255c',NULL,'所在省份','Province where');
insert into SYS_CFG_SQL_TABLE(ID,NAME,ORDERNO,DATA_TYPE,CATEGORYNAME,CATEGORYNAMELAB,AFFECTEDPROPERTY,LISTWIDTH,LISTFORMAT,ALIGN,COLOR,COLORENABLEDTEST,ORDERMODE,SCENEID,EADPDATATYPE,TITLE,TITLE_LOCAL) values('4028802763dd7b090163dd8d2fb8255f','city',2,NULL,'JF_CITY','甲方所属地市','province',15,'单行部分','left','000000',NULL,-1,'4028802763dd7b090163dd8d2fb8255c',NULL,'所在城市','City where');


-- 4502 场景修改

delete from SYS_CFG_IMPORT where id in (select id from SYS_CFG_IMPORT where SCENEID = (select id from sys_cfg_scene where beanid = 'projectType' and  reqAction = 'importExcelAction!to_import' and jsp = '/operation/importData/importExcelInit.jsp' and role = '4') and ID in 
('402882296dd78e60016dd793a1cc0007','402882296dd78e60016dd793a1cc0008','402882296dd78e60016dd793a1cc0009','402882296dd78e60016dd793a1cc000a','402882296dd78e60016dd793a1cc000b'));

INSERT INTO SYS_CFG_IMPORT("ID", "NAME", "DATA_TYPE", "CATEGORYNAME", "ORDERNO", "CATEGORYNAMELAB", "SCENEID", "AFFECTEDPROPERTY", "EADPDATATYPE", "LISTWIDTH", "ALIGN", "REQCHECK", "COLLECTIONATTR", "BEANID", "TABNAME", "UNIQUESS") VALUES ('402882296dd78e60016dd793a1cc0007', 'subjectClassId', 'string', 'STA_CLASS', '5', '教育部统计归属', '402882296dd78e60016dd793a1cb0001', NULL, NULL, '6', NULL, NULL, NULL, 'projectType', '项目分类', NULL);
INSERT INTO SYS_CFG_IMPORT("ID", "NAME", "DATA_TYPE", "CATEGORYNAME", "ORDERNO", "CATEGORYNAMELAB", "SCENEID", "AFFECTEDPROPERTY", "EADPDATATYPE", "LISTWIDTH", "ALIGN", "REQCHECK", "COLLECTIONATTR", "BEANID", "TABNAME", "UNIQUESS") VALUES ('402882296dd78e60016dd793a1cc0008', 'projectSourceId', 'string', 'PROJECT_SOURCE', '6', '项目来源', '402882296dd78e60016dd793a1cb0001', NULL, NULL, '6', NULL, NULL, NULL, 'projectType', '项目分类', NULL);
INSERT INTO SYS_CFG_IMPORT("ID", "NAME", "DATA_TYPE", "CATEGORYNAME", "ORDERNO", "CATEGORYNAMELAB", "SCENEID", "AFFECTEDPROPERTY", "EADPDATATYPE", "LISTWIDTH", "ALIGN", "REQCHECK", "COLLECTIONATTR", "BEANID", "TABNAME", "UNIQUESS") VALUES ('402882296dd78e60016dd793a1cc0009', 'projectLevelId', 'string', 'PROJECT_LEVEL_ID', '7', '项目级别', '402882296dd78e60016dd793a1cb0001', NULL, NULL, '6', NULL, NULL, NULL, 'projectType', '项目分类', NULL);
INSERT INTO SYS_CFG_IMPORT("ID", "NAME", "DATA_TYPE", "CATEGORYNAME", "ORDERNO", "CATEGORYNAMELAB", "SCENEID", "AFFECTEDPROPERTY", "EADPDATATYPE", "LISTWIDTH", "ALIGN", "REQCHECK", "COLLECTIONATTR", "BEANID", "TABNAME", "UNIQUESS") VALUES ('402882296dd78e60016dd793a1cc000a', 'paySourceId', 'string', 'PROJECT_TYPE_PAY_SOURCE', '8', '支付来源', '402882296dd78e60016dd793a1cb0001', NULL, NULL, '6', NULL, NULL, NULL, 'projectType', '项目分类', NULL);
INSERT INTO SYS_CFG_IMPORT("ID", "NAME", "DATA_TYPE", "CATEGORYNAME", "ORDERNO", "CATEGORYNAMELAB", "SCENEID", "AFFECTEDPROPERTY", "EADPDATATYPE", "LISTWIDTH", "ALIGN", "REQCHECK", "COLLECTIONATTR", "BEANID", "TABNAME", "UNIQUESS") VALUES ('402882296dd78e60016dd793a1cc000b', 'isProcessAlarm', 'string', 'SF', '9', '是或否（存储值：1/0）', '402882296dd78e60016dd793a1cb0001', NULL, NULL, '6', NULL, NULL, NULL, 'projectType', '项目分类', NULL);


2-17

提交专利迁移流程

已解决BUG：
4445 校级项目变更导出的Excel表中，不展示项目分类和变更类型
4425 校级申报，历史申请列表导出的Excel表中项目分类的内容不正确
4392 获奖成果查看和审核界面中存在多余属性

还在进行的BUG修改，由于三个BUG的错误在同一问题上，预计今日完成：
4502 合同类别导入，导入项及模板出现多余的项
4501 合同类别设置列表，快捷查询出现多余的查询项
4484 进账合同变更导出项，显示不存在的元素

2-18
 
 已完成的BUG修改：
 4521 论文收录审核报错
 4393 管理员的著作权编辑界面中，非第一单位的学校署名展示属性“著作权人” 
 4414 申请书新增界面中保存后，展示的按钮不正确
 4415 科研人员新增界面存在多余属性
 4418 科研秘书和管理员的申报材料列表操作权限错误
 4440 纵向项目新增，国民经济行业的父类可选择
 4532 科研秘书首页待办，所有待办展示时，不显示经费外拨 新增后也未重现BUG
 
 正在进行的BUG修改：
 4502 合同类别导入，导入项及模板出现多余的项       
 4501 合同类别设置列表，快捷查询出现多余的查询项
 4484 进账合同变更导出项，显示不存在的元素
 

 4482 合同认定列表，导出文件名显示不合理 参考其他模块，截止时间为明日

2-19

 已完成的BUG修改：
 4482 合同认定列表，导出文件名显示不合理
 4515 银行到款导入，可导入字段显示错位
 4531 科研秘书首页待办，纵向项目立项待办计数错误


2-20
 已完成的BUG修改：
 4540 新增单位后，单位查看无法显示备注
 4536 个人中心，打印科研详情报错    
 4535 个人中心，科研详情导出报错
 4484 进账合同变更导出项，显示不存在的元素
 4502 合同类别导入，导入项及模板出现多余的项       
 4501 合同类别设置列表，快捷查询出现多余的查询项

 2-21

 已完成的BUG修改：
 4428 成果获奖的申报列表缺少快捷分组查询
 4449 科研秘书可删除学校通过的经费结转数据
 在纵向项目变更列表导出时，会同时导出了横向项目变更数据、校级项目变更数据的问题
 4529 项目查看，项目经费页签展示，只显示学校通过状态的经费外拨


项目分类 PROJECT_TYPE_ALL
变更类型 CHANGE_TYPE_ALL


 =====

 2-24

 今日完成工作：
 4450 经费结转编辑界面校验经费非负数        
 4550 校级项目申报、项目评审菜单报错        
 4542 论文新增界面中，发表/刊物论文集数据没有加载成功
