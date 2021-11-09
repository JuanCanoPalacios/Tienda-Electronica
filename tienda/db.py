import mysql.connector

try: 
    mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='Tienda_Electronica'
    )
    print("[BD]: Conectado con éxito.")
    mycursor = mydb.cursor()
except mysql.connector.errors.DatabaseError:
    print("[BD]: Conexión fallida.")
    mydb = None
    mycursor = None

def ejecutarSQL(sql):
    mycursor.execute(sql)
    mydb.commit()

def ejecutarSQL_VAL(sql,val):
    mycursor.executemany(sql, val)
    mydb.commit()

def mostrar(parametro):
    mycursor.execute(parametro)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def dato(parametro):
    mycursor.execute(parametro)
    myresult = mycursor.fetchall()
    return myresult
