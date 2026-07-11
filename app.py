from flask import flask

app = Flask("Alejandro")

@app.route("/")
def inicio():
    return render_template("Hola mundo desde Flask")

if __name__ == "__main__":
    app.run(debug=True)