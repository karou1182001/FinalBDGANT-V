#Librerías
from flask import Flask, render_template, request, redirect, url_for, flash
import CUBRIDdb
import numpy as np

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

@app.route("/consulta_1")
def consulta_1():
    #Consulta para listar las pajillas y ver el  código de las
    #vacas y toros asociados
    cur.execute('SELECT pajilla.id_pajilla, pajilla.fecha_embase, pajilla.toro, pajilla.empleado_en, pajilla.vendido_en, inseminacion.vaca FROM pajilla CROSS JOIN inseminacion WHERE pajilla.empleado_en= inseminacion.cod_inseminacion')
    datos = cur.fetchall()
    
    for dato in datos:
        if dato[4]==0:
            dato[4]= "No vendido"
        if dato[5]==0:
            dato[5]= "No aplica"
    
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    return render_template('consulta_1.html', datos = datos)

@app.route("/consulta_2")
def consulta_2():
    #Consulta de las vacas de las vacas que han sido inseminadas con información asociada,
    #con una opción que permita ver cuáles quedaron embarazadas y opción para ver su estado
    #de inseminación
    cur.execute('SELECT * FROM inseminacion ORDER BY cod_inseminacion ASC')
    datos = cur.fetchall()
    return render_template('consulta_2.html', datos = datos)


#----------PONER AQUÍ LAS CONSULTAS---------

#Se conecta por el puerto 3000
if __name__ == '__main__':
    app.run(port = 3000, debug=True)
