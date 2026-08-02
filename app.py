from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

# Crear la aplicacion Flask
app = Flask(__name__)
app.secret_key = '030726'

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
        nombre_usuario = request.form["nombre_usuario"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        contraseña = request.form["password"]  # Aquí capturamos la contraseña

        # Encriptamos la variable correcta
        contraseña_encriptada = generate_password_hash(contraseña)

        try:
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO gestion_usuarios (nombre_usuario, correo, contraseña, telefono) VALUES (%s, %s, %s, %s)"
            datos = (nombre_usuario, correo, contraseña_encriptada, telefono)
            
            cursor.execute(sql, datos)
            mysql.connection.commit()
            cursor.close()

            return redirect(url_for("ingreso_exitoso"))
        except Exception as error:
            return f"Error al registrar: {error}"
            
    return render_template("registro.html")

# Página de inicio de sesión
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        contraseña = request.form["password"]

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM gestion_usuarios WHERE correo = %s", (correo,))
        usuario = cursor.fetchone()
        cursor.close()

        if usuario:
            contraseña_hash = usuario[3]

            if check_password_hash(contraseña_hash, contraseña):
                session['logueado'] = True
                session['nombre_usuario'] = usuario[1]
                session['correo'] = usuario[2]
                return redirect(url_for('panel_inicio'))
            else:
                # Contraseña incorrecta
                return render_template("login.html", error="Contraseña incorrecta")
        else:
            # Correo no registrado
            return render_template("login.html", error="El correo no está registrado")

    return render_template("login.html")

# Ruta principal de bienvenida (protegida)
@app.route("/inicio")
def panel_inicio():
    # Verificamos si la clave 'logueado' existe en la sesión
    if session.get('logueado') == True:
        return render_template("index.html", usuario=session.get('nombre_usuario'))
    else:
        return redirect(url_for('login'))

# Ruta para cerrar sesión
@app.route("/logout")
def logout():
    session.clear() # Borra todos los datos y la sesión activa
    return redirect(url_for('login')) # Lo regresa al login


# NUEVA RUTA SOLO PARA MOSTRAR EL ÉXITO (GET)
@app.route("/exito")
def ingreso_exitoso():
    return render_template("ingreso_exitoso.html")

# Ejecutar la aplicacion (Siempre va al final del todo)
if __name__ == "__main__":
    app.run(debug=True)