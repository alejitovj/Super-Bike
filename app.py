from flask import Flask, render_template
from flask_mysqldb import MySQL

#Crear la aplicacion Flask
app = Flask(__name__)

#Configuracion de MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'super_bike'

#Crear la conexion
mysql = MySQL(app)

#rutas de aplicacion

#pagina principal
@app.route("/")
def inicio():
    return render_template("index.html")

#Pagina de catalogo
@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")

#Pagina de contacto
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

#Pagina de quienes somos
@app.route("/quienes-somos")
def quienessomos():
    return render_template("quienessomos.html")

#Pagina de login
@app.route("/login")
def login():
    return render_template("login.html")

#Pagina de registro
@app.route("/registro")
def registro():
    return render_template("registro.html")

#ruta para comprobar la conexion a la base de datos
@app.route("/conexion")
def conexion():
    try:
        # Crear un cursor para ejecutar consultas
        cursor = mysql.connection.cursor()

        # Ejecutar consulta a la tabla
        cursor.execute("SELECT * FROM gestion_usuarios")

        # Obtener registros
        datos = cursor.fetchall()

        # Cerrar el cursor
        cursor.close()

        return {
            "mensaje": "Conexión exitosa a la base de datos",
            "cantidad_registros": len(datos),
            "usuarios": datos
        }
    except Exception as error:

        return {
            "mensaje": "Error al conectar con la base de datos",
            "detalle": str(error)
        }, 500

#Ejecutar la aplicacion
if __name__ == "__main__":
    app.run(debug=True)
