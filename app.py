from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import MySQLdb
from flask import send_file
import io
from openpyxl import Workbook


# Crear la aplicacion Flask
app = Flask(__name__)
app.secret_key = 'SuperBike'

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
                session['user_name'] = usuario[1]
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

# Consultar Usuarios

@app.route("/consultar_usuarios")
def consultar_usuarios():

    if not session.get("logueado"):
        return redirect(url_for("login"))

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute("""
        SELECT
            id,
            nombre,
            correo,
            telefono,
            nombre_usuario,
            rol
        FROM gestion_usuarios
    """)

    usuarios = cursor.fetchall()

    cursor.close()

    return render_template(
        "consultar_usuarios.html",
        usuarios=usuarios
    )


# =================
# Editar Usuario
# =================

@app.route("/editar_usuario/<int:id>", methods=["GET", "POST"])
def editar_usuario(id):

    if not session.get("logueado"):
        return redirect(url_for("login"))

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    if request.method == "POST":

        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        nombre_usuario = request.form["nombre_usuario"]
        rol = request.form["rol"]

        cursor.execute("""
            UPDATE gestion_usuarios
            SET
                nombre = %s,
                correo = %s,
                telefono = %s,
                nombre_usuario = %s,
                rol = %s
            WHERE id = %s
        """, (
            nombre,
            correo,
            telefono,
            nombre_usuario,
            rol,
            id
        ))

        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("consultar_usuarios"))

    cursor.execute("""
        SELECT *
        FROM gestion_usuarios
        WHERE id = %s
    """, (id,))

    usuario = cursor.fetchone()

    cursor.close()

    return render_template(
        "editar_usuario.html",
        usuario=usuario
    )

# ======================================
# Eliminar usuarios
# ======================================

@app.route("/eliminar_usuarios")
def eliminar_usuarios():

    if not session.get("logueado"):
        return redirect(url_for("login"))

    cursor = mysql.connection.cursor(
        MySQLdb.cursors.DictCursor
    )

    cursor.execute(
        """
        SELECT
            id,
            nombre,
            correo,
            telefono,
            nombre_usuario,
            rol
        FROM gestion_usuarios
        """
    )

    usuarios = cursor.fetchall()

    cursor.close()

    return render_template(
        "eliminar_usuarios.html",
        usuarios=usuarios
    )


# ======================================
# Eliminar usuario seleccionado
# ======================================

@app.route("/eliminar_usuario/<int:id>", methods=["POST"])
def eliminar_usuario(id):

    if not session.get("logueado"):
        return redirect(url_for("login"))

    cursor = mysql.connection.cursor()

    cursor.execute(
        """
        DELETE FROM gestion_usuarios
        WHERE id = %s
        """,
        (id,)
    )

    mysql.connection.commit()

    cursor.close()

    return redirect(
        url_for("eliminar_usuarios")
    )

#====================
# Reporte de reservas
#====================

@app.route("/reporte")
def reporte():

    if "id_usuario" not in session:
        return redirect(url_for("login"))

    fecha = request.args.get("fecha")

    cursor = mysql.connection.cursor(
        MySQLdb.cursors.DictCursor
    )

    if fecha:

        cursor.execute("""
        SELECT

            r.id_reserva,
            u.id_usuario,
            u.nombre,
            u.correo,
            r.fecha_reserva,
            r.hora_reserva,
            r.cantidad_personas,
            r.estado,
            r.observaciones
            FROM reservas r
            INNER JOIN gestion_usuarios u
            ON r.id_usuario = u.id_usuario
            WHERE r.fecha_reserva = %s
            ORDER BY r.fecha_reserva DESC, r.hora_reserva DESC
        """, (fecha,))

    else:

        cursor.execute("""
        SELECT 

            r.id_reserva,
            u.id_usuario,
            u.nombre,
            u.correo,
            r.fecha_reserva,
            r.hora_reserva,
            r.cantidad_personas,
            r.estado,
            r.observaciones
            FROM reservas r
            INNER JOIN gestion_usuarios u
            ON r.id_usuario = u.id_usuario
            ORDER BY r.fecha_reserva DESC, r.hora_reserva DESC
        """)


    reservas = cursor.fetchall()

    cursor.close()

    return render_template(
    "reporte.html",
    reservas = reservas,
    fecha = fecha
)


#=========================
# Exportar reporte a Excel
#=========================

@app.route("/reporte_excel")
def reporte_excel():

    if "id_usuario" not in session:
        return redirect(url_for("login"))

    fecha = request.args.get("fecha")

    cursor = mysql.connection.cursor(
        MySQLdb.cursors.DictCursor
    )

    if fecha:

        cursor.execute("""
        SELECT
            r.id_reserva,
            u.id_usuario,
            u.nombre,
            u.correo,
            r.fecha_reserva,
            r.hora_reserva,
            r.cantidad_personas,
            r.estado,
            r.observaciones
            FROM reservas r
            INNER JOIN gestion_usuarios u
            ON r.id_usuario = u.id_usuario
            WHERE r.fecha_reserva = %s
            ORDER BY r.fecha_reserva DESC
        """, (fecha,))

    else:

        cursor.execute("""
        SELECT
            r.id_reserva,
            u.id_usuario,
            u.nombre,
            u.correo,
            r.fecha_reserva,
            r.hora_reserva,
            r.cantidad_personas,
            r.estado,
            r.observaciones
            FROM reservas r
            INNER JOIN gestion_usuarios u
            ON r.id_usuario = u.id_usuario
            ORDER BY r.fecha_reserva DESC
        """)


    datos = cursor.fetchall()

    cursor.close()

    libro = Workbook()
    hoja = libro.active
    hoja.title = "Reporte Reservas"

    hoja.append([
        "ID Reserva",
        "ID Usuario",
        "Nombre",
        "Correo",
        "Fecha Reserva",
        "Hora Reserva",
        "Cantidad Personas",
        "Estado",
        "Observaciones"
    ])

    for fila in datos:

        hoja.append([
        fila["id_reserva"],
        fila["id_usuario"],
        fila["nombre"],
        fila["correo"],
        fila["fecha_reserva"],
        fila["hora_reserva"],
        fila["cantidad_personas"],
        fila["estado"],
        fila["observaciones"]
    ])

    archivo = io.BytesIO()

    libro.save(archivo)
    archivo.seek(0)

    return send_file(
        archivo,
        download_name="reporte_reservas.xlsx",
        as_attachment=True
    )






# Ejecutar la aplicación

if __name__ == "__main__":
    app.run(debug=True)