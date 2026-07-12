from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route("/")
def inicio():
    return render_template("index.html")

# Página Catálogo
@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")

# Página Contáctanos
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

# Página Quiénes somos
@app.route("/quienessomos")
def quienessomos():
    return render_template("quienessomos.html")

# Página Login
@app.route("/login")
def login():
    return render_template("login.html")

# Página Registro
@app.route("/registro")
def registro():
    return render_template("registro.html")

if __name__ == "__main__":
    app.run(debug=True)