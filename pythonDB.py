import sqlite3 as sq

#เขื่อมต่อฐานข้อมูล
con = sq.connect('student.db')
with con:
     cur = con.cursor() #ตัว Pointer ตัวชี้ตำแหน่ง
     #cur.execute("create table comsci(id int,name text)")
    #  cur.execute("insert into comsci values(1,'Esso')")
    #  cur.execute("insert into comsci values(2,'Baew')")
    #  cur.execute("insert into comsci values(3,'Bam')")
    #  cur.execute("insert into comsci values(4,'Jib')")

     data = [(1,"Ha"),(2,"Yo"),(3,"Gi"),(4,"Fa")]
     cur.executemany('Insert into comsci values(?,?)',data) 
     print(data)

     

con.close() #ปิดฐานข้อมูล

