import socket
import time
import os
import sys
import pickle
import sqlite3
import datetime
import random


print('\n\n','*'*10 + '  CLIENT  ' + '*'*10,'\n\n')
TCP_IP = "127.0.0.1"
TCP_PORT = 6789
BUFFER_SIZE = 1024



name = []
passw = []
phno = []
add = []
email = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []
mail = []
ema = ''
book = ()
booklist = []
username = "" #รอรับค่าเลขมือถือจากผู้ใช้
password = "" #รอรับรหัสผ่านจากผู้ใช้

i = 0

con = sqlite3.connect("hotel2.db")
def addDB(list):
    with con:
        curr = con.cursor()
        data = list

        curr.executemany("insert into Booking(username,email,phon,ckeckIn,checkOut,rootType,price) values(?,?,?,?,?,?,?)", data,)    
   



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))

flag_login = 0

def Clear():
    os.system('clear')


def Index():
    while True:
        print('-------------------------------------')
        manu = ('''
        1. Admin
        2. User
        3. Exit
        ''')
        print(manu)
        select = input("Choose your choice: ")
        if select == '1':
            Addminlogin()
        elif select == '2':
            Main()
        elif select == '3':
            print("Good Bye~ ~")
            sys.exit()
        else:
            print("Please try again")





def Main():
    print("-------------------------------")
    print('1. Login' + '\n'
      '2. Register \n\n')
    while True:
        Input = int(input('โปรดเลือกเมนู (หมายเลข): '))
        Clear()
        if Input == 1:
            Login()
            break
        elif Input == 2:
            Register()
            time.sleep(2)
            Login()
            break
        else:
            print('โปรดกรอกชื่อให้ถูกต้อง!')
    global flag_login
    if flag_login == 1:
        Home()

    s.close()
    print('*'*10 + '  EXIT  ' + '*'*10)

def Login():
    while True:
        print("\n***** Login *****")     
        s.send(bytes("--LOGIN--","utf-8"))
        global username
        global password
        username = input("Enter your username: ")
        s.send(bytes(username,"utf-8"))
        password = input("Enter your password: ")
        Clear()
        s.send(bytes(password,"utf-8"))
        time.sleep(1)
        s.send("break".encode("utf-8"))

        while 1:
            data = s.recv(BUFFER_SIZE).decode("utf-8")
            if not data: break
            elif data == "yes":
                #login สำเร็จ
                print("*** Login successfully ***\n")
                print("Hello : ",username)
                global flag_login
                flag_login = 1
                break
            elif data == "no":
                #login ไม่สำเร็จ
                print("คุณเข้าสู่ระบบไม่สำเร็จ")
                print("กรุณาลองใหม่อีกครั้ง\n")
                break
        if flag_login == 1:
            break

def Register():
    print("\n :ระบบสมัครสมาชิก:")   
    global username
    global password
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        password_con = input("Enter your password again: ")
        if password == password_con:
            s.send(bytes("--REG--","utf-8"))
            time.sleep(0.5)
            s.send(bytes(username,"utf-8"))
            time.sleep(0.1)
            s.send(bytes(password,"utf-8"))
            time.sleep(0.1)
            s.send("break".encode("utf-8"))
            print("ได้ทำการส่งคำขอไปที่เซิร์ฟเวอร์")
            break
        else:
            print("โปรดตรวจสอบรหัสผ่านและรหัสผ่านยืนยันให้ตรงกัน")
    #ทำการส่งข้อมูลไปสมัคร
    while 1:
        data = s.recv(BUFFER_SIZE).decode("utf-8")
        if not data: break
        elif data == "yes":
            #login สำเร็จ
            print("*** Registered successfully ***\n")
            time.sleep(1)
            Clear()
            break




