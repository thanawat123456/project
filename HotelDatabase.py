import sqlite3
con = sqlite3.connect('hotel.db')


with con:
    cur = con.cursor()

    # Create table
    cur.execute("""create table User(
                    username varchar(20) primary key,
                    password varchar(20) not null)""")

    cur.execute('''CREATE TABLE Booking
                (username VARCHAR, email VARCHAR, phon VARCHAR,ckeckIn VARCHAR,checkOut VARCHAR, rootType VARCHAR,price Int)''')   

con.close()