import mysql.connector

mydb = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='',
  database='Tienda_Electronica'
)
mycursor = mydb.cursor()

def EjecutarSQL(sql,val):
  mycursor.executemany(sql, val)
  mydb.commit()

def Mostrar(Parametro):
  mycursor.execute(Parametro)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
