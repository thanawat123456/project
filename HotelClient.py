import random
import socket
import datetime
import sqlite3 as DB,sys

host = "127.0.0.1"
port = 6000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,  socket.SO_REUSEADDR,1) 
server.connect((host,port))
con = DB.connect("hotel.db")

with con :
    cur = con.cursor()



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

book = ()
booklist = []


i = 0



def UsersList():
    u = cur.execute("select * from users")
    l = u.fetchall()
    print('จำนวนสมาชิก :', len(l), '\tคน')  # แสดงชข้อมูลในDB
    for i in range(len(l)):
        print(i + 1)
        print('username :', l[i][0])
        print('password :', l[i][1])

        print('-----------------------------')    

def addDB(list):

    with con:
        curr = con.cursor()
        data = list

        curr.executemany("insert into Booking values(?,?,?,?,?,?,?)", data)
    
  
def login():
   username = input("please enter your username: ")
   server.send(username.encode('utf-8'))
   password = input("please enter your password: ")
   server.send(password.encode('utf-8'))

def Register():
    username = input("please enter your username: ")  
    server.send(username.encode('utf-8'))
    password = input("please enter your password: ")
    
    

            
    
    server.send(password.encode('utf-8'))
    
    

 
    


def manuUserLog():
   while True:
       print('-------------------------------------')
       print('Welcome to Users System')
       manu = ('''
       1. สมัครสมาชิก
       2. เข้าระบบ
       3. กลับ
       ''')
       print(manu)
       select = input("Choose your choice: ")
       if select=='1':
           data = 'register'
           server.send(data.encode('utf-8'))  # ส่งข้อความไปหาserver
           Register()
           print('sdfwefwef')
           data_server = server.recv(1024).decode('utf-8')
           print("Data from server:" + data_server)
       elif select=='2':
           data = 'login'
           server.send(data.encode('utf-8'))  # ส่งข้อความไปหาserver
           login()
           data_server = server.recv(1024).decode('utf-8')
           print("Data from server:"+'Hello\t' + data_server)
           Home()
       elif select == '3':
           print("Thank you")
           
       else:
           print("Please try again")         
          

    





def Home():
    
    print("\t\t\t\t\t\t WELCOME TO HOTEL SBAI\n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Rooms Detail\n")
    print("\t\t\t 3 Food Menu \n")
    print("\t\t\t 4 Payment\n")
    print("\t\t\t 5 Record\n")
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
        restaurant()
    
    elif ch == 4:
        print(" ")
        Payment()
    
    elif ch == 5:
        print(" ")
        Record()
    
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

        book = ('')
        booklist.clear()
        manuUserLog()



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
            
        
            if n!="" and p1!="" and a!="":
                name.append(n)
                add.append(a)
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
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
            
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
            name.pop(i)
            add.pop(i)
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
        print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
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


