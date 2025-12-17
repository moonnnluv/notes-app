from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hola():
    return "Hola Mundo!"


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
        "version": 1.0,
        "author": "Ale"
    } 
    return jsonify(data)