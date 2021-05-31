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
    cur.execute('SELECT cod_vaca,nombre,genetica_lechera,historial_medico,salida FROM Vaca')
    tmpdatos = cur.fetchall()
    return render_template("vacas.html",datos = tmpdatos)

@app.route("/toros")
def toros():
    cur.execute('SELECT cod_toro,nombre,rating,historial_medico,salida FROM Toro')
    datos = cur.fetchall()
    return render_template("toros.html",datos = datos)

@app.route("/registro_medico/<string:id>")
def historial_medico(id):
    cur.execute("SELECT cod_medico,estado,descripcion,fecha,emitido_por FROM registro_medico WHERE cod_medico = {0}".format(id))
    tmpdatos = cur.fetchall()
    return render_template("registro_medico.html",datos = tmpdatos)

@app.route("/registro_alimentacion/<string:id>")
def registro_alimentacion(id):
    cur.execute("SELECT cod_alimentacion,proviene_de,peso_kg,liquido_lt,fecha FROM reg_alimentacion WHERE proviene_de = {0}".format(id))
    tmpdatos = cur.fetchall()
    return render_template("registro_alimentacion.html",datos = tmpdatos)

@app.route("/engordes")
def engordes():
    cur.execute('SELECT cod_engorde,nombre,valor_estimado,categoria,historial_medico,salida FROM Engorde')
    tmpdatos = cur.fetchall()
    return render_template("engorde.html",datos = tmpdatos)


@app.route("/terneros")
def terneros():
    cur.execute('SELECT cod_ternero,nombre,sexo,fecha_nacimiento,edad,peso_nacimiento,prospecto,historial_medico,salida FROM Ternero')
    tmpdatos = cur.fetchall()
    return render_template("terneros.html",datos = tmpdatos)

@app.route("/clientes")
def clientes():
    #cur.execute('SELECT codigo,telefono,nombre,credito,calificacion FROM cliente')
    cur.execute('SELECT * FROM cliente')
    tmpdatos = cur.fetchall()
    print(tmpdatos)
    return render_template("clientes.html",datos = tmpdatos)

@app.route("/registro_ventas")
def registro_ventas():
    cur.execute('SELECT factura,cliente,precio,fecha FROM registro_venta')
    tmpdatos = cur.fetchall()
    return render_template("registro_ventas.html",datos = tmpdatos)

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

@app.route("/consulta_2/<string:id>")
def consulta_2(id):
    datosVaca = []
    if id=="1c":
        #Consulta de las vacas que han sido inseminadas con información asociada,
        #con una opción que permita ver cuáles quedaron embarazadas y opción para ver su estado
        #de inseminación
        cur.execute('SELECT * FROM inseminacion')
        datos = cur.fetchall()
        #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
        #En axis se especifica que se quiere eliminar una fila o columna
        datos=np.delete(datos, 0 , axis=0)
    elif id=="2c":
        cur.execute('SELECT * FROM inseminacion WHERE exito = ? VALUES(?)', 'si')
        datos = cur.fetchall()
    else:
        cur.execute('SELECT * FROM inseminacion')
        datos = cur.fetchall()
        datos=np.delete(datos, 0 , axis=0)
        cur.execute('SELECT vaca.cod_vaca, vaca.nombre, vaca.genetica_lechera, vaca.salida FROM vaca WHERE cod_vaca = ? VALUES(?)', id)
        datosVaca = cur.fetchall()

    #Ordenamos la lista por código
    datos=sorted(datos, key=lambda cod : cod[0])
    return render_template('consulta_2.html', datos = datos, datosVaca=datosVaca)


@app.route("/estado_ins/<string:id>")
def estado_ins(id):
    cur.execute('SELECT * FROM estado_inseminacion WHERE cod_inseminacion = ? VALUES(?)', id)
    datos = cur.fetchall()
    #Ordenamos la lista por código
    datos=sorted(datos, key=lambda cod : cod[0])
    return render_template('estado_ins.html', datos = datos)
    


#----------PONER AQUÍ LAS CONSULTAS---------

#Se conecta por el puerto 3000
if __name__ == '__main__':
    app.run(port = 3000, debug=True)
