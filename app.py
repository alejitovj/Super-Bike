from flask import Flask, render_template, request, session, redirect, url_for, send_file
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import MySQLdb
from openpyxl import Workbook
import io


# ============================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ============================================================

app = Flask(__name__)

# Clave secreta para manejar las sesiones
app.secret_key = "SuperBike"


# ============================================================
# CONFIGURACIÓN DE MYSQL
# ============================================================

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "super_bike"

mysql = MySQL(app)


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def usuario_logueado():
    """
    Comprueba si existe una sesión activa.
    """
    return session.get("logueado") is True


def administrador():
    """
    Comprueba si el usuario actualmente conectado
    tiene rol de administrador.
    """
    return session.get("rol") == "admin"


def proteger_ruta():
    """
    Si el usuario no está logueado, lo envía al login.
    """
    if not usuario_logueado():
        return redirect(url_for("login"))

    return None


def proteger_administrador():
    """
    Comprueba que el usuario esté logueado y además
    tenga permisos de administrador.
    """
    if not usuario_logueado():
        return redirect(url_for("login"))

    if not administrador():
        return redirect(url_for("panel_inicio"))

    return None


# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

@app.route("/")
def inicio():
    return render_template(
        "index.html",
        usuario=session.get("user_name")
    )


# ============================================================
# CATÁLOGO
# ============================================================

@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")


# ============================================================
# CONTACTO
# ============================================================

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


# ============================================================
# QUIÉNES SOMOS
# ============================================================

@app.route("/quienes-somos")
def quienessomos():
    return render_template("quienessomos.html")


# ============================================================
# COMPROBAR CONEXIÓN CON LA BASE DE DATOS
# ============================================================

@app.route("/conexion")
def conexion():
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

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


# ============================================================
# REGISTRO DE USUARIO
# ============================================================

@app.route("/registro", methods=["GET", "POST"])
def registro():

    if request.method == "POST":

        nombre_usuario = request.form["nombre_usuario"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        contraseña = request.form["password"]

        # Encriptar contraseña
        contraseña_encriptada = generate_password_hash(contraseña)

        try:

            cursor = mysql.connection.cursor()

            # Comprobar si el correo ya existe
            cursor.execute(
                """
                SELECT id
                FROM gestion_usuarios
                WHERE correo = %s
                """,
                (correo,)
            )

            usuario_existente = cursor.fetchone()

            if usuario_existente:
                cursor.close()

                return render_template(
                    "registro.html",
                    error="El correo ya está registrado"
                )

            # Registrar usuario
            cursor.execute(
                """
                INSERT INTO gestion_usuarios
                (
                    nombre_usuario,
                    correo,
                    contraseña,
                    telefono,
                    rol
                )
                VALUES (%s, %s, %s, %s)
                """,
                (
                    nombre_usuario,
                    correo,
                    contraseña_encriptada,
                    telefono,
                    "usuario"
                )
            )

            mysql.connection.commit()
            cursor.close()

            return redirect(url_for("ingreso_exitoso"))

        except Exception as error:

            return render_template(
                "registro.html",
                error=f"Error al registrar: {error}"
            )

    return render_template("registro.html")


# ============================================================
# INICIO DE SESIÓN
# ============================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        correo = request.form["correo"]
        contraseña = request.form["password"]

        try:

            cursor = mysql.connection.cursor(
                MySQLdb.cursors.DictCursor
            )

            cursor.execute(
                """
                SELECT
                    id,
                    nombre,
                    correo,
                    contraseña,
                    telefono,
                    nombre_usuario,
                    rol
                FROM gestion_usuarios
                WHERE correo = %s
                """,
                (correo,)
            )

            usuario = cursor.fetchone()

            cursor.close()

            # Comprobar si existe el usuario
            if not usuario:

                return render_template(
                    "login.html",
                    error="El correo no está registrado"
                )

            # Comprobar contraseña
            if not check_password_hash(
                usuario["contraseña"],
                contraseña
            ):

                return render_template(
                    "login.html",
                    error="Contraseña incorrecta"
                )

            # ==================================================
            # GUARDAR DATOS EN LA SESIÓN
            # ==================================================

            session["logueado"] = True
            session["id_usuario"] = usuario["id"]
            session["user_name"] = usuario["nombre_usuario"]
            session["correo"] = usuario["correo"]
            session["rol"] = usuario["rol"]

            return redirect(url_for("panel_inicio"))

        except Exception as error:

            return render_template(
                "login.html",
                error=f"Error al iniciar sesión: {error}"
            )

    return render_template("login.html")


# ============================================================
# PÁGINA DE INICIO DESPUÉS DEL LOGIN
# ============================================================

@app.route("/inicio")
def panel_inicio():

    proteccion = proteger_ruta()

    if proteccion:
        return proteccion

    return render_template(
        "index.html",
        usuario=session.get("user_name")
    )


# ============================================================
# CERRAR SESIÓN
# ============================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ============================================================
# REGISTRO EXITOSO
# ============================================================

@app.route("/exito")
def ingreso_exitoso():
    return render_template("ingreso_exitoso.html")


# ============================================================
# CONSULTAR USUARIOS
# ============================================================

@app.route("/consultar_usuarios")
def consultar_usuarios():

    proteccion = proteger_administrador()

    if proteccion:
        return proteccion

    try:

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
            ORDER BY id DESC
            """
        )

        usuarios = cursor.fetchall()

        cursor.close()

        return render_template(
            "consultar_usuarios.html",
            usuarios=usuarios
        )

    except Exception as error:

        return f"Error al consultar usuarios: {error}", 500


# ============================================================
# EDITAR USUARIO
# ============================================================

@app.route("/editar_usuario/<int:id>", methods=["GET", "POST"])
def editar_usuario(id):

    proteccion = proteger_administrador()

    if proteccion:
        return proteccion

    try:

        cursor = mysql.connection.cursor(
            MySQLdb.cursors.DictCursor
        )

        # ----------------------------------------------------
        # ACTUALIZAR USUARIO
        # ----------------------------------------------------

        if request.method == "POST":

            nombre = request.form["nombre"]
            correo = request.form["correo"]
            telefono = request.form["telefono"]
            nombre_usuario = request.form["nombre_usuario"]
            rol = request.form["rol"]

            cursor.execute(
                """
                UPDATE gestion_usuarios
                SET
                    nombre = %s,
                    correo = %s,
                    telefono = %s,
                    nombre_usuario = %s,
                    rol = %s
                WHERE id = %s
                """,
                (
                    nombre,
                    correo,
                    telefono,
                    nombre_usuario,
                    rol,
                    id
                )
            )

            mysql.connection.commit()

            cursor.close()

            return redirect(
                url_for("consultar_usuarios")
            )

        # ----------------------------------------------------
        # OBTENER USUARIO
        # ----------------------------------------------------

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
            WHERE id = %s
            """,
            (id,)
        )

        usuario = cursor.fetchone()

        cursor.close()

        # Usuario no encontrado
        if not usuario:
            return "Usuario no encontrado", 404

        return render_template(
            "editar_usuario.html",
            usuario=usuario
        )

    except Exception as error:

        return f"Error al editar usuario: {error}", 500


