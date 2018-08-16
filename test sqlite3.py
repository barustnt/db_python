import sqlite3


def QueryReq (Query,conn): #define fct to read the query and excute it from the object conn wich is a funct cnxdb
    cursor = conn.cursor() #define a cusor for read
    cursor.execute(Query) #for execute the Query
    row = cursor.fetchall() #for the cursor search one value and their is fetchall
    conn.commit()  # to give us the possibility to write on our data base
    cursor.close() # must do it because we defined the the cursor in this function so we must end it
    print(row)
    return row

def cnxdb():
    cnx = None # for initialisation of the variable
    try: # we must use it because their is a possibility to lose the connection with our data base
        cnx = sqlite3.connect('cerist.db')
    except Error as e:
        print(e)
    return cnx
Query = ("insert into device_name(name,type) values ('CONDOR_AC','AC');") # our first Query
conn = cnxdb() #we use this object to create the conction with our data base and use it in all the Query
#InitialValue = QueryReq(Query,conn=conn)  #create an object to read the Query wich call function 'QueryReq' with two object Query and conn winch refrence to the conction with the data base
                                          # we add [0] to read the first value because python back with a tuble
Query2 =("SELECT* FROM device_name;")
ShowTable =QueryReq(Query2,conn)

conn.close()