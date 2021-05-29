#Librerías
from flask import Flask, render_template, request, redirect, url_for, flash
import CUBRIDdb

app = Flask(__name__)

#Establecer conexión con Cubrid 
#El nombre de la base de datos debe ser GANTV
#La contraseña inazuma11
conn = CUBRIDdb.connect('CUBRID:localhost:30000:GANTV:::', 'dba', 'inazuma11')
#Init cursor
cur = conn.cursor()

#Iniciar una sesión
app.secret_key='mysecretkey'

#cur.execute("") ejecuta operaciones SQL e.g. cur.execute("SELECT * FROM user WHERE id = 10") 
#cur.execute("DELETE FROM user WHERE id = 10") 

@app.route('/') #Decorador que indica que cada vez que un user entre a la ruta principal de la app se le devolverá una respuesta.
def index():
    return render_template('index.html')

@app.route("/vacas")
def vacas(): 
    return render_template("vacas.html")

@app.route("/toros")
def toros():
    return render_template("toros.html")

@app.route("/terneros")
def terneros():
    return render_template("terneros.html")

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

@app.route("/veterinarios")
def veterinarios():
    return render_template("veterinarios.html")

#----------PONER AQUÍ LAS CONSULTAS---------

#Se conecta por el puerto 3000
if __name__ == '__main__':
    app.run(port = 3000, debug=True)
