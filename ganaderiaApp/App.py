#Librerías
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
import CUBRIDdb
import numpy as np
from numpy.lib.function_base import select

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
#Funciones útiles
#Calcular edad a partir de la fecha de nacimiento
def edad(naci):
    hoy = datetime.datetime.today()
    print(hoy)
    if hoy < naci:
        print('error en la fecha de nacimiento')
    else:
        ano = naci.year
        mes = naci.month
        dia = naci.day
 
        fecha = naci
        edad = 0
        while fecha < hoy:
            edad += 1
            fecha = datetime.datetime(ano+edad, mes, dia)
 
    return int(edad)

@app.route('/') #Decorador que indica que cada vez que un user entre a la ruta principal de la app se le devolverá una respuesta.
def index():
    return render_template('index.html')

@app.route("/vacas")
def vacas(): 
    #Obtiene los datos
    cur.execute("SELECT * FROM vaca ORDER BY cod_vaca ASC")
    datos = cur.fetchall()
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    #Los mandamos al HTML para imprimirlos
    return render_template("vacas.html", datos = datos)

@app.route("/añadir_vaca", methods=["POST"])
def add_vaca():
    if request.method == "POST":
        #Determina el código del último registro médico
        cur.execute('SELECT * FROM registro_medico ORDER BY cod_medico DESC LIMIT 1')
        datos = cur.fetchone()
        new_cod_medico = int(datos[0]) + 1 
        #Añade el registro médico básico del nuevo animal
        today = datetime.date.today()
        args1 = [new_cod_medico, "Por llenar", "Por llenar", today, 0]
        cur.execute("INSERT INTO registro_medico (cod_medico, estado, descripcion, fecha, emitido_por) VALUES (?, ?, ?, ?, ?)", args1)
        conn.commit()
        #Añade la vaca
        cod = request.form["cod"]
        nombre = request.form["nombre"]
        genetica = request.form["genetica"]
        args2 = [cod, nombre, genetica, new_cod_medico, 0]
        #Operación SQL en cuestión
        cur.execute("INSERT INTO vaca (cod_vaca, nombre, genetica_lechera, historial_medico, salida) VALUES(?, ?, ?, ?, ?)", args2)
        #Se ejecuta la operación
        conn.commit()
        flash("Vaca añadida correctamente")
        return redirect(url_for("vacas"))   

@app.route("/toros")
def toros():
    #Obtiene los datos
    cur.execute("SELECT * FROM toro ORDER BY cod_toro ASC")
    datos = cur.fetchall()
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    #Los mandamos al HTML para imprimirlos
    return render_template("toros.html", datos = datos)

@app.route("/añadir_toro", methods=["POST"])
def add_toro():
    if request.method == "POST":
        #Determina el código del último registro médico
        cur.execute('SELECT * FROM registro_medico ORDER BY cod_medico DESC LIMIT 1')
        datos = cur.fetchone()
        new_cod_medico = int(datos[0]) + 1 
        #Añade el registro médico básico del nuevo animal
        today = datetime.date.today()
        args1 = [new_cod_medico, "Por llenar", "Por llenar", today, 0]
        cur.execute("INSERT INTO registro_medico (cod_medico, estado, descripcion, fecha, emitido_por) VALUES (?, ?, ?, ?, ?)", args1)
        conn.commit()
        #Añade al toro
        cod = request.form["cod"]
        nombre = request.form["nombre"]
        ex_pajilla = request.form["ex_pajilla"]
        args2 = [cod, nombre, ex_pajilla, new_cod_medico, 0]
        #Operación sql
        cur.execute("INSERT INTO toro (cod_toro, nombre, rating, historial_medico, salida) VALUES(?, ?, ?, ?, ?)", args2)
        #Confirmación de la operación
        conn.commit()
        flash("Toro añadido correctamente")
    return redirect(url_for("toros"))

@app.route("/terneros")
def terneros():
    #Obtiene los datos
    cur.execute("SELECT * FROM ternero ORDER BY cod_ternero ASC")
    datos = cur.fetchall()
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    #Los mandamos al HTML para imprimirlos
    return render_template("terneros.html", datos = datos)

