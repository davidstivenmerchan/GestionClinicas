from flask import Flask, render_template, request, redirect, url_for, flash, jsonify # type: ignore

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Usuarios simulados (en una base de datos esto sería diferente)
usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in usuarios and usuarios[username] == password:
        return render_template('index.html')
    else:
        flash("Usuario o contraseña incorrectos.")
        return redirect(url_for('home'))
    
@app.route('/index')
def dashboard():
    return render_template('index.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/reset-password', methods=['POST'])
def reset_password():
    username = request.form['username']
    
    # Aquí podrías implementar la lógica de restablecimiento de contraseña (ej. enviar un email)
    flash(f"Instrucciones para restablecer la contraseña han sido enviadas a {username}.")
    return redirect(url_for('home'))

@app.route('/citas')
def citas_generate():
    return render_template('citas.html')

@app.route('/historia')
def historia_clinica():
    return render_template('historia_clinica.html')

@app.route('/laboratorios')
def laboratorios():
    return render_template('laboratorios.html')


@app.route('/')
def autorizacion():
    return render_template('autorizacion.html')

@app.route('/autorizaciones')
def autorizaciones():
    return render_template('autorizacion.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    numero_orden = request.json.get('numero_orden')
    # Simulación de búsqueda
    if numero_orden == "12345":
        response_message = "Autorización encontrada para el número de orden 12345."
    else:
        response_message = "No se encontró la autorización para este número de orden."
    
    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(debug=True)


