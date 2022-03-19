import email
import socket
import sqlite3,time,sys
import threading

host = "127.0.0.1"  # ip
port = 6000#int(input("Set port: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,  socket.SO_REUSEADDR,1) 
server.bind((host, port))   # ผูก object เข้ากับ host port
server.listen(5)  # กำหนดจำนวน client
print("รอการเชื่อมต่อจาก client :")
client, addr = server.accept()  # method นี้จะยืนยันว่า client ได้เชื่อมกับ server แล้ว และเก็บค่าใน client,addr
print("Connected From : "+str(addr))
count = 0
count +=1
print('Connect count: ',count)


def UsersList():
    with sqlite3.connect("hotel.db") as db:
        cur = db.cursor()
        u = cur.execute("select username from users")
        l = u.fetchall()
        print('จำนวนสมาชิก :', len(l), '\tคน')  # แสดงชข้อมูลในDB
        for i in range(len(l)):
            print(l[i])



def login(name,p):

   while True:
       username = name
       password = p
       with sqlite3.connect("hotel.db") as db:
           cur = db.cursor()
       find_user = ("select * from User where username =? and password =?")
       cur.execute(find_user,[(username),(password)])
       result = cur.fetchall()
       if result:
           for i in result:
               print("Username: "+i[0])
           return ("exit")
           break
       else:
           print("Username and password not regnised")
           again = input("Do you want to try again?(y/n): ")
           if again.lower()=='n':
               print("good bey")
               time.sleep(1)
               #return ("exit")
               break


def Register(name,p):
   found = 0
   while found == 0:
       username = name
       with sqlite3.connect("hotel.db", timeout=1) as db:
           cur = db.cursor()
       find_user = ("select * from User where username =?")
       cur.execute(find_user,[(username)])

       if cur.fetchall():
           print("Username Taken, Please try again")
       else:
           found = 1
 

   username = name
   password = p

   InsertData = '''insert into User(username,password) values(?,?)'''
   cur.execute(InsertData,[(username),(password)])
   db.commit()

def book():
    while True:

        print('--------------')
        print()
        break


def status():
    while True:
        print('--------------------')
        data = 'ทางโรงแรมได้ยืนยันการจองของท่านเรียบร้อยแล้ว'
        client.send(data.encode('utf-8'))
        
        break

while True:
    
    
    # รับข้อมูลจาก Client
    data = client.recv(1024).decode('utf-8')  # 1024byte หรือ 1024 ตัวอักษร และแปลง byte เป็น string
    if not data:
        break
    elif data =='register':
        name = client.recv(1024).decode('utf-8')
        p = client.recv(1024).decode('utf-8')
        
        task = threading.Thread(target=Register, args=(name,p))
        task.start()
        print("esso hahaha")
        print("client: " + data)#print ข้อความที่ clientส่งมา
        data1 = 'Your Account created!!!! ' #ข้อความที่เตรียมส่งให้client
        client.send(data1.encode('utf-8'))#ส่งไปหาclient
    elif data == 'login':
        name = client.recv(1024).decode('utf-8')
        p = client.recv(1024).decode('utf-8')       
        task = threading.Thread(target=login, args=(name,p))
        task.start()
        print("client: " + data)  # print ข้อความที่ clientส่งมา
        data1 = str(name)  # ข้อความที่เตรียมส่งให้client
        client.send(data1.encode('utf-8'))  # ส่งไปหาclient
    elif data == 'ทำการชำระเงินเรียบร้อย':
        status() 
        print("client: ", data)
    elif data == 'book':
       dat = client.recv(1024).decode('utf-8')
       book()
       print(data)   
      
       
       
client.close()
