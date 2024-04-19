import mysql.connector
db=mysql.connector.connect(user="root",password='Mathan@123',host='localhost',database='task')
var=db.cursor()
#var.execute("create database task")
#print("create database")
#var.execute("use task")
print("used")
#var.execute("create table tasklist(id int,name varchar(20),age int)")
print("table created")
var.execute("insert into tasklist values(1,'kumar',22)")
var.execute("insert into tasklist values(2,'raj',24)")
var.execute("insert into tasklist values(3,'gj',25)")
var.execute("insert into tasklist values(4,'rahul',26)")
var.execute("insert into tasklist values(5,'lokesh',27)")
db.commit()
var.execute("update tasklist set name='rajesh' where id=2")
db.commit()
print("inserted")
var.execute("delete from tasklist where id=2")
db.commit()
#var.execute("alter table tasklist add column list int")
#print("added")
var.execute("alter table tasklist drop column age")
print("droped")
var.execute("alter table tasklist rename column age to ages")
print("changed")
var.execute("drop table tasklist")
var.execute("drop database task")







