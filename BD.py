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

def EjecutarSQL_VAL(sql,val):
  if (mycursor is None and mydb is None):
    print ("No fue posible conectarse a la BD")
  else:  
    mycursor.executemany(sql, val)
    mydb.commit()

def Mostrar(Parametro):
  if (mycursor is None and mydb is None):
    print("No fue posible conectarse a la BD")
  else:  
    mycursor.execute(Parametro)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)

