import socket
import time
import traceback
import sqlite3
from threading import Thread
import pickle
import threading as thread
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print('\n\n','*'*10 + '  SERVER  ' + '*'*10,'\n\n')
TCP_IP = "127.0.0.1"
TCP_PORT = 6789
BUFFER_SIZE = 1024


subject = 'ทดสอบการส่งข้อความผ่านอีเมลรายวิชา network '
     
def sendthai(sendto,subj="ทดสอบส่งเมลลล์",detail="สวัสดี!\nคุณสบายดีไหม?\n"):

	myemail = 'test.django50@gmail.com'
	mypassword = "0652709145"
	receiver = sendto

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subj
	msg['From'] = 'โปรแกรมเมอร์เหล้าขาว'
	msg['To'] = receiver
	text = detail

	part1 = MIMEText(text, 'plain')
	msg.attach(part1)

	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()

	s.login(myemail, mypassword)
	s.sendmail(myemail, receiver.split(','), msg.as_string())
	s.quit()



def MSG():
    con = sqlite3.connect('hotel2.db' ,timeout=1)
    with con:
            cur = con.cursor()
            d1 = ''
            d2 = ''
            d3 = ''
            d4 = ''
            d5 = ''
            d6 = ''
            d7 = ''
            u = cur.execute("SELECT * FROM Booking ORDER BY id DESC LIMIT 0, 1")
            l = u.fetchall() 
            for i in range(len(l)):
                            d1 = l[i][0]
                            d2= l[i][1]
                            d3 = l[i][2]
                            d4 = l[i][3]
                            d5 = l[i][4]
                            d6 = l[i][5]
                            d7 = l[i][6]
                            d8 = l[i][7]

            msg = '''ID: {}
Username: {}
Email: {}
Phone NO: {}
Check IN: {}
Check Out: {}
Room Type: {}
Price: {}              
                    '''.format(d1,d2,d3,d4,d5,d6,d7,d8)    
    con.close()                
    return msg   


def Login(connection ,ip):
    member_profile = []

    while True:
        data = connection.recv(BUFFER_SIZE).decode("utf-8")
        if not data: break
        if len(member_profile) > 2 or len(member_profile) == 2:
            break

        member_profile.append(data)
    

    #check id
    conn_db = sqlite3.connect('hotel2.db')
    c=conn_db.cursor()
    c.execute("SELECT * FROM User ")
    flag = 1
    for no in c.fetchall():
        if no == tuple(member_profile):
            time.sleep(0.2)
            print("Confirm the information is correct!!! ")
            flag = 0
            break
    if flag == 0:
        connection.send("yes".encode("utf-8"))
    else:
        connection.send("no".encode("utf-8"))
    conn_db.commit()
    conn_db.close()
    print("Login to: ",member_profile[0])
    

def Register(connection ,ip):
    member_profile = []
   
    while True:
        data = connection.recv(BUFFER_SIZE).decode("utf-8")
        if not data: break
        elif len(member_profile) > 2 or len(member_profile) == 2:
            break
        print("rev: ",data)
        member_profile.append(data)



   #check id
    conn_db = sqlite3.connect('hotel2.db')
    c=conn_db.cursor()
    sqlite_insert_with_param = """INSERT INTO User
                          (username, password) 
                          VALUES (?, ?);"""
    data_tuple = (member_profile[0],member_profile[1])
    c.execute(sqlite_insert_with_param, data_tuple)

    time.sleep(0.2)

    conn_db.commit()
    conn_db.close()
    connection.send("yes".encode("utf-8"))
    print("Registered successfully")


def process_input(input_str):


    return str(input_str).upper()

def receive_input(connection):
    client_input = connection.recv(BUFFER_SIZE)
    
    decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    result = process_input(decoded_input)

    return result


def status(connection):
    time.sleep(1)
    while True:
        print()
        print("")
        confirm1=input("Server ยืนยันการจองของผู้ใช้บริการ (y/n) : ")
        time.sleep(1)
        print('การจองสำเร็จ')
        if confirm1 == 'y':
            connection.send("ทางโรงแรมได้ยืนยันการจองของท่านเรียบร้อยแล้ว".encode("utf-8"))
            break
        

def client_thread(connection, ip, port):
    is_active = True

    while is_active:
        client_input = receive_input(connection)

        if "--LOGIN--" in client_input:
            print() 
            print("Client Login...")
            Login(connection, ip)
        elif "--REG--" in client_input:
            print() 
            print("Client Register...")
            Register(connection, ip)
        elif "ทำการชำระเงินเรียบร้อย" in client_input: 
            print() 
            print('ทำการชำระเงินเรียบร้อย')  
            status(connection)
        elif "--QUIT--" in client_input:
            print("Client Logout")
            connection.close()
            print("Connection " + ip + ":" + port + " ได้ทำการออกจากระบบ")
            is_active = False
        elif "ยืนยันการส่งเมล" in client_input:
            print()
            print('กำลังกำเนินการ...')
            con = sqlite3.connect('hotel2.db')
            mail = ''
            with con:
                cur = con.cursor()
                for row in cur.execute('SELECT * FROM Booking ORDER BY id DESC LIMIT 0, 1'):
                    mail = row[2]                 
            da = MSG()
            ta = "ทางโรงแรม SBAI ขอแสดงความขอบคุณที่มาใช้บริการ\nรายละเอียดการจองของท่านมีดังนี้\n"+da
            print('Email to: ',mail)
            sendthai(mail,subject,ta)
            print('ส่งอีเมลเมลไปยัง Client สำเร็จ')
            ma = 'Server ทำการส่งรายละเอียดไปทางอีเมลของคุณแล้ว'
            connection.send(ma.encode("utf-8"))

        else:
            pass    




def Main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP,TCP_PORT)) #เชื่อมต่อ
    s.listen(5)
    print("LISTENING Server is listening... ")
    
    #flag_server = 0
    while True:
        conn,addr = s.accept()
        ip,port = str(addr[0]), str(addr[1])
        print()
        print('Client connect to'+str(addr))
        try:
            Thread(target=client_thread,args=(conn,ip,port)).start()
            print(f"[ACTIVE CONNECTIONS] {thread.activeCount() - 1}")
        except:
            print("Thread did not start.")
            traceback.print_exc()
    
       
    
Main()