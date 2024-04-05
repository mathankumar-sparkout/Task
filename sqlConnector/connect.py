import mysql.connector;
co=mysql.connector.connect(host='localhost',password='Mathan@123',user='root',database="employees")


cur=co.cursor()

#create database
cur.execute("create database employees")

#create table
cur.execute("CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))")
print("created table")

#insert table
cur.execute("INSERT INTO customer (name, address) VALUES (%s, %s)",("John", "Highway 21"))
co.commit()
cur.execute("insert into customer(name,address) values (%s,%s)",("mathan","pollachi"))
co.commit()
print("inserted")

#update table
cur.execute("update customer set name='mathankumar' where address='pollachi'")
co.commit()
#delete table
cur.execute("delete from customer where name='john'")
co.commit()

#add column
cur.execute("alter table customer add column id int" )