def restaurant():
    ph=int(input("Customer Id: "))
    global i
    f=0
    r=0
    for n in range(0,i):
        if custid[n]==ph and p[n]==0:
            f=1
            print("-------------------------------------------------------------------------")
            print("						 Hotel SBAI")
            print("-------------------------------------------------------------------------")
            print("						 Menu Card")
            print("-------------------------------------------------------------------------")
            print("\n BEVARAGES                            26 สเต็กหมู................. 340.00")
            print("----------------------------------    27 ฝีเลมิยอง................ 350.00")
            print(" 1 ชาธรรมดา................ 20.00     28 ริบอาย.................. 350.00")
            print(" 2 น้ำอัดลม.................. 25.00")
            print(" 3 กาแฟ.................... 25.00     ROTI")
            print(" 4 เครื่องดื่มเย็นๆ............. 25.00     ----------------------------------")
            print(" 5 เนยขนมปัง................ 30.00     29 โรตีกล้วยหอม.............. 15.00")
            print(" 6 ขนมปังแยม................ 30.00     30 โรตีโฮมเมด............... 15.00")
            print(" 7 ผัก แซนวิช................ 50.00     31 โรตีผักสด................. 20.00")
            print(" 8 ผัก แซนวิชขนมปังปิ้ง......... 50.00     32 โรตีไอศกรีม............... 20.00")
            print(" 9 แซนวิชขนมปังปิ้งชีส.......... 70.00")
            print(" 10 แซนวิชย่าง............... 70.00     RICE")
            print("                                      ----------------------------------")
            print(" SOUPS                                33 ข้าวหุง.................. 90.00")
            print("----------------------------------    34 ข้าวเหนียว............... 90.00")
            print(" 11 ซุปมะเขือเทศ............. 110.00    35 ข้าวหุงพิเศษ.............. 110.00")
            print(" 12 ซุปพริกหวาน ............. 110.00    36 ข้าวเหนียวพิเศษ........... 110.00")
            print(" 13 ซุปผักสไตล์อิตาเลี่ยน........ 110.00")
            print(" 14 ซุปใสลูกชิ้นปลา............ 110.00    CAKE")
            print(" 15 ซุปหน่อไม้ฝรั่ง............. 110.00    ----------------------------------")
            print("                                      37 เค้กเนยสด.............. 100.00")
            print(" MAIN COURSE                          38 เครปเค้ก............... 110.00")
            print("----------------------------------    39 ชิฟฟอนเค้ก.............. 130.00")
            print(" 16 สเต๊กเนื้อซอสบัลซามิก....... 310.00    40 สปันจ์เค้ก............... 130.00")
            print(" 17 ซี่โครงเนื้อย่าง............ 310.00    41 เค้กไข่ขาว.............. 130.00")
            print(" 18 เนื้ออบซอสไวน์แดง......... 320.00    42 ไอศกรีมเค้ก............. 140.00")
            print(" 19 เนื้ออบเวลลิงตัน........... 320.00")
            print(" 20 ออสโซบุคโคไวน์แดง........ 340.00    ICE CREAM")
            print(" 21 ซี่โครงแกะอบกับราทาทูอี..... 340.00    ----------------------------------")
            print(" 22 น่องแกะตุ๋น............... 340.00    43 ไอศกรีมวนิลา............ 60.00")
            print(" 23 ซี่โครงหมูอบบาร์บีคิว........ 340.00    44 ไอศกรีมสตรอเบอร์รี่....... 60.00")
            print(" 24 ขาหมูทอดเยอรมมัน......... 340.00    45 ไอศกรีมสัปปะรด.......... 60.00")
            print(" 25 ฝีเลมิยองสเต็ก............ 340.00    46 ไอศกรีมบัตเตอร์สก๊อต...... 60.00")
            print("Press 0 -to end ")
            ch=1
            while(ch!=0):
                
                ch=int(input(" -> "))
                
      
                if ch==1 or ch==31 or ch==32:
                    rs=20
                    r=r+rs
                elif ch<=4 and ch>=2:
                    rs=25
                    r=r+rs
                elif ch<=6 and ch>=5:
                    rs=30
                    r=r+rs
                elif ch<=8 and ch>=7:
                    rs=50
                    r=r+rs
                elif ch<=10 and ch>=9:
                    rs=70
                    r=r+rs
                elif (ch<=15 and ch>=11) or ch==35 or ch==36 or ch==38:
                    rs=310
                    r=r+rs
                elif ch<=19 and ch>=18:
                    rs=320
                    r=r+rs
                elif (ch<=26 and ch>=20) or ch==42:
                    rs=340
                    r=r+rs
                elif ch<=28 and ch>=27:
                    rs=350
                    r=r+rs
                elif ch<=30 and ch>=29:
                    rs=15
                    r=r+rs
                elif ch==33 or ch==34:
                    rs=90
                    r=r+rs
                elif ch==37:
                    rs=100
                    r=r+rs
                elif ch<=41 and ch>=39:
                    rs=130
                    r=r+rs
                elif ch<=46 and ch>=43:
                    rs=60
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("Wrong Choice..!!")
            print("Total Bill: ",r)
            
            
            r=r+rc.pop(n)
            rc.append(r)
        else:
            pass
    if f == 0:
        print("Invalid Customer Id")
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
            book = (name[n],phno[n],add[n],checkin[n],checkout[n],room[n],price[n])
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
                    print("\n Amount: ",(price[n]*day[n])+rc[n])
                    print("\n		 Pay For Hotel SBAI")
                    print(" (y/n)")
                    ch=str(input("->"))
                    
                    if ch=='y' or ch=='Y':
                        print("\n\n --------------------------------")
                        print("		 Hotel SBAI")
                        print(" --------------------------------")
                        print("			 Bill")
                        print(" --------------------------------")
                        print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
                        print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
                        print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
                        print(" Restaurant Charges: \t",rc[n])
                        print(" --------------------------------")
                        print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t")
                        print(" --------------------------------")
                        print("		 Thank You")
                        print("		 Visit Again :)")
                        print(" --------------------------------\n")

                        
                        mass = 'ทำการชำระเงินเรียบร้อย'
                        server.send(mass.encode('utf-8'))
                        

                        data_server = server.recv(1024).decode('utf-8')
                        print('Data from server: '+data_server)
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
                pass                     
                 
    if f==0:
        print("Invalid Customer Id")
        
    n = int(input("0-BACK\n ->"))
    if n == 0:
        
        Home()
    else:
        exit()


def Record():
    

    if phno!=[]:
        print("	 *** HOTEL RECORD ***\n")
        print("| Name	 | Phone No.    | Address	 | Check-In  | Check-Out	 | Room Type	 | Price	 |")
        print("----------------------------------------------------------------------------------------------------------------------")
        
        for n in range(0,i):
            try:
                print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",checkin[n],"\t|",checkout[n],"\t|",room[n],"\t|",price[n])
                print('esssssooooo',booklist)
                data = 'book'
                server.send(data.encode('utf-8'))

            except:
                
                pass    
        
        print("----------------------------------------------------------------------------------------------------------------------")
    
    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
        
    else:
        exit()



def seletRoll():
    while True:
        print('-------------------------------------')
        print('Welcome to Food Service System')
        manu = ('''
        1. Admin
        2. User
        3. Exit
        ''')
        print(manu)
        select = input("Choose your choice: ")
        if select == '1':
            data = 'Admin'
            server.send(data.encode('utf-8'))  # ส่งข้อความไปหาserver
            
        elif select == '2':
            data = 'User'
            server.send(data.encode('utf-8'))  # ส่งข้อความไปหาserver
            manuUserLog()
        elif select == '3':
            print("Good Bye~ ~")
            sys.exit()
        else:
            print("Please try again")

seletRoll()