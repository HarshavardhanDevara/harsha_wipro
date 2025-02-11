create database first_db;
use first_db;
show tables;   
create table dept(deptno int(10), dname char(30), loc varchar(33));
select*from dept;
create table emp(empno int(10), ename varchar(15), job varchar(15), mgr char(4), hiredate date, sal int(6), comm int(6), deptno int(2));
#sal is in int 
select*from emp;
INSERT INTO dept (deptno, dname, loc)VALUES ('10','ACCOUNTING','NEW YORK');
INSERT INTO dept (deptno, dname, loc)VALUES ('20','RESEARCH','DALLAS');
INSERT INTO dept (deptno, dname, loc)VALUES ('30','SALES','CHICAGO');
INSERT INTO dept (deptno, dname, loc)VALUES ('40','OPERATIONS','BOSTON');
INSERT INTO emp  VALUES ('7369','SMITH','CLERK','7902','1980-12-17','800.00',NULL,'20');
INSERT INTO emp  VALUES ('7499','ALLEN','SALESMAN','7698','1981-02-20','1600.00','300.00','30');
INSERT INTO emp  VALUES ('7521','WARD','SALESMAN','7698','1981-02-22','1250.00','500.00','30');
INSERT INTO emp  VALUES ('7566','JONES','MANAGER','7839','1981-04-02','2975.00',NULL,'20');
INSERT INTO emp  VALUES ('7654','MARTIN','SALESMAN','7698','1981-09-28','1250.00','1400.00','30');
INSERT INTO emp  VALUES ('7698','BLAKE','MANAGER','7839','1981-05-01','2850.00',NULL,'30');
INSERT INTO emp  VALUES ('7782','CLARK','MANAGER','7839','1981-06-09','2450.00',NULL,'10');
INSERT INTO emp  VALUES ('7788','SCOTT','ANALYST','7566','1982-12-09','3000.00',NULL,'20');
INSERT INTO emp  VALUES ('7839','KING','PRESIDENT',NULL,'1981-11-17','5000.00',NULL,'10');
INSERT INTO emp  VALUES ('7844','TURNER','SALESMAN','7698','1981-09-08','1500.00','0.00','30');
INSERT INTO emp  VALUES ('7876','ADAMS','CLERK','7788','1983-01-12','1100.00',NULL,'20');
INSERT INTO emp  VALUES ('7900','JAMES','CLERK','7698','1981-12-03','950.00',NULL,'30');
INSERT INTO emp  VALUES ('7902','FORD','ANALYST','7566','1981-12-03','3000.00',NULL,'20');
INSERT INTO emp  VALUES ('7934','MILLER','CLERK','7782','1982-01-23','1300.00',NULL,'10');

