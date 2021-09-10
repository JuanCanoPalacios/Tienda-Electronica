import mysql.connector

try: 
  mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='Tienda_Electronica'
  )
  mycursor = mydb.cursor()
except mysql.connector.errors.DatabaseError:
  print("No se pudo conectar a la base de datos...")
  mydb = None
  mycursor = None

def EjecutarSQL(sql):
  mycursor.execute(sql)
  mydb.commit()

def EjecutarSQL_VAL(sql,val):
  mycursor.executemany(sql, val)
  mydb.commit()

def Mostrar(Parametro):
  mycursor.execute(Parametro)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
