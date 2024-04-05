import mysql.connector;

db=mysql.connector.connect(host='localhost',password='Mathan@123',user='root',database='person')

var=db.cursor()
#data base create
var.execute("create database person")
print("database created")
#table create
var.execute("create table data(id int primary key,name varchar(20),mark int)")
db.commit()
#----insert table---
print("table create")
var.execute("insert into data values(1,'kumar',90)") 
var.execute("insert into data values(2,'arun',100)") 
var.execute("insert into data values(3,'suresh',98)") 
var.execute("insert into data values(4,'rahul',92)") 
var.execute("insert into data values(5,'tamil',88)") 
db.commit()
print("intered")

#update-----table
var.execute("update data set name=raju where mark=92")
db.commit()
#modify table-------
var.execute("alter table data modify column id int")
#delete ----------table
var.execute("delete from data where mark=88")
db.commit()