desc emp;
desc dept;
alter table dept modify dname varchar(15), modify loc varchar(15);
select empno, ename, job, hiredate from emp where deptno=10;
select ename, sal from emp where job = 'clerk'; 
select ename, job, sal from emp where hiredate = '1980-12-17';
desc emp;
show tables;
select*from emp;
select*from dept;
SELECT ABS(-2);
SELECT POW(2,3);
SELECT POW(DEPTNO,2) FROM emp;
SELECT SQRT(16);
SELECT MOD(12,5);
SELECT ROUND(12.738,2);
SELECT ROUND(12.734,2);
SELECT ceil(12.734);
SELECT FLOOR(12.734);
SELECT truncate(12.546,2);
SELECT RANDOM();
SELECT ln(100);
SELECT LOG10(1000);
SELECT LOG(2,8);
SELECT SIGN(-3);
SELECT SIGN(3);
SELECT GREATEST(30,40,50,100);
SELECT LEAST(30,40,50,100);
SELECT UPPER('hello');
SELECT LOWER('HELLO');
SELECT LENGTH('HELLO');
SELECT STRCMP('HELLO','SHASHI');
SELECT STRCMP('HELLO','DOO');
SELECT strcmp('HELLO','HELLO');
SELECT SUBSTRING('WORKING ON BUILT IN FUNCTIONS',4,7);
SELECT locate('ON','WORKING ON BUILT IN FUNCTIONS');
SELECT CONCAT('I AM',' ','WORKING ON BUILT IN FUNCTIONS');
SELECT CONCAT_WS('-',ENAME,DEPTNO,SAL) FROM EMP;
SELECT ASCII('G');
SELECT REPLACE('GOOD MORNING','GOOD','HAPPY');
SELECT REVERSE('GOOD  MORNING');
SELECT REPEAT('GOOD MORNING',3);
SELECT RTRIM('HELLO     ');
SELECT TRIM('     HELLO');
SELECT TRIM('     HELLO     ');
SELECT LPAD('HELLO',10,'*');
SELECT rpad('HELLO',10,'*');
SELECT LPAD(RPAD('HELLO',10,''),15,'');
SELECT curdate();
SELECT current_timestamp();
SELECT YEAR(curdate());
select year(hiredate) from emp;
select month(hiredate) from emp;
select day(hiredate) from emp;
select dayname(hiredate) from emp;
select dayofweek(hiredate) from emp;
select dayofweek(hiredate) from emp;
select week(hiredate) from emp;
select date_format(hiredate,'%d-%m-%y') from emp;
select date_format(hiredate,'%d-%m-%y') from emp;
select datediff(curdate(),'2001-06-18') 'difference';
select count(*) from emp;
select sum(sal) from emp;
select min(sal) from emp;
select max(sal) from emp;
select sum(sal),deptno from emp group by deptno;
select sum(sal),deptno from emp where deptno=30 group by deptno;
select sum(sal),deptno from emp group by deptno having sum(sal)>9000;
select sum(sal),deptno from emp group by deptno having sum(sal)>9000 order by deptno desc;
select ename,sal,comm from emp where comm>sal;
select * from emp;
select deptno,sum(sal) as total_sal from emp group by deptno;
select ename from emp order by sal;
select ename from emp order by sal asc limit 3; #top 3 salary members
select ename from emp order by sal desc limit 3;
select ename,if(sal>2500,'eligible for promotion','not eligible') from emp;
select comm,sal,coalesce(comm,sal) from emp;
select ename,case deptno when 10 then "marketing" when 20 then "training" else "new joinee" end department from emp;
select ename,ifnull(comm,700) as status from emp;
select ename,nullif(deptno,10) as status from emp;
create table order_tbl(orderid int,item varchar(30),quantity int,o_year int);
insert into order_tbl values(101,'laptop',5,2003),(102,'laptop',1,2001);
insert into order_tbl values(103,'mobile',2,2008),(105,'laptop',5,2003),(102,'laptop',4,2008);
insert into order_tbl values(104,'tv',3,2007),(106,'calcular',4,2006),(107,'mobile',4,2008);
insert into order_tbl values(108,'calcular',7,2007),(109,'tv',4,2001),(110,'mobile',4,2008);
select o_year,sum(quantity) over(partition by o_year) as sale from order_tbl;
select empno,deptno,sal,row_number() over(partition by deptno order by sal desc) as rownum from emp;
select empno,deptno,sal,row_number() over(partition by deptno order by sal desc) as rownum from emp;
select empno,deptno,sal,rank() over(partition by deptno order by sal desc) as ranking from emp;
select empno,deptno,sal,rank() over(partition by deptno order by sal desc) as ranking,dense_rank() over(partition by deptno order by sal desc) as denseranking from emp;


select ltrim(        "hello");
select rtrim("hello"       );
select trim(        "hello"         );
select substring("working on built in function", 4,4);
select substring("working on built in function", 4,7);
select rpad(lpad('hello', 10, '*'), 15, '*');

select avg(sal) from emp;
select sum(sal),deptno from emp group by deptno;
select sum(sal),deptno from emp where depno=10 group by deptno;
select sum(sal),deptno from emp group by deptno;
select deptno, ename, sum(sal) from emp group by deptno, ename;

select ename from emp order by sal desc;

select ename, comm, ifnull(comm,700) as status from emp;

select comm, sal, coalesce(comm, sal) from emp;

