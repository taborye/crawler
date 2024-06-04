
#创建一个数据库
create databases new_spider charset utf-8;

#选择指定的数据库
use new_spider;

#查看所有的数据库
show databases;
select databases();

#删除指定的数据库
drop database new_spider;

#创建一张表table(exceal表格) 电影名字 评分 简介 导演 上映时间
create table movie_tb(
    moviename varchar,
    score float,
    desc string,
    docter string,
    playDate date
);


数据库数据类型：
char varchar int double float date time datetime set  enum

#创建一个学生表
create table student {
    id int,
    name char(30),
    age int,
    score float(5,2),五位数组成,小数位最多两位
    endSchool date,
    gender enum("male","female"),
    lesson set("math","english","python","java")
};

create table t1 {
    id int primary key, #主键约束:主键唯一,还可以联合主键约束
    name char,
    salary

};

create table t2 {
    id int primary key,
    name char(10),
    sex char default("male")#默认约束
};

唯一约束unique

desc student; #desc查看表结构

#修改表的名字
alter table student rename stu;
#x修改表中字段类型
alter table stu modify score int;


#修改字段名
alter table stu change gender sex char (10);

#增加表中的字段
alter table stu add startschool date
#删除表中字段
alter table stu drop age

#删除表table

drop  table stu



create table new_dep {
    id int primary key,
    dep_desc varchar(30),
    dep_name varchar(30)
};

insert into new_dep(id,dep_desc,dep_name) values  (1,"sale_product",'sale')

insert into new_dep values(2,"dep something",'dep');
insert into new_dep values(3,"dep something",'dep'),(4,"dep something",'dep'),(5,"dep something",'dep')



修改数据
update new_dep set dep_name = 'sales' where id = 3;#将id=3 的数据中dep_name 改为sales

delete from new_dep where id = 2; #将id=2的数据删除
delete from new_dep where id = 2 or dept_name = 'dep';

SET SQL_SAFE_UPDATES = 0#解除安全模式
SET SQL_SAFE_UPDATES = 0#添加安全模式




create table emp (
    id int primary key auto_increment,
    name char (20),
    gender enum('male','female'),
    age int,
    hire_date date,
    job_title varchar(30),
    salary float(10,2),
    office_num int,
    dep_id int
)

#查询所有字段信息
select * from emp

#查询指定字段
select name salary from emp

#查询字段的运算
select name ,salary * 12 as year_sal form emp;  #as year_sal 取别名

#条件查询where
#查询销售员工的姓名和薪资
select name,salary from emp where job_title = "sales";

#查询薪资大于1w的老师的名字和具体薪资
select name,salary from emp where salary > 10000 and job_title = 'teacher';

#查询薪资为3k,或5k,或9k的员工的名字和具体薪资
select name,salary from emp where  salary=3000 or salary = 5000 or salary = 9000;
select name,salary from emp where  salary in(3000,5000,9000);


#区间判断
#查询薪资范围在1000-5000之间的员工的名字和岗位名称
select name ,job_title from emp where salary between 1000 and 5000;

#模糊查询
#查询名字是以a开头的员工的名字和薪资
select name,salary from emp where name like 'a%'
#查询名字是zhang开头的，并且后面只能有3个字符的员工
select name,salary form emp where name like 'zhang___'

#排序
#根据薪资排序(默认是从小到达排序,加上desc就是从大到小排序)
select * from emp order by  salary desc
#根据工作名称排序
select *from emp where order by job_title


#limit 限定
select *from emp limit 3 #查询前三条数据
select *from emp limit 1,3 #从第一行开始查询3条数据

#查询薪资最高的员工的薪资
select *from emp order by salary dec limit 1;


#查询的基本操作  分表查询 链表查询

#分组查询  多表查询 练习  python 链接数据库  pandas 数据处理操作
