from flask import Flask, redirect, request, jsonify, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    role = "admin"
    notes = ["Nota 1", "Nota 2", "Nota 3"]
    return render_template("home.html", role=role, notes=notes)


@app.route("/about")
def about():
    return "Esta es una aplicación de notas simple."

@app.route("/contact",  methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Formulario enviado correctamente.", 201
    return "Página de contacto"

@app.route("/api/info")
def api_info():
    data = {
        "app": "Notes App",
        "version": "1.0.0",
        "author": "Ale"
    } 
    return jsonify(data), 200

@app.route("/confirmacion")
def confirmation():
    return "Prueba"

@app.route("/crear-nota", methods=['POST', 'GET'])
def create_note():
    if request.method == 'POST':
        nota = request.form.get('nota', "No encontrada")
        return redirect(
            url_for("confirmation", nota=nota )
        )
    return render_template("note_form.html")