select empno,deptno,sal, row_number() over(partition by deptno order by sal desc) as rownum from emp;
#all cases works using joins instead of were 
select empno,ename,dname,e.deptno from emp e, dept d where e.deptno= d.deptno;
select empno,ename,dname,emp.deptno from emp,dept where emp.deptno= dept.deptno;
#on used while diff columns in diff tables,using used on same columns and table name
select empno,ename,dname,e.deptno from emp e join dept d on(e.deptno= d.deptno);
select empno,ename,dname,e.deptno from emp e join dept d using(deptno);
select empno,ename,dname,deptno from emp join dept using(deptno);
select empno,ename,dname,deptno from emp natural join dept;
select empno,ename,dname,deptno from emp inner join dept using (deptno);
select*from dept;
select count(*) from dept;  #to count rows
select count(*) from emp;
select empno,ename,dname,emp.deptno from emp cross join dept;
select empno,ename,dname,emp.deptno from emp,dept where emp.deptno>dept.deptno;
select empno,ename,dname,emp.deptno from emp,dept where emp.deptno<>dept.deptno;
select empno,ename,dname,deptno from emp left join dept using (deptno);
select empno,ename,dname,deptno from emp right join dept using (deptno);
select empno,ename,dname,deptno from dept left join emp using (deptno);
select empno,ename,dname,deptno from emp full join dept using (deptno);
select empno,ename,dname,deptno from emp full join dept; #full join not works
select e2.ename,e1.ename from emp e1,emp e2 where e1.empno = e2.mgr;

select empno,ename,job,mgr,hiredate,sal, IFNULL(comm, 0) as comm, deptno from emp;
select ename, empno, job, sal from emp where (job='MANAGER' OR job='SALESMAN') AND sal > 2600;
select ename, empno from emp where job='MANAGER' AND sal > 2600;
select distinct length(ename) as name_length from emp;
select round(months_between(sysdate, hiredate)) as months_worked from emp
where job='President'; #no answer

select ename from emp where sal> (select sal from emp where ename='allen');
select ename from emp where sal> (select sal from emp where ename='allen') and job in (select job from emp where job ='clerk');
select ename from emp where sal> (select sal from emp where ename='allen') and job in (select job from emp where job ='analyst');
select*from emp where deptno=10;
select*from emp where deptno=10 or deptno=20;
select job from emp where job ='ANALYST';
select*from emp where deptno in (10,20);

