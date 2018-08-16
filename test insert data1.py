from mysql.connector import MySQLConnection, Error
import mysql.connector

def QueryReq (Query,conn): #define fct to read the query and excute it from the object conn wich is a funct cnxdb
    cursor = conn.cursor() #define a cusor for read
    cursor.execute(Query) #for execute the Query
    row = cursor.fetchone() #for the cursor search one value and their is fetchall
    conn.commit()  # to give us the possibility to write on our data base
    cursor.close() # must do it because we defined the the cursor in this function so we must end it
    return row

def cnxdb():
    cnx = None # for initialisation of the variable
    try: # we must use it because their is a possibility to lose the connection with our data base
        cnx = mysql.connector.connect(user='root', password='naruto2009',
                                      host='127.0.0.1',
                                      database='cerist')
    except Error as e:
        print(e)
    return cnx
Query = ("SELECT tv_sound FROM tv WHERE   tv.id=2;") # our first Query
conn = cnxdb() #we use this object to create the conction with our data base and use it in all the Query
InitialValue = QueryReq(Query,conn=conn)[0]  #create an object to read the Query wich call function 'QueryReq' with two object Query and conn winch refrence to the conction with the data base
                                             # we add [0] to read the first value because python back with a tuble
InitialValue = int(InitialValue)             # to return it to int
print("This is the value before the updating " , +InitialValue)
values=int(input("enter the volum you want <0-100>")) #Give us the value wich you want

n=values-InitialValue
if  n > 0 :
   print("the number of vol up is " ,n)
else :
    n=-n
    print(("the number of vol down is ",n))

Query2 = ("UPDATE tv SET tv_sound="+str(values)+" WHERE tv.id=2;")
UdatedValue=QueryReq(Query2,conn)
Query = ("SELECT tv_sound FROM tv WHERE   tv.id=2;")
tchek=QueryReq(Query,conn) [0]
tchek= int (tchek)
print("the curnet value wich saved in the data base is ",+ tchek)

conn.close()

