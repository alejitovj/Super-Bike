from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

# Crear la aplicacion Flask
app = Flask(__name__)

# Configuracion de MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'super_bike'

# Crear la conexion
mysql = MySQL(app)

# --- RUTAS DE APLICACIÓN ---

# Página principal
@app.route("/")
def inicio():
    return render_template("index.html")

# Página de catalogo
@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")

# Página de contacto
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

# Página de quienes somos
@app.route("/quienes-somos")
def quienessomos():
    return render_template("quienessomos.html")

# Página de login
@app.route("/login")
def login():
    return render_template("login.html")

# Ruta para comprobar la conexion a la base de datos
@app.route("/conexion")
def conexion():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM gestion_usuarios")
        datos = cursor.fetchall()
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

# Página de registro
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        nombre_usuario = request.form["nombre_usuario"]
        contraseña = request.form["password"]

        contraseña_encriptada = generate_password_hash(contraseña)

        cursor = mysql.connection.cursor()
        sql = """
        INSERT INTO gestion_usuarios 
        (nombre, correo, telefono, nombre_usuario, contraseña)
        VALUES (%s, %s, %s, %s, %s)
        """
        datos = (nombre, correo, telefono, nombre_usuario, contraseña_encriptada)
        
        cursor.execute(sql, datos)
        mysql.connection.commit()
        cursor.close()

        # Devuelve "ok" para que el fetch de JavaScript active la alerta de SweetAlert2
        return "ok"
    
    # Si es una petición GET, carga la vista del formulario
    return render_template("registro.html")

# Ejecutar la aplicacion (Siempre va al final del todo)
if __name__ == "__main__":
    app.run(debug=True)