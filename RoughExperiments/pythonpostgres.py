import psycopg2
import sys
#making a connection
connect = psycopg2.connect(dbname = "postgres", user = "postgres", host = "localhost", port = "5432", password = "18012000")
#returns connection object to run sql queries
#print(connect)
cursor = connect.cursor()   #used to run queries against Database

#creating table and adding data
def create():
    cursor.execute("create table pytab(Name text, ID int, Language text);")
    print("Table Added")

"""def add():
    cursor.execute("insert into pytab(Name, ID, Language) values('Sam',1,'python');")
    cursor.execute("insert into pytab(Name, ID, Language) values('Jack',2,'java');")
    print("Data Added")"""

def add():
    print("Please enter the Data you want to insert : ")
    name = input("Name: ")
    id = int(input("ID: "))
    lang = input("language: ")
    query = "insert into pytab(Name, ID, Language) values(%s,%s,%s)"
    # using string formatting operator %
    cursor.execute(query,(name,id,lang))
    print("Data Added")

def show():
    cursor.execute("select * from pytab;")
    print(cursor.fetchall())    #to get the all data, fetchone for single data
    print("Data Shown!")

def dele():
    cursor.execute("drop table pytab;")
    print("Table Deleted")

if __name__ == "__main__":
    print("Welcome to PostgreSQL Python Connection\n")
    while True:
        print("Please select a desired operation you wanna do:\n't' for creating new table\n'd' for deleting the table\n'a' for adding values\
            \n's' for showing the data\n'e' to exit!")
        opt = input("Operation : ").lower()
        if opt == "t":
            try:
                create()
            except:
                print("FATAL! Table already exists!")
            connect.commit()
        elif opt == "d":
            try:
                dele()
            except:
                print("FATAL! Table doesn't exist!")
            connect.commit()
        elif opt == "a":
            try:
                add()
            except:
                print("Please check the source for error!")
            connect.commit()
        elif opt == "s":
            try:
                show()
            except:
                print("Nothing to show!")
            connect.commit()
        elif opt == "e":
            print("Exited!") 
            break
        else:
            print("Invalid Operation!")
    print("Connection Closed!")
    connect.close()