# ============================================================
# PÁGINA PARA ELIMINAR USUARIOS
# ============================================================

@app.route("/eliminar_usuarios")
def eliminar_usuarios():

    proteccion = proteger_administrador()

    if proteccion:
        return proteccion

    try:

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
            ORDER BY id DESC
            """
        )

        usuarios = cursor.fetchall()

        cursor.close()

        return render_template(
            "eliminar_usuarios.html",
            usuarios=usuarios
        )

    except Exception as error:

        return f"Error al cargar usuarios: {error}", 500


# ============================================================
# ELIMINAR USUARIO
# ============================================================

@app.route("/eliminar_usuario/<int:id>", methods=["POST"])
def eliminar_usuario(id):

    proteccion = proteger_administrador()

    if proteccion:
        return proteccion

    try:

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

    except Exception as error:

        return f"Error al eliminar usuario: {error}", 500


# ============================================================
# REPORTE DE USUARIOS
# ============================================================

@app.route("/reporte")
def reporte():

    proteccion = proteger_administrador()

    if proteccion:
        return proteccion

    try:

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
            ORDER BY id DESC
            """
        )

        usuarios = cursor.fetchall()

        cursor.close()

        return render_template(
            "reporte.html",
            usuarios=usuarios
        )

    except Exception as error:

        return f"Error al generar reporte: {error}", 500


# ============================================================
# EXPORTAR REPORTE A EXCEL
# ============================================================

@app.route("/reporte_excel")
def reporte_excel():

    proteccion = proteger_administrador()

    if proteccion:
        return proteccion

    try:

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
            ORDER BY id DESC
            """
        )

        datos = cursor.fetchall()

        cursor.close()

        # ----------------------------------------------------
        # CREAR ARCHIVO EXCEL
        # ----------------------------------------------------

        libro = Workbook()

        hoja = libro.active
        hoja.title = "Reporte Usuarios"

        # Encabezados
        hoja.append(
            [
                "ID",
                "Nombre",
                "Correo",
                "Teléfono",
                "Usuario",
                "Rol"
            ]
        )

        # Datos
        for fila in datos:

            hoja.append(
                [
                    fila["id"],
                    fila["nombre"],
                    fila["correo"],
                    fila["telefono"],
                    fila["nombre_usuario"],
                    fila["rol"]
                ]
            )

        # ----------------------------------------------------
        # GUARDAR EXCEL EN MEMORIA
        # ----------------------------------------------------

        archivo = io.BytesIO()

        libro.save(archivo)

        archivo.seek(0)

        # ----------------------------------------------------
        # DESCARGAR ARCHIVO
        # ----------------------------------------------------

        return send_file(
            archivo,
            download_name="reporte_usuarios.xlsx",
            as_attachment=True
        )

    except Exception as error:

        return f"Error al generar el archivo Excel: {error}", 500


# ============================================================
# EJECUTAR APLICACIÓN
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)