select ename from emp where sal< any(select sal from emp where job = 'salesman');
select ename from emp where sal< all(select sal from emp where job = 'salesman');
#corelated subquery
#constrains
create table student(id int not null, name varchar(30));
desc student;
insert into student values(100,'harsha');
insert into student (id) values(200);
insert into student (name) values('rakesh'); #not null 
select*from student;
drop table student;
create table student(id int unique, name varchar(30), grade varchar(2));
desc student;
insert into student values(100,'vidhya','B');
insert into student values(100,'Leena','c'); #unique duplicates not allow
select*from student;
drop table student;
create table student(id int, name varchar(30), grade varchar(2) check(grade in('A','B','C','D')));
create table students(id int, name varchar(30), grade varchar(2) check(grade in('A','B','C','D'))default'A');
drop table students;
select e.ename, d.deptno, d.dname from emp e join dept d on e.deptno = d.deptno;
select d.dname, d.deptno, d.loc from dept d left join emp e on d.deptno = e.deptno
where e.ename is null;
select e.ename, e.sal, d.dname, d.deptno from emp e
join dept d on e.deptno = d.deptno
where e.sal >( select min(e2.sal) from emp e2 where e2.deptno = e.deptno); 
select e.ename, e.sal, e.deptno from emp e
where e.sal >( select max(e2.sal) from emp e2 where e2.deptno = 30); 
select e1.ename, e1.deptno, e1.sal from emp e1 
left join emp e2 on e1.job = e2.empno where e1.job is null; #wrong
create table employee(eno int,ename char(20),sal int,doj date);
insert into employee values(100,'shashi',34000,'2020-01-30'),(200,'manoj',50000,'2025-08-29'),(300,'vishnu',20000,'2021-09-16'),(400,'kiran',60000,'2024-07-15'),(900,'Rdj',50000,'2022-09-01');
use my_first_db;
create table newemp as select * from employee where 1=2;
insert into newemp values(400,'ashley',45000,'2023-07-17'),(500,'srinu',70000,'2021-07-08'),(200,'manoj',50000,'2025-08-29'),(300,'vishnu',20000,'2021-09-16');
select * from employee union select * from newemp;
select * from employee union all select * from newemp;
-- select * from employee except select * from newemp;
-- select * from employee except all select * from newemp;
select * from emp;
select * from dept;
select empno,ename,dname,e.deptno from emp e,dept d where e.deptno=d.deptno;  #equi join
select empno,ename,dname,emp.deptno from emp,dept where emp.deptno=dept.deptno;
select empno,ename,dname,e.deptno from emp e join dept d on e.deptno=d.deptno;
select empno,ename,dname,e.deptno from emp e join dept d on(e.deptno=d.deptno);
select empno,ename,dname,e.deptno from emp e join dept d using(deptno);
select empno,ename,dname,deptno from emp join dept  using(deptno);
select empno,ename,dname,deptno from emp natural join dept;
select empno,ename,dname,deptno from emp inner join dept  using(deptno);
select empno,ename,dname,emp.deptno from emp,dept where emp.deptno>dept.deptno; #non-equi join
select empno,ename,dname,emp.deptno from emp,dept where emp.deptno<>dept.deptno;
select empno,ename,dname,emp.deptno from emp left join dept using(deptno);
select empno,ename,dname,emp.deptno from emp right join dept using(deptno);
#full outer join not supported in mysql.
select empno,ename,dname,emp.deptno from emp,dept where emp.deptno<>dept.deptno;
select empno,ename,dname,emp.deptno from emp left join dept using(deptno);
select empno,ename,dname,emp.deptno from emp right join dept using(deptno);
#full outer join not supported in mysql.
select e2.ename,e1.ename from emp e1,emp e2 where e1.empno=e2.mgr;
select ename,empno from emp where job='manager' and sal>2600 order by ename;
select ename,empno,job,mgr,hiredate,deptno,ifnull(comm,0) as comm from emp  ;
select ename,job from emp where (job='manager'or job='salesman') and sal>1500;
select ename,job from emp where job in ('manager','salesman') and sal>1500;
select distinct length(ename) from emp;
select * from emp;
select round(datediff(curdate(),hiredate)/30) from emp where job='president'; #approximate
select round(timestampdiff(month,hiredate,curdate())) as monthsworked from emp where job='president';
select ename from emp where sal>(select sal from emp where ename='allen') and job in (select job from emp where job='analyst');
select ename from emp where sal>(select sal from emp where ename='allen') and job ='analyst';
select ename from emp where sal>(select sal from emp where ename='allen');
select ename from emp where sal>(select sal from emp where ename='allen') and job in (select job from emp where job='analyst');
select ename from emp where sal>(select sal from emp where ename='allen') and job ='analyst';
select ename from emp where sal<any(select sal from emp where job='salesman');
select ename from emp where sal<all(select sal from emp where job='salesman');
select ename from emp where sal in (select sal from emp where job='salesman');
SELECT ename, sal, deptno FROM emp e WHERE sal > (SELECT avg(sal) FROM emp WHERE deptno = e.deptno);
create table student(id int not null,name varchar(10));
insert into student values(100,'shashi');
insert into student(id) values(200);
insert into student(name) values('abcd');# it will not insert id cannot be null
select * from student;
create table stud(id int unique,name varchar(10));
insert into stud values(100,'manoj');
insert into stud values(200,'kiran');
insert into stud values(100,'rock'); # it will not insert because id is unique
create table stu(id int,name varchar(10),grade varchar(2) check(grade in ('A','B','C','D')));
insert into stu values(100,'RDJ','A');
insert into stu values(101,'Venom','E'); # it will not insert because grade is not in required values
create table st(id int,name varchar(10),grade varchar(2) default 'A');
insert into st(id,name) values(112,'ajay');
select * from st;
insert into st(id) values(202);
create table parent(id int, name varchar(10), constraint p1 primary key(id));
insert into parent values(10,'vishal');
insert into parent values(20,'robert');
insert into parent values(30,'downey');
insert into parent values(10,'abcd'); #it will not insert
insert into parent values(null,'vishnu');#it will not insert
create table child(cid int,cname varchar(10), foreign key(cid)  references parent(id));
insert into child values(10,'xyz');
insert into child values(20,'visak');
insert into child values(40,'vishal'); #does not insert the values
drop table parent;
create table chil(cid int,cname varchar(10), foreign key(cid)  references parent(id) on delete cascade);
insert into chil values(10,'abc');
insert into chil values(20,'xyza');
insert into chil values(30,'abcyz');
delete from parent where id=30;
select * from parent;
select * from chil;
create table p1(id int primary key auto_increment,name varchar(10));
insert into p1(name) values('junior');
select * from p1;
select ename,deptno,dname from emp join dept using(deptno);
select dname from dept where deptno not in (select deptno from emp);
SELECT ename, sal FROM emp e WHERE sal > (SELECT min(sal) FROM emp WHERE deptno = e.deptno);
SELECT ename, sal, deptno FROM emp e where sal>(SELECT max(sal) FROM emp WHERE deptno =30);
select * from emp;
select ename from emp where mgr is null;



