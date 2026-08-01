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

#Pagina de registro
@app.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "POST":

        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        nombre_usuario = request.form["usuario"]
        contraseña = request.form["password"]

# Encriptar contraseña
    contraseña_encriptada = generate_password_hash(contraseña)

    cursor = mysql.connection.cursor()

    sql = """
    INSERT INTO gestion_usuarios 
    (nombre, correo, telefono, nombre_usuario, contraseña)
    VALUES (%s, %s, %s, %s, %s)
    """

    datos = (
        nombre,
        correo,
        telefono,
        nombre_usuario,
        contraseña_encriptada
    )

    cursor.execute(sql, datos)
    mysql.connection.commit()
    cursor.close()

    return """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
</head>
<body>
    <script>
        Swal.fire({
            title: '¡Usuario registrado!',
            text: 'Tu cuenta fue creada correctamente.',
            icon: 'success',
            confirmButtonText: 'Continuar',
            confirmButtonColor: '#b71c1c',
            background: '#fff8f8',
            color: '#7f0000',
            iconColor: '#c62828'
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = '/login';
            }
        });
    </script>
</body>
</html>
"""