def Home():
    
    print("\t\t\t\t WELCOME TO HOTEL SBAI\n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Rooms Detail\n")
    print("\t\t\t 3 Payment\n")
    print("\t\t\t 4 Sendmail\n")
    print("\t\t\t 0 Exit\n")
    
    ch=int(input("->"))
    
    if ch == 1:
        print(" ")
        Booking()
    
    elif ch == 2:
        print(" ")
        Rooms_Info()
    
    elif ch == 3:
        print(" ")
        Payment()
    
    elif ch == 4:
        print(" ")
        Sendmail()
    
    else:
        name.clear()
        passw.clear()
        phno.clear()
        add.clear()
        email.clear()
        checkin.clear()
        checkout.clear()
        room.clear()
        price.clear()
        rc.clear()
        p.clear()
        roomno.clear()
        custid.clear()
        day.clear()
        mail.clear()

        book = ('')
        booklist.clear()
        Exit()
        



def date(c):
    
    if c[2] >= 2022 and c[2] <= 2023:
        
        if c[1] != 0 and c[1] <= 12:
            
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                
                if c[2]%4 == 0 and c[0] <= 29:
                    pass
                
                elif c[0]<29:
                    pass
                
                else:
                    print("Invalid date\n")
                    name.pop(i)
                    phno.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Booking()
            
            
            
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
                pass
            
        
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
                pass
            
        
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
                pass
    
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:
                pass
            
            else:
                print("Invalid date\n")
                name.pop(i)
                phno.pop(i)
                add.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                Booking()
                
        else:
            print("Invalid date\n")
            name.pop(i)
            phno.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
            
    else:
        print("Invalid date\n")
        name.pop(i)
        phno.pop(i)
        add.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        Booking()



def Booking():

        global i
        print(" BOOKING ROOMS")
        print(" ")
        
        while 1:
            n = str(input("Name: "))
            p1 = str(input("Phone No.: "))
            a = str(input("Address: "))
            e = str(input("Email : "))
            
        
            if n!="" and p1!="" and a!="" and e!="":
                name.append(n)
                add.append(a)
                mail.append(e)
                break
                
            else:
                print("\tName, Phone no. & Address cannot be empty..!!")
            
        cii=str(input("Check-In: "))
        checkin.append(cii)
        cii=cii.split('/')
        ci=cii
        ci[0]=int(ci[0])
        ci[1]=int(ci[1])
        ci[2]=int(ci[2])
        date(ci)
        
        coo=str(input("Check-Out: "))
        checkout.append(coo)
        coo=coo.split('/')
        co=coo
        co[0]=int(co[0])
        co[1]=int(co[1])
        co[2]=int(co[2])
        
        
        if co[1]<ci[1] and co[2]<ci[2]:
            
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
            name.pop(i)
            add.pop(i)
            mail.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
            
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
            name.pop(i)
            add.pop(i)
            mail.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        else:
            pass
        
        date(co)
        d1 = datetime.datetime(ci[2],ci[1],ci[0])
        d2 = datetime.datetime(co[2],co[1],co[0])
        d = (d2-d1).days
        day.append(d)
        
        print("----SELECT ROOM TYPE----")
        print(" 1. Type A")
        print(" 2. Type B")
        print(" 3. Type C")
        print(" 4. Type D")
        print(("\t\tPress 0 for Room Prices"))
        
        ch=int(input("->"))
        
       
        if ch==0:
            print(" 1. Type A. 3500")
            print(" 2. Type B. 4000")
            print(" 3. Type C. 4500")
            print(" 4. Type D. 5000")
            ch=int(input("->"))
        if ch==1:
            room.append('Type A')
            print("Room Type A")
            price.append(3500)
            print("Price- 3500")
        elif ch==2:
            room.append('Type A')
            print("Room Type B")
            price.append(4000)
            print("Price- 4000")
        elif ch==3:
            room.append('Type C')
            print("Room Type C")
            price.append(4500)
            print("Price- 4500")
        elif ch==4:
            room.append('Type D')
            print("Room Type D")
            price.append(5000)
            print("Price- 5000")
        else:
            print(" Wrong choice..!!")



        rn = random.randrange(40)+300
        cid = random.randrange(40)+10
        
        
   
        while rn in roomno or cid in custid:
            rn = random.randrange(60)+300
            cid = random.randrange(60)+10
            
        rc.append(0)
        p.append(0)
            
        if p1 not in phno:
            phno.append(p1)
        elif p1 in phno:
            for n in range(0,i):
                if p1== phno[n]:
                    if p[n]==1:
                        phno.append(p1)
        elif p1 in phno:
            for n in range(0,i):
                if p1== phno[n]:
                    if p[n]==0:
                        print("\tหมายเลขโทรศัพท์ มีอยู่แล้วและยังไม่ได้ชำระเงิน..!!")
                        name.pop(i)
                        add.pop(i)
                        checkin.pop(i)
                        checkout.pop(i)
                        Booking()
        print("")
        print("\t\t***ROOM BOOKED SUCCESSFULLY***\n")
        print("Room No. - ",rn)
        print("Customer Id - ",cid)
        roomno.append(rn)
        custid.append(cid)
        

        i=i+1
        n=int(input("0-BACK\n ->"))
        if n==0:
            Home()
        else:
            exit()




def Rooms_Info():
    print("		 ------ HOTEL ROOMS INFO ------")
    print("")
    print("Type A")
    print("---------------------------------------------------------------")
    print("สิ่งอำนวยความสะดวกในห้องประกอบด้วย: เตียงคู่ 1 เตียง, โทรทัศน์, โทรศัพท์,")
    print("ตู้บานคู่, โต๊ะกาแฟ 1 ตัวพร้อมโซฟา 2 ตัว, ระเบียงและ")
    print("ห้องน้ำในตัวพร้อมน้ำอุ่น/น้ำเย็น.\n")

    print("Type B")
    print("---------------------------------------------------------------")
    print("สิ่งอำนวยความสะดวกในห้องประกอบด้วย: เตียงคู่ 1 เตียง, โทรทัศน์, โทรศัพท์,")
    print("ตู้บานคู่, โต๊ะกาแฟ 1 ตัวพร้อมโซฟา 2 ตัว, ระเบียง")

    print("Type C")
    print("---------------------------------------------------------------")
    print("สิ่งอำนวยความสะดวกในห้องประกอบด้วย: 1 เตียงใหญ่ + 1 เตียงเดี่ยว โทรทัศน์,")
    print("โทรศัพท์, ตู้สามประตู, โต๊ะกาแฟ 1 ตัวพร้อมโซฟา 2 ตัว, ")
    print("โต๊ะข้าง 1 ตัว ระเบียงพร้อมโต๊ะสำเนียง พร้อมเก้าอี้ 2 ตัว ")
    print("ห้องน้ำในตัวพร้อมน้ำอุ่น/น้ำเย็น\n")

    print("Type D")
    print("---------------------------------------------------------------")
    print("สิ่งอำนวยความสะดวกในห้องประกอบด้วย: 1 เตียงใหญ่ + 1 เตียงเดี่ยว โทรทัศน์,")
    print("โทรศัพท์ ตู้สามประตู โต๊ะกาแฟ 1 ตัว พร้อมโซฟา 2 ตัว, ")
    print("โต๊ะข้าง 1 ตัว ระเบียงพร้อมโต๊ะเอนกประสงค์พร้อมเก้าอี้ 2 ตัว")
    print("และห้องน้ำในตัวพร้อมน้ำร้อน/เย็น + หน้าต่าง.\n\n")
    print()
    n=int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit()



    
                
            