@app.route("/añadir_ternero", methods=["POST"])
def add_ternero():
    if request.method == "POST":
        #Determina el código del último registro médico
        cur.execute('SELECT * FROM registro_medico ORDER BY cod_medico DESC LIMIT 1')
        datos = cur.fetchone()
        new_cod_medico = int(datos[0]) + 1 
        #Añade el registro médico básico del nuevo animal
        today = datetime.date.today()
        args1 = [new_cod_medico, "Por llenar", "Por llenar", today, 0]
        cur.execute("INSERT INTO registro_medico (cod_medico, estado, descripcion, fecha, emitido_por) VALUES (?, ?, ?, ?, ?)", args1)
        conn.commit()
        #Añade al ternero
        cod = request.form["cod"]
        nombre = request.form["nombre"]
        fecha_nacimiento = request.form["fecha_nacimiento"]
        sex = request.form["sex"]
        #Calcula la edad a partir de la fecha de nacimiento
        temp_age = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        age = edad(temp_age)  
        peso = request.form["peso"]
        prospecto = request.form["prospecto"]
        nacido_de = request.form["nacido_de"]
        args2 = [cod, nombre, sex, fecha_nacimiento, age, peso, prospecto, new_cod_medico, 0, nacido_de]
        #Comando sql
        cur.execute("INSERT INTO ternero (cod_ternero, nombre, sexo, fecha_nacimiento, edad, peso_nacimiento, prospecto, historial_medico, salida, nacido_de) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", args2)
        #Confirmamos comando
        conn.commit()
        flash("Ternero añadido correctamente")
    return redirect(url_for("terneros"))

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

@app.route("/añadir_cliente", methods=["POST"])
def add_cliente():
    if request.method == "POST":
        cod= request.form["cod"]
        nombre= request.form["nombre"]
        tel= request.form["tel"]
        cre= request.form["cre"]
        cal= request.form["cal"]
        args=[cod, nombre, tel, cre, cal]
        #Comando sql
        cur.execute("INSERT INTO cliente (codigo, nombre, telefono, credito, calificacion) VALUES (?, ?, ?, ?, ?)", args)
        #Confirmar comando
        conn.commit()
        flash("Cliente añadido correctamente")
    return redirect(url_for("clientes"))

@app.route("/veterinarios")
def veterinarios():
    cur.execute("SELECT * FROM veterinario ORDER BY cod_vet ASC")
    datos = cur.fetchall()
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    return render_template("veterinarios.html", datos = datos)

@app.route("/añadir_veterinario", methods=["POST"])
def add_veterinario():
    if request.method == "POST":
        cod= request.form["cod"]
        nombre= request.form["nombre"]
        tel= request.form["tel"]
        correo= request.form["correo"]
        empresa= request.form["empresa"]
        emer_tel = request.form["emer_tel"]
        args=[int(cod), nombre, tel, correo, empresa, emer_tel]
        #Comando sql
        cur.execute("INSERT INTO veterinario (cod_vet, nombre, telefono, correo, empresa, telefono_emergencia) VALUES (?,?,?,?,?,?)", args)
        #Confirmar comando
        conn.commit()
        flash("Veterinario añadido correctamente")
    return redirect(url_for("veterinarios"))

@app.route("/engordes")
def engordes():
    cur.execute("SELECT * FROM engorde ORDER BY cod_engorde ASC")
    datos = cur.fetchall()
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    return render_template("engorde.html", datos = datos)

@app.route("/añadir_engorde", methods=["POST"])
def add_engorde():
    if request.method == "POST":
        #Determina el código del último registro médico
        cur.execute('SELECT * FROM registro_medico ORDER BY cod_medico DESC LIMIT 1')
        datos = cur.fetchone()
        new_cod_medico = int(datos[0]) + 1 
        #Añade el registro médico básico del nuevo animal
        today = datetime.date.today()
        args1 = [new_cod_medico, "Por llenar", "Por llenar", today, 0]
        cur.execute("INSERT INTO registro_medico (cod_medico, estado, descripcion, fecha, emitido_por) VALUES (?, ?, ?, ?, ?)", args1)
        conn.commit()
        #Añadir el engorde
        cod = request.form["cod"]
        nombre = request.form["nombre"]
        val = request.form["valor_estimado"]
        cat = request.form["categoria"]
        args = [cod, nombre, val, cat, new_cod_medico, 0]
        #Comando sql 
        cur.execute("INSERT INTO engorde (cod_engorde, nombre, valor_estimado, categoria, historial_medico, salida) VALUES(?,?,?,?,?,?)", args)
        #Confirmación del comando
        conn.commit()
        flash("Engorde añadido correctamente")
    return redirect(url_for("engordes"))

@app.route("/registro_medico/<string:id>")
def historial_medico(id):
    if id=="1c":
      print("Pon aquí la consulta general")
    else:
        cur.execute("SELECT cod_medico,estado,descripcion,fecha,emitido_por FROM registro_medico WHERE cod_medico = {0}".format(id))
        datos = cur.fetchmany()
        return render_template("registro_medico.html",datos = datos)

@app.route("/registro_ventas")
def registro_ventas():
    cur.execute('SELECT factura,cliente,precio,fecha FROM registro_venta')
    datos = cur.fetchall()
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    return render_template("registro_ventas.html",datos = datos)

#Consultas
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
