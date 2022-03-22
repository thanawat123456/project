import sqlite3
con = sqlite3.connect('hotel2.db' ,timeout=1)

def delete_task():
    con = sqlite3.connect('hotel2.db' ,timeout=1)
    with con:
        data =input("Delete Username: ")
        cur = con.cursor()
        sql_delete_query = """DELETE from User where username = ?"""
        cur.execute(sql_delete_query,[(data)])
        con.commit()
    con.close()  

delete_task()


# with con:
#     cur = con.cursor()
#     name = input("Enter data: ")
    

#     # Create table
#     # cur.execute("""create table User(
                    
#     #                 username varchar(20) not null,
#     #                 password varchar(20) not null)""")

#     # cur.execute('''CREATE TABLE Booking(
#     #             id	integer NOT NULL,
#     #             username VARCHAR, 
#     #              email VARCHAR, 
#     #              phon VARCHAR,
#     #              ckeckIn VARCHAR,
#     #              checkOut VARCHAR, 
#     #              rootType VARCHAR,
#     #              price Int,
#     #             PRIMARY KEY("id" AUTOINCREMENT))''')   
#     #cur.execute("insert into User values('esso','123')")
#     # data =('sdf','Esso','sdf','sdfs','ssdf','sdf','sdfsdr')
#     # cur.execute("insert into Booking(username,email,phon,ckeckIn,checkOut,rootType,price) values(?,?,?,?,?,?,?)", data,)         
# #     data = ''
# #     d1 = ''
# #     d2 = ''
# #     d3 = ''
# #     d4 = ''
# #     d5 = ''
# #     d6 = ''
# #     d7 = ''
# #     u = cur.execute("SELECT * FROM Booking ORDER BY id DESC LIMIT 0, 1")
# #     l = u.fetchall() 
# #     for i in range(len(l)):
# #                     d1 = l[i][0]
# #                     d2= l[i][1]
# #                     d3 = l[i][2]
# #                     d4 = l[i][3]
# #                     d5 = l[i][4]
# #                     d6 = l[i][5]
# #                     d7 = l[i][6]
# #                     d8 = l[i][7]

# #     msg = '''ID: {}
# # Username: {}
# # Email: {}
# # Phone NO: {}
# # Check IN: {}
# # Check Out: {}
# # Room Type: {}
# # Price: {}              
# # '''.format(d1,d2,d3,d4,d5,d6,d7,d8)
# # print(msg)


                    
   
#     # u = cur.execute("select * from User")
#     # l = u.fetchall()
#     # print('จำนวนสมาชิก :', len(l), '\tคน')  # แสดงชข้อมูลในDB
    
#     # for i in range(len(l)):
#     #     print('ID : ',i+1)
#     #     print('Username : ' ,l[i][0])
#     #     print('Password : ',l[i][1])
#     #     print('-----------------------------')

#     # print("	 *** HOTEL RECORD ***\n")
#     # u = cur.execute("select * from Booking")
#     # l = u.fetchall()        
#     # for i in range(len(l)):
#     #     # print("|",l[i][0],"  |",l[i][1]+"  \t |",l[i][2],"\t\t|",l[i][3],"\t\t|",l[i][4],"\t|",l[i][5],"\t|",l[i][6],"\t|",l[i][6])
#     #     # print(l[i][0],l[i][1],l[i][2],l[i][3],l[i][4],l[i][5],l[i][6],l[i][6])
#     #     print('ID : ',l[i][0])
#     #     print('Username : ',l[i][1])
#     #     print('email : ',l[i][2])
#     #     print('Phone No : ',l[i][3])
#     #     print('Check In : ',l[i][4])
#     #     print('Check Out : ',l[i][5])
#     #     print('Room Type : ',l[i][6])
#     #     print('Price : ',l[i][6])
#     #     print('=======================================')
        



# # def MSG():
# #     with con:
# #             cur = con.cursor()
# #             d1 = ''
# #             d2 = ''
# #             d3 = ''
# #             d4 = ''
# #             d5 = ''
# #             d6 = ''
# #             d7 = ''
# #             u = cur.execute("SELECT * FROM Booking ORDER BY id DESC LIMIT 0, 1")
# #             l = u.fetchall() 
# #             for i in range(len(l)):
# #                             d1 = l[i][0]
# #                             d2= l[i][1]
# #                             d3 = l[i][2]
# #                             d4 = l[i][3]
# #                             d5 = l[i][4]
# #                             d6 = l[i][5]
# #                             d7 = l[i][6]
# #                             d8 = l[i][7]

# #             msg = '''ID: {}
# #     Username: {}
# #     Email: {}
# #     Phone NO: {}
# #     Check IN: {}
# #     Check Out: {}
# #     Room Type: {}
# #     Price: {}              
# #                     '''.format(d1,d2,d3,d4,d5,d6,d7,d8)    
# #     return msg   


# # data = MSG()
# # print((data))   
      



# con.close()