def Payment():
    
    ph=str(input("Phone Number: "))
    global i
    f=0
    
    for n in range(0,i):
        try:
            print(phno[n])
            book = (name[n],mail[n],phno[n],checkin[n],checkout[n],room[n],(price[n]*day[n]))
            booklist.append(book)
            addDB(booklist)
            

            if ph==phno[n] :
                
                if p[n]==0:
                    f=1
                    print(" Payment")
                    print(" --------------------------------")
                    print(" MODE OF PAYMENT")
                    
                    print(" 1- บัตรเครดิต/เดบิต")
                    print(" 2- เงินสด")
                    x=int(input("-> "))
                    print("\n Amount: ",(price[n]*day[n]))
                    print("\n		 Pay For Hotel SBAI")
                    print(" (y/n)")
                    ch=str(input("->"))
                    
                    if ch=='y' or ch=='Y':
                        print("\n\n --------------------------------")
                        print("       Hotel SBAI")
                        print(" --------------------------------")
                        print("       Bill")
                        print(" --------------------------------")
                        print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
                        print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
                        print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
                        print(" --------------------------------")
                        print("\n Total Amount: ",(price[n]*day[n]),"\t")
                        print(" --------------------------------")
                        print("		 Thank You")
                        print("		 Visit Again :)")
                        print(" --------------------------------\n")

                        s.send(bytes("ทำการชำระเงินเรียบร้อย","utf-8"))  
                        data = s.recv(BUFFER_SIZE).decode("utf-8")
                        time.sleep(1)
                        print('Data from server: '+data)

                        p.pop(n)
                        p.insert(n,1)
                        roomno.pop(n)
                        custid.pop(n)
                        roomno.insert(n,0)
                        custid.insert(n,0)
                        
                else:
                    
                    for j in range(n+1,i):
                        if ph==phno[j] :
                            if p[j]==0:
                                pass
                            
                            else:
                                f=1
                                print("\n\tชำระเงินแล้ว :)\n\n")
        except:
              Home()
    if f==0:
        print("Invalid Customer Id")
        
    n = int(input("0-BACK\n ->"))
    if n == 0:
        
        Home()
    else:
        exit()


def Sendmail():
    sen = input('คุณต้องการให้ทางโรงแรมส่งข้อมูลการจองไปทางอีเมล (y/n): ' )
    if sen == 'y':
        s.send("ยืนยันการส่งเมล".encode("utf-8")) 
        data = s.recv(BUFFER_SIZE).decode("utf-8")
        time.sleep(1)
        print(data)
        print()
        n = int(input("0-BACK\n ->"))
        if n == 0:
            Home()
    else:
        pass

        



    
def Exit():
    s.send("--QUIT--".encode("utf-8"))
    print("ขอบคุณที่ใช้บริการ  ^_^")
    sys.exit()

def Addminlogin():
    print("กรอกข้อมูลของ Admin")
    username = input("please enter your username: ")
    password = input("please enter your password: ")
    if username == 'admin' and password == '7777':
        admin()       
    else:
        print("Please try again")
                


def ADMIN_User():
    conn_db = sqlite3.connect('hotel2.db')
    c=conn_db.cursor()
    u = c.execute("select * from User")
    l = u.fetchall()
    print('จำนวนสมาชิก :', len(l), '\tคน')  # แสดงชข้อมูลในDB
    for i in range(len(l)):
        print('ID : ',i+1)
        print('Username : ' ,l[i][0])
        print('Password : ',l[i][1])
    conn_db.close()    
    n = int(input("0-BACK\n ->"))
    if n == 0:
        admin()

    


def Delete_User():
    con = sqlite3.connect('hotel2.db' ,timeout=1)
    with con:
        data =input("Delete Username: ")
        cur = con.cursor()
        sql_delete_query = """DELETE from User where username = ?"""
        cur.execute(sql_delete_query,[(data)])
        con.commit()
    con.close() 
    n = int(input("0-BACK\n ->"))
    if n == 0:
        admin()

def admin():
    print()
    print("******** ADMIN *********\n")
    print("\t1. ดูรายชื่อผู้รับบริการทั้งหมด")
    print("\t2. ดูประวัติการจอง")
    print("\t3. สั่งปิดบริการ User")
    print("\t4. EXIT")
    Input = int(input('Phoose your choice: '))
    Clear()
    if Input == 1:
        ADMIN_User()
    elif Input == 2:
        ADMIN_Book()
    elif Input == 3:
         Delete_User()   
    else :
        Exit()
def ADMIN_Book():
    conn = sqlite3.connect('hotel2.db')
    cur=conn.cursor()
    print("	 *** HOTEL RECORD ***\n")
    qury = cur.execute("select * from Booking")
    data = qury.fetchall()        
    for i in range(len(data)):
        print('ID : ',data[i][0])
        print('Username : ',data[i][1])
        print('email : ',data[i][2])
        print('Phone No : ',data[i][3])
        print('Check In : ',data[i][4])
        print('Check Out : ',data[i][5])
        print('Room Type : ',data[i][6])
        print('Price : ',data[i][6])
        print('=======================================')
    conn.close() 
    n = int(input("0-BACK\n ->"))
    if n == 0:
        admin()        

Index() 

