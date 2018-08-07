import mysql.connector

cnx = mysql.connector.connect(user='root', password='naruto2009',
                              host='127.0.0.1',
                              database='cerist')
cnx.close()