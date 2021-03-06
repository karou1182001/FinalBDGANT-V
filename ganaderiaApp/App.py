#Librerías
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
import CUBRIDdb
import flask
import numpy as np
from numpy.lib.function_base import select

app = Flask(__name__)

#Establecer conexión con Cubrid 
#El nombre de la base de datos debe ser GANTV
#La contraseña inazuma11
conn = CUBRIDdb.connect('CUBRID:54.227.229.70:30000:prueba:::', 'dba', 'inazuma11')
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


#VACA
@app.route("/vacas")
def vacas(): 
    #Obtiene los datos
    cur.execute("SELECT cod_vaca, nombre, genetica_lechera, COALESCE(historial_medico, 0), COALESCE(salida, 0) FROM vaca ORDER BY cod_vaca ASC")
    datos = cur.fetchall()
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    for dato in datos:
        if dato[4]=="0":
           dato[4]= "Vigente"
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
        salida = request.form["salida"]
        cad="Vaca añadida correctamente"
        if not salida:
            salida = 0
        if int(salida) == 0: 
            args2 = [cod, nombre, genetica, new_cod_medico, salida]
            #Operación SQL en cuestión
            cur.execute("INSERT INTO vaca (cod_vaca, nombre, genetica_lechera, historial_medico, salida) VALUES(?, ?, ?, ?, ?)", args2)
            #Se ejecuta la operación
            conn.commit()
        else: 
            #Buscamos primero si el código de la salida ya existe
            cur.execute("SELECT cod_registro FROM salida WHERE cod_registro = ? VALUES(?)", int(salida))
            datos = cur.fetchall()
            #Si la salida aún no existe se agrega
            #Viendo si datos está vacío
            if not(datos):
                sal_arr = [salida, "Por llenar", today, 0, 0]
                cur.execute("INSERT INTO salida (cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES(?,?,?,?,?)", sal_arr)
                conn.commit()
                cad="Vaca añadida correctamente. No olvide registrar los datos de la salida"
            args2 = [cod, nombre, genetica, new_cod_medico, int(salida)]
            #Operación SQL en cuestión
            cur.execute("INSERT INTO vaca (cod_vaca, nombre, genetica_lechera, historial_medico, salida) VALUES(?, ?, ?, ?, ?)", args2)
            #Se ejecuta la operación
            conn.commit()
        flash(cad)
        return redirect(url_for("vacas"))   

@app.route("/update_vaca", methods = ["POST"])
def update_vaca():
    if request.method == "POST":    
        cod = request.form["cod"]
        nombre = request.form["nombre"]
        genetica = request.form["genetica"]
        salida = request.form["salida"]
        args = [nombre, genetica, salida, cod]
        cad="Vaca actualizada correctamente"
        cur.execute("SELECT * FROM vaca WHERE cod_vaca = ?", cod)
        dato = cur.fetchone()
        if dato:
            if not salida: 
                salida = 0
            if int(salida) != 0:
                #Buscamos primero si el código de la salida ya existe
                cur.execute("SELECT cod_registro FROM salida WHERE cod_registro = ? VALUES(?)", int(salida))
                datos = cur.fetchall()
                #Si la salida aún no existe se agrega
                #Viendo si datos está vacío
                if not(datos):
                    today = datetime.date.today()
                    sal_arr = [salida, "Por llenar", today, 0, 0]
                    cur.execute("INSERT INTO salida (cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES(?,?,?,?,?)", sal_arr)
                    conn.commit()
                    cad="Vaca actualizada correctamente. Recuerde registrar los datos de la salida"
            cur.execute("UPDATE vaca SET nombre = ?, genetica_lechera = ?, salida = ? WHERE cod_vaca = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")
        return redirect(url_for("vacas"))

@app.route("/delete_vaca", methods=["GET"])
def delete_vaca():
    id=request.args.get('id')
    iden = id
    cur.execute("DELETE FROM vaca WHERE cod_vaca = ? VALUES(?)", iden)
    conn.commit()
    flash("La vaca ha sido eliminada correctamente")
    return redirect(url_for("vacas")) 

#TORO
@app.route("/toros")
def toros():
    #Obtiene los datos
    cur.execute("SELECT cod_toro, nombre, rating, COALESCE(historial_medico), COALESCE(salida) FROM toro ORDER BY cod_toro ASC")
    datos = cur.fetchall()
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    for dato in datos:
        if dato[4]=="0":
            dato[4]= "Vigente"
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
        salida = request.form["salida"]
        args2 = [cod, nombre, ex_pajilla, new_cod_medico, salida]
        cad="Toro añadido correctamente."
        if not salida: 
            salida = 0
        if int(salida) != 0:
            #Buscamos primero si el código de la salida ya existe
            cur.execute("SELECT cod_registro FROM salida WHERE cod_registro = ? VALUES(?)", int(salida))
            datos = cur.fetchall()
            #Si la salida aún no existe se agrega
            #Viendo si datos está vacío
            if not(datos):
                sal_arr = [salida, "Por llenar", today, 0, 0]
                cur.execute("INSERT INTO salida (cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES(?,?,?,?,?)", sal_arr)
                conn.commit()
                cad="Toro añadido correctamente. No olvide registrar los datos de la salida"
        #Operación sql
        cur.execute("INSERT INTO toro (cod_toro, nombre, rating, historial_medico, salida) VALUES(?, ?, ?, ?, ?)", args2)
        #Confirmación de la operación
        conn.commit()
        flash(cad)
    return redirect(url_for("toros"))

@app.route("/delete_toro", methods=["GET"])
def delete_toro():
    id=request.args.get('id')
    iden = id
    cur.execute("DELETE FROM toro WHERE cod_toro = ? VALUES(?)", iden)
    conn.commit()
    flash("El toro ha sido eliminado correctamente")
    return redirect(url_for("toros")) 

@app.route("/update_toro", methods = ["POST"])
def update_toro():
    if request.method == "POST":    
        cod = request.form["cod"]
        nombre = request.form["nombre"]
        rating = request.form["ex_pajilla"]
        salida = request.form["salida"]
        args = [nombre, rating, salida, cod]
        cad="Toro actualizado correctamente"
        cur.execute("SELECT * FROM toro WHERE cod_toro = ?", cod)
        dato = cur.fetchone()
        if dato:
            if not salida: 
                salida = 0
            if int(salida) != 0:
                 #Buscamos primero si el código de la salida ya existe
                cur.execute("SELECT cod_registro FROM salida WHERE cod_registro = ? VALUES(?)", int(salida))
                datos = cur.fetchall()
                #Si la salida aún no existe se agrega
                #Viendo si datos está vacío
                if not(datos):
                    today = datetime.date.today()
                    sal_arr = [salida, "Por llenar", today, 0, 0]
                    cur.execute("INSERT INTO salida (cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES(?,?,?,?,?)", sal_arr)
                    conn.commit()
                    cad="Toro actualizado correctamente. Recuerde registrar los datos de la salida"
            cur.execute("UPDATE toro SET nombre = ?, rating = ?, salida = ? WHERE cod_toro = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")
        return redirect(url_for("toros"))

#REGISTRO MÉDICO
@app.route("/registro_medico", methods=["GET"])
def historial_medico():
    id=request.args.get('id')
    if id=="1c":
        cur.execute("SELECT cod_medico,estado,descripcion,fecha,COALESCE(emitido_por, 0) FROM registro_medico")
        datos = cur.fetchall()
        return render_template("registro_medico.html",datos = datos)
    else:
        cur.execute("SELECT cod_medico,estado,descripcion,fecha,COALESCE(emitido_por, 0) FROM registro_medico WHERE cod_medico = {0}".format(id))
        datos = cur.fetchall()
        return render_template("registro_medico.html",datos = datos)

@app.route("/estuvo_enfermo", methods=["GET"])
def estuvo_enfermo():
    id=request.args.get('id')
    if id=="1c":
        cur.execute("SELECT ref_enfermo,paciente,duracion_enfermedad,fecha_de_diagnostico,enfemerdad FROM estuvo_enfermo")
        datos = cur.fetchall()
        return render_template("registro_medico.html",datos = datos)
    else:
        cur.execute("SELECT reg_enfermo,paciente,duracion_enfermedad,fecha_de_diagnostico,enfermedad FROM estuvo_enfermo WHERE paciente = {0}".format(id))
        datos = cur.fetchall()
        return render_template("estuvo_enfermo.html",datos = datos)

#REGISTRO DE VENTA
@app.route("/registro_ventas")
def registro_ventas():
    #cur.execute('SELECT factura, COALESCE(cliente, 0),precio,fecha FROM registro_venta')
    cur.execute("SELECT factura, cliente, precio, fecha FROM registro_venta")
    datos = cur.fetchall()
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    return render_template("registro_ventas.html",datos = datos)

@app.route("/añadir_venta", methods=["POST"])
def add_venta():
    if request.method == "POST":
        #Determina el código del último 
        cur.execute('SELECT * FROM registro_venta ORDER BY factura DESC LIMIT 1')
        datos = cur.fetchone()
        factura= int(datos[0]) + 1 
        cliente= request.form["cliente"]
        precio= request.form["precio"]
        fecha= request.form["fecha"]
        args=[int(factura), int(cliente), float(precio), fecha]
        #Comando sql
        cur.execute("INSERT INTO registro_venta (factura, cliente, precio, fecha) VALUES (?, ?, ?, ?)", args)
        #Confirmar comando
        conn.commit()
        flash("Venta añadida correctamente")
    return redirect(url_for("registro_ventas"))

@app.route("/update_venta", methods = ["POST"])
def update_venta():
    if request.method == "POST":    
        factura=request.form["factura"]
        cliente= request.form["cliente"]
        precio= request.form["precio"]
        fecha= request.form["fecha"]
        args=[int(cliente), precio, fecha, int(factura)]
        cad="Venta actualizada correctamente"
        cur.execute("SELECT * FROM registro_venta WHERE factura = ?", factura)
        dato = cur.fetchone()
        if dato:
            cur.execute("UPDATE registro_venta SET cliente= ?, precio= ?, fecha = ? WHERE factura = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")    
        return redirect(url_for("registro_ventas"))

@app.route("/delete_registro_de_venta", methods=["GET"])
def delete_registro_de_venta():
    id=request.args.get('id')
    iden = id
    cur.execute("DELETE FROM registro_venta WHERE factura = ? VALUES(?)", iden)
    conn.commit()
    flash("El registro de venta ha sido eliminado correctamente")
    return redirect(url_for("registro_ventas"))

#TERNERO
@app.route("/terneros")
def terneros():
    #Obtiene los datos
    cur.execute("SELECT cod_ternero, nombre, sexo, fecha_nacimiento, edad, peso_nacimiento, prospecto, COALESCE(historial_medico, 0), COALESCE(salida, 0), COALESCE(nacido_de, 0) FROM ternero ORDER BY cod_ternero ASC")
    datos = cur.fetchall()
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    for dato in datos:
        print(dato)
        if dato[8]==0:
            dato[8]= "Vigente"
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
        salida = request.form["salida"]
        nacido_de = request.form["nacido_de"]
        args2 = [cod, nombre, sex, fecha_nacimiento, age, peso, prospecto, new_cod_medico, salida, nacido_de]
        cad="Ternero añadido correctamente."
        if not salida: 
            salida = 0
        if int(salida) != 0:
            #Buscamos primero si el código de la salida ya existe
            cur.execute("SELECT cod_registro FROM salida WHERE cod_registro = ? VALUES(?)", int(salida))
            datos = cur.fetchall()
            #Si la salida aún no existe se agrega
            #Viendo si datos está vacío
            if not(datos):
                sal_arr = [salida, "Por llenar", today, 0, 0]
                cur.execute("INSERT INTO salida (cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES(?,?,?,?,?)", sal_arr)
                conn.commit()
                cad="Ternero añadido correctamente. No olvide registrar los datos de la salida"
        #Comando sql
        cur.execute("INSERT INTO ternero (cod_ternero, nombre, sexo, fecha_nacimiento, edad, peso_nacimiento, prospecto, historial_medico, salida, nacido_de) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", args2)
        #Confirmamos comando
        conn.commit()
        flash(cad)
    return redirect(url_for("terneros"))

@app.route("/update_ternero", methods = ["POST"])
def update_ternero():
    if request.method == "POST":    
        cod = request.form["cod"]
        nombre = request.form["nombre"]
        fecha_nacimiento = request.form["fecha_nacimiento"]
        sex = request.form["sex"]
        temp_age = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        age = edad(temp_age)  
        peso = request.form["peso"]
        prospecto = request.form["prospecto"]
        nacido_de = request.form["nacido_de"]
        salida = request.form["salida"]
        args = [nombre, sex, fecha_nacimiento, age, peso, prospecto, salida, nacido_de, cod]
        cad="Ternero actualizado correctamente."
        cur.execute("SELECT * FROM ternero WHERE cod_ternero = ?", cod)
        dato = cur.fetchone()
        if dato:
            if not salida: 
                salida = 0
            if int(salida) != 0:
                #Buscamos primero si el código de la salida ya existe
                cur.execute("SELECT cod_registro FROM salida WHERE cod_registro = ? VALUES(?)", int(salida))
                datos = cur.fetchall()
                #Si la salida aún no existe se agrega
                #Viendo si datos está vacío
                if not(datos):
                    today = datetime.date.today()
                    sal_arr = [salida, "Por llenar", today, 0, 0]
                    cur.execute("INSERT INTO salida (cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES(?,?,?,?,?)", sal_arr)
                    conn.commit()
                    cad="Ternero actualizado correctamente. Recuerde registrar los datos de la salida."
            cur.execute("UPDATE ternero SET nombre = ?, sexo = ?, fecha_nacimiento = ?, edad = ?, peso_nacimiento = ?, prospecto = ?, salida = ?, nacido_de = ? WHERE cod_ternero = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")
        return redirect(url_for("terneros"))

@app.route("/delete_ternero", methods=["GET"])
def delete_ternero():
    id=request.args.get('id')
    iden = id
    cur.execute("DELETE FROM ternero WHERE cod_ternero = ? VALUES(?)", iden)
    conn.commit()
    flash("El ternero ha sido eliminado correctamente")
    return redirect(url_for("terneros")) 

#CLIENTES
@app.route("/clientes", methods=['GET'])
def clientes():
    id=request.args.get('id')
    if(id == '1c'):
        cur.execute("SELECT codigo, nombre, telefono, credito, calificacion FROM cliente")
    else:
        cur.execute("SELECT codigo,nombre, telefono, credito, calificacion FROM cliente WHERE codigo =  {0}".format(id))
    tmpdatos = cur.fetchall()
    for dato in tmpdatos:
        if dato[2]=="000":
            dato[2]="No tiene"
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    tmpdatos=np.delete(tmpdatos, 0 , axis=0)
    return render_template("clientes.html",datos = tmpdatos)

@app.route("/añadir_cliente", methods=["POST"])
def add_cliente():
    if request.method == "POST":
        #Determina el código del último 
        cur.execute('SELECT * FROM cliente ORDER BY codigo DESC LIMIT 1')
        datos = cur.fetchone()
        cod= int(datos[0]) + 1 
        nombre= request.form["nombre"]
        tel= request.form["tel"]
        cre= request.form["cre"]
        cal= request.form["cal"]
        if tel=="":
            print("Entra")
            tel="000"
        args=[int(cod), nombre, tel, cre, int(cal)]
        #Comando sql
        cur.execute("INSERT INTO cliente (codigo, nombre, telefono, credito, calificacion) VALUES (?, ?, ?, ?, ?)", args)
        #Confirmar comando
        conn.commit()
        cur.execute("SELECT codigo, nombre, telefono, credito, calificacion FROM cliente")
        flash("Cliente añadido correctamente")
        tmpdatos = cur.fetchall()
        for dato in tmpdatos:
            if dato[2]=="000":
                dato[2]="No tiene"
        #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
        #En axis se especifica que se quiere eliminar una fila o columna
        tmpdatos=np.delete(tmpdatos, 0 , axis=0)
    return render_template("clientes.html",datos = tmpdatos)

@app.route("/delete_cliente", methods=["GET"])
def delete_cliente():
    id=request.args.get('id')
    iden = id
    cur.execute("DELETE FROM cliente WHERE codigo = ? VALUES(?)", iden)
    conn.commit()
    #Mostrar
    cur.execute("SELECT codigo, nombre, telefono, credito, calificacion FROM cliente")
    flash("El cliente ha sido eliminado correctamente")
    tmpdatos = cur.fetchall()
    for dato in tmpdatos:
        if dato[2]=="000":
            dato[2]="No tiene"
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    tmpdatos=np.delete(tmpdatos, 0 , axis=0)
    return render_template("clientes.html",datos = tmpdatos)

@app.route("/update_cliente", methods = ["POST"])
def update_cliente():
    if request.method == "POST":    
        cod= request.form["cod"]
        nombre= request.form["nombre"]
        tel= request.form["tel"]
        cre= request.form["cre"]
        cal= request.form["cal"]
        args=[cod, nombre, tel, cre, cal]
        if tel=="":
            tel="000"
        args=[nombre, tel, cre, cal, int(cod)]
        cad="Cliente actualizado correctamente"
        cur.execute("SELECT * FROM cliente WHERE codigo = ?", cod)
        dato = cur.fetchone()
        if dato:
            cur.execute("UPDATE cliente SET nombre= ?, telefono= ?, credito = ?, calificacion= ? WHERE codigo = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")    
        cur.execute("SELECT codigo, nombre, telefono, credito, calificacion FROM cliente")
        tmpdatos = cur.fetchall()
        for dato in tmpdatos:
            if dato[2]=="000":
                dato[2]="No tiene"
        #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
        #En axis se especifica que se quiere eliminar una fila o columna
        tmpdatos=np.delete(tmpdatos, 0 , axis=0)
        return render_template("clientes.html",datos = tmpdatos)

#VETERINARIOS
@app.route("/veterinarios")
def veterinarios():
    cur.execute("SELECT * FROM veterinario ORDER BY cod_vet ASC")
    datos = cur.fetchall()
    for dato in datos:
        if dato[2]=="000":
            dato[2]="No tiene"
        if dato[5]=="000":
            dato[5]="No tiene"
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    return render_template("veterinarios.html", datos = datos)

@app.route("/añadir_veterinario", methods=["POST"])
def add_veterinario():
    if request.method == "POST":
        #Determina el código del último 
        cur.execute('SELECT * FROM veterinario ORDER BY cod_vet DESC LIMIT 1')
        datos = cur.fetchone()
        cod_vet= int(datos[0]) + 1 
        nombre= request.form["nombre"]
        telefono= request.form["tel"]
        correo= request.form["correo"]
        empresa= request.form["empresa"]
        telefono_emergencia = request.form["emer_tel"]
        if telefono=="":
            telefono="000"
        if telefono_emergencia=="":
            telefono_emergencia="000"
        args=[int(cod_vet), nombre, telefono, correo, empresa, telefono_emergencia]
        #Comando sql
        cur.execute("INSERT INTO veterinario (cod_vet, nombre, telefono, correo, empresa, telefono_emergencia) VALUES (?,?,?,?,?,?)", args)
        #Confirmar comando
        conn.commit()
        flash("Veterinario añadido correctamente")
    return redirect(url_for("veterinarios"))

@app.route("/delete_veterinario", methods=["GET"])
def delete_vet():
    id=request.args.get('id')
    iden = id
    cur.execute("DELETE FROM veterinario WHERE cod_vet = ? VALUES(?)", iden)
    conn.commit()
    flash("El veterinario ha sido eliminado correctamente")
    return redirect(url_for("veterinarios")) 

@app.route("/update_veterinario", methods = ["POST"])
def update_veterinario():
    if request.method == "POST":    
        cod_vet= request.form["cod"]
        nombre= request.form["nombre"]
        telefono= request.form["tel"]
        correo= request.form["correo"]
        empresa= request.form["empresa"]
        telefono_emergencia = request.form["emer_tel"]
        if telefono=="":
            telefono="000"
        if telefono_emergencia=="":
            telefono_emergencia="000"
        args=[nombre, telefono, correo, empresa, telefono_emergencia, int(cod_vet)]
        cad="Veterinario actualizado correctamente"
        cur.execute("SELECT * FROM veterinario WHERE cod_vet = ?", cod_vet)
        dato = cur.fetchone()
        if dato:
            cur.execute("UPDATE veterinario SET nombre= ?, telefono= ?, correo = ?, empresa= ? , telefono_emergencia= ? WHERE cod_vet = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")
        return redirect(url_for("veterinarios"))

#ENGORDES
@app.route("/engordes")
def engordes():
    cur.execute("SELECT cod_engorde, nombre, valor_estimado, categoria, COALESCE(historial_medico, 0), COALESCE(salida, 0) FROM engorde ORDER BY cod_engorde ASC")
    datos = cur.fetchall()
    #Eliminamos la fila 0 solo por cuestión de estética, ya que esta fila representa datos nulos
    #En axis se especifica que se quiere eliminar una fila o columna
    datos=np.delete(datos, 0 , axis=0)
    for dato in datos:
        if dato[5]=="0":
            dato[5]= "Vigente"
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
        salida = request.form["salida"]
        args = [cod, nombre, val, cat, new_cod_medico, salida]
        cad="Engorde añadido correctamente."
        if not salida: 
            salida = 0
        if int(salida) != 0:
            #Buscamos primero si el código de la salida ya existe
            cur.execute("SELECT cod_registro FROM salida WHERE cod_registro = ? VALUES(?)", int(salida))
            datos = cur.fetchall()
            #Si la salida aún no existe se agrega
            #Viendo si datos está vacío
            if not(datos):
                sal_arr = [salida, "Por llenar", today, 0, 0]
                cur.execute("INSERT INTO salida (cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES(?,?,?,?,?)", sal_arr)
                conn.commit()
                cad="Engorde añadido correctamente. No olvide registrar los datos de la salida"
        #Comando sql 
        cur.execute("INSERT INTO engorde (cod_engorde, nombre, valor_estimado, categoria, historial_medico, salida) VALUES(?,?,?,?,?,?)", args)
        #Confirmación del comando
        conn.commit()
        flash(cad)
    return redirect(url_for("engordes"))

@app.route("/delete_engorde", methods=["GET"])
def delete_engorde():
    id=request.args.get('id')
    iden = id
    cur.execute("DELETE FROM engorde WHERE cod_engorde = ? VALUES(?)", iden)
    conn.commit()
    flash("El engorde ha sido eliminado correctamente")
    return redirect(url_for("engordes")) 

@app.route("/update_engorde", methods = ["POST"])
def update_engorde():
    if request.method == "POST":    
        cod = request.form["cod"]
        nombre = request.form["nombre"]
        valor_estimado = request.form["valor_estimado"]
        categoria = request.form["categoria"]
        salida = request.form["salida"]
        args = [nombre, valor_estimado, categoria, salida, cod]
        cad="Engorde actualizado correctamente."
        cur.execute("SELECT * FROM engorde WHERE cod_engorde = ?", cod)
        dato = cur.fetchone()
        if dato:
            if not salida: 
                salida = 0
            if int(salida) != 0:
                #Buscamos primero si el código de la salida ya existe
                cur.execute("SELECT cod_registro FROM salida WHERE cod_registro = ? VALUES(?)", int(salida))
                datos = cur.fetchall()
                #Si la salida aún no existe se agrega
                #Viendo si datos está vacío
                if not(datos):
                    today = datetime.date.today()
                    sal_arr = [salida, "Por llenar", today, 0, 0]
                    cur.execute("INSERT INTO salida (cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES(?,?,?,?,?)", sal_arr)
                    conn.commit()
                    cad="Ternero actualizado correctamente. Recuerde registrar los datos de la salida."
            cur.execute("UPDATE engorde SET nombre = ?, valor_estimado = ?, categoria = ?, salida = ? WHERE cod_engorde = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")
        return redirect(url_for("engordes"))

#PAJILLAS
@app.route("/pajillas")
def pajillas():
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

@app.route("/añadir_pajilla", methods=["POST"])
def add_pajilla():
    if request.method == "POST":
        #Determina el código del último 
        cur.execute('SELECT * FROM pajilla ORDER BY id_pajilla DESC LIMIT 1')
        datos = cur.fetchone()
        id_pajilla = int(datos[0]) + 1 
        fecha_embase= request.form["fecha_embase"]
        toro= request.form["toro"]
        empleado_en= request.form["empleado_en"]
        vendido_en= request.form["vendido_en"]
        if empleado_en=="":
            empleado_en=0
        if vendido_en=="":
            vendido_en=0
        args=[int(id_pajilla), fecha_embase, int(toro), int(empleado_en), int(vendido_en)]
        #Comando sql
        cur.execute("INSERT INTO pajilla (id_pajilla, fecha_embase, toro, empleado_en, vendido_en) VALUES (?, ?, ?, ?, ?)", args)
        #Confirmar comando
        conn.commit()
        cad="Pajilla añadida correctamente con cod "+ str(id_pajilla)
        flash(cad)
    return redirect(url_for("pajillas"))

@app.route("/update_pajilla", methods = ["POST"])
def update_pajilla():
    if request.method == "POST":    
        id_pajilla = request.form["id_pajilla"]
        fecha_embase= request.form["fecha_embase"]
        toro= request.form["toro"]
        empleado_en= request.form["empleado_en"]
        vendido_en= request.form["vendido_en"]
        args = [fecha_embase, toro, empleado_en, vendido_en, id_pajilla]
        cad="Pajilla actualizada correctamente"
        cur.execute("SELECT * FROM pajilla WHERE id_pajilla = ?", id_pajilla)
        dato = cur.fetchone()
        if dato:
            cur.execute("UPDATE pajilla SET fecha_embase= ?, toro= ?, empleado_en= ?, vendido_en= ? WHERE id_pajilla = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")
        return redirect(url_for("pajillas"))

@app.route("/delete_pajilla", methods=["GET"])
def delete_pajilla():
    try:
        id=request.args.get('id')
        cur.execute("DELETE FROM pajilla WHERE id_pajilla= ? VALUES(?)", id)
        conn.commit()
        flash("La pajilla ha sido eliminada correctamente")
    except:
        flash("No se puede eliminar la pajilla")
    #Mostrar tabla
    #Consulta para listar las pajillas y ver el  código de las
    #vacas y toros asociados
    cur.execute('SELECT pajilla.id_pajilla, pajilla.fecha_embase, pajilla.toro, pajilla.empleado_en, pajilla.vendido_en, inseminacion.vaca FROM pajilla CROSS JOIN inseminacion WHERE pajilla.empleado_en= inseminacion.cod_inseminacion')
    datos = cur.fetchall()
    for dato in datos:
        if dato[4]==0:
            dato[4]= "No vendido"
        if dato[5]==0:
            dato[5]= "No aplica"
    if datos[0][0]==0:
        datos=np.delete(datos, 0 , axis=0)
    return render_template('consulta_1.html',datos = datos)

#INSEMINACIONES
@app.route("/añadir_inseminacion", methods=["POST"])
def add_inseminacion():
    if request.method == "POST":
        #Determina el código del último 
        cur.execute('SELECT * FROM inseminacion ORDER BY cod_inseminacion DESC LIMIT 1')
        datos = cur.fetchone()
        cod_inseminacion = int(datos[0]) + 1 
        fecha= request.form["fecha"]
        exito= request.form["exito"]
        veterinario= request.form["veterinario"]
        vaca= request.form["vaca"]
        args=[int(cod_inseminacion), fecha, exito, int(veterinario), int(vaca)]
        #Comando sql
        cur.execute("INSERT INTO inseminacion (cod_inseminacion, fecha, exito, veterinario, vaca) VALUES (?, ?, ?, ?, ?)", args)
        #Confirmar comando
        conn.commit()
        cad="Inseminación añadida correctamente con código "+ str(cod_inseminacion)
        flash(cad)
        cur.execute('SELECT * FROM inseminacion')
        datos = cur.fetchall()
        if datos[0][0]==0:
           datos=np.delete(datos, 0 , axis=0)
        datos=sorted(datos, key=lambda cod : cod[0])
    return render_template('consulta_2.html', datos = datos, datosVaca=[])

@app.route("/consulta_2", methods=["GET"])
def consulta_2():
    id=request.args.get('id')
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

@app.route("/update_inseminacion", methods = ["POST"])
def update_inseminacion():
    if request.method == "POST":    
        cod_inseminacion = request.form["cod_inseminacion"]
        fecha= request.form["fecha"]
        exito= request.form["exito"]
        veterinario= request.form["veterinario"]
        vaca= request.form["vaca"]
        args=[fecha, exito, int(veterinario), int(vaca), int(cod_inseminacion)]
        cad="Registro de inseminación actualizado correctamente."
        cur.execute("SELECT * FROM inseminacion WHERE cod_inseminacion = ?", cod_inseminacion)
        dato = cur.fetchone()
        if dato:
            cur.execute("UPDATE inseminacion SET fecha= ?, exito= ?, veterinario= ?, vaca= ? WHERE cod_inseminacion = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")
        #Mostramos la tabla
        cur.execute('SELECT * FROM inseminacion')
        datosVaca = []
        datos = cur.fetchall()
        datos=np.delete(datos, 0 , axis=0)
        #Ordenamos la lista por código
        datos=sorted(datos, key=lambda cod : cod[0])
        return render_template('consulta_2.html', datos = datos, datosVaca=datosVaca)


@app.route("/delete_inseminacion", methods=["GET"])
def delete_inseminacion():
    try:
        id=request.args.get('id')
        cur.execute("DELETE FROM inseminacion WHERE cod_inseminacion= ? VALUES(?)", id)
        conn.commit()
        flash("El registro de inseminación ha sido eliminado correctamente")
    except:
        flash("No se puede eliminar el registro")
    #Mostrar tabla
    #Consulta para listar las pajillas y ver el  código de las
    #vacas y toros asociados
    cur.execute('SELECT * FROM inseminacion')
    datos = cur.fetchall()
    if datos[0][0]==0:
        datos=np.delete(datos, 0 , axis=0)
    return render_template('consulta_2.html',datos = datos)

#ESTADO INSEMINACIÓN
@app.route("/estado_ins", methods=["GET"])
def estado_ins():
    id=request.args.get('id')
    cur.execute('SELECT * FROM estado_inseminacion WHERE cod_inseminacion = ? VALUES(?)', id)
    datos = cur.fetchall()
    #Ordenamos la lista por código
    datos=sorted(datos, key=lambda cod : cod[0])
    return render_template('estado_ins.html', datos = datos, id=id)

@app.route("/añadir_estado_inseminacion", methods=["POST", "GET"])
def add_estado_inseminacion():
    if request.method == "POST":
        id=request.args.get('id')
        #Determina el código del último registro médico
        cur.execute('SELECT * FROM estado_inseminacion ORDER BY cod_registro DESC LIMIT 1')
        datos = cur.fetchone()
        cod_registro = int(datos[0]) + 1 
        mes= request.form["mes"]
        fecha= request.form["fecha"]
        estado= request.form["estado"]
        peso_vaca= request.form["peso_vaca"]
        args=[int(cod_registro), int(mes), fecha, estado, int(id), float(peso_vaca)]
        #Comando sql
        cur.execute("INSERT INTO estado_inseminacion (cod_registro, mes, fecha, estado, cod_inseminacion, peso_vaca) VALUES (?, ?, ?, ?, ?, ?)", args)
        #Confirmar comando
        conn.commit()
        cad="Estado de inseminación añadido correctamente con cod "+ str(cod_registro)
        flash(cad)
        cur.execute('SELECT * FROM estado_inseminacion WHERE cod_inseminacion = ? VALUES(?)', id)
        datos = cur.fetchall()
        if datos[0][0]==0:
           datos=np.delete(datos, 0 , axis=0)
        datos=sorted(datos, key=lambda cod : cod[0])
    return render_template('estado_ins.html', datos = datos, id=id)

@app.route("/update_estado_inseminacion", methods = ["POST", "GET"])
def update_estado_inseminacion():
    if request.method == "POST":
        id=request.args.get('id')
        cod_registro = request.form["cod_registro"]
        mes= request.form["mes"]
        fecha= request.form["fecha"]
        estado= request.form["estado"]
        peso_vaca= request.form["peso_vaca"]
        args=[ int(mes), fecha, estado, int(id), float(peso_vaca), int(cod_registro)]
        cad="Registro de estado de inseminación actualizado correctamente."
        cur.execute("SELECT * FROM estado_inseminacion WHERE cod_registro = ?", cod_registro)
        dato = cur.fetchone()
        if dato:
            cur.execute("UPDATE estado_inseminacion SET mes= ?, fecha= ?, estado= ?, cod_inseminacion= ?, peso_vaca= ? WHERE cod_registro = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")
        #Mostramos la tabla
        cur.execute('SELECT * FROM estado_inseminacion WHERE cod_inseminacion = ? VALUES(?)', id)
        datos = cur.fetchall()
        #Ordenamos la lista por código
        datos=sorted(datos, key=lambda cod : cod[0])
        return render_template('estado_ins.html', datos = datos, id=id)

@app.route("/delete_estado_inseminacion", methods=["GET"])
def delete_estado_inseminacion():
    try:
        id=request.args.get('id')
        cur.execute("DELETE FROM estado_inseminacion WHERE cod_registro= ? VALUES(?)", id)
        conn.commit()
        flash("El registro de estado de inseminación ha sido eliminado correctamente")
    except:
        flash("No se puede eliminar el registro")
     #Mostramos la tabla
    cur.execute('SELECT * FROM estado_inseminacion WHERE cod_inseminacion = ? VALUES(?)', id)
    datos = cur.fetchall()
    #Ordenamos la lista por código
    datos=sorted(datos, key=lambda cod : cod[0])
    return render_template('estado_ins.html', datos = datos, id=id)

#ENFERMEDAD
@app.route("/enfermedades", methods=['GET'])
def enfermedad():
    id=request.args.get('id')
    if(id == '1c'): #consulta general
        cur.execute('SELECT cod_enfermedad,nom_enfermedad,duracion_promedio,indice_letalidad,tratamiento_estandar FROM Enfermedad')
        tmpdatos = cur.fetchall()
        return render_template('Enfermedad.html',datos = tmpdatos)
    else:
        cur.execute('SELECT cod_enfermedad,nom_enfermedad,duracion_promedio,indice_letalidad,tratamiento_estandar FROM Enfermedad WHERE cod_enfermedad = {0}'.format(id))
        tmpdatos = cur.fetchall()
        return render_template('Enfermedad.html',datos = tmpdatos)

@app.route("/añadir_enfermedad", methods=["POST"])
def add_enfermedad():
    if request.method == "POST":
        #Determina el código del último registro médico
        cur.execute('SELECT * FROM enfermedad ORDER BY cod_enfermedad DESC LIMIT 1')
        datos = cur.fetchone()
        cod_enfermedad = int(datos[0]) + 1 
        nom_enfermedad= request.form["nom_enfermedad"]
        duracion_promedio= request.form["duracion_promedio"]
        indice_letalidad= request.form["indice_letalidad"]
        tratamiento_estandar= request.form["tratamiento_estandar"]
        args=[int(cod_enfermedad), nom_enfermedad, float(duracion_promedio), int(indice_letalidad), tratamiento_estandar]
        #Comando sql
        cur.execute("INSERT INTO enfermedad (cod_enfermedad, nom_enfermedad, duracion_promedio, indice_letalidad, tratamiento_estandar) VALUES (?, ?, ?, ?, ?)", args)
        #Confirmar comando
        conn.commit()
        cad="Enfermedad añadida correctamente con cod "+ str(cod_enfermedad)
        flash(cad)
        cur.execute('SELECT * FROM enfermedad ORDER BY cod_enfermedad')
        datos = cur.fetchall()
        if datos[0][0]==0:
           datos=np.delete(datos, 0 , axis=0)
        datos=sorted(datos, key=lambda cod : cod[0])
    return render_template('enfermedad.html', datos = datos)

@app.route("/delete_enfermedad", methods=["GET"])
def delete_enfermedad():
    try:
        id=request.args.get('id')
        cur.execute("DELETE FROM enfermedad WHERE cod_enfermedad= ? VALUES(?)", id)
        conn.commit()
        flash("La enfermedad ha sido eliminada correctamente")
    except:
        flash("No se puede eliminar porque hay animales asociados")
    #Mostrar tabla
    cur.execute('SELECT * FROM enfermedad ORDER BY cod_enfermedad')
    datos = cur.fetchall()
    if datos[0][0]==0:
        datos=np.delete(datos, 0 , axis=0)
    return render_template('enfermedad.html',datos = datos)

@app.route("/update_enfermedad", methods = ["POST"])
def update_enfermedad():
    if request.method == "POST":    
        cod_enfermedad = request.form["cod_enfermedad"]
        nom_enfermedad= request.form["nom_enfermedad"]
        duracion_promedio= request.form["duracion_promedio"]
        indice_letalidad= request.form["indice_letalidad"]
        tratamiento_estandar= request.form["tratamiento_estandar"]
        args=[nom_enfermedad, float(duracion_promedio), int(indice_letalidad), tratamiento_estandar, int(cod_enfermedad)]
        cad="Enfermedad actualizada correctamente"
        cur.execute("SELECT * FROM enfermedad WHERE cod_enfermedad = ?", cod_enfermedad)
        dato = cur.fetchone()
        if dato:
            cur.execute("UPDATE enfermedad SET nom_enfermedad= ?, duracion_promedio= ?, indice_letalidad= ?, tratamiento_estandar= ? WHERE cod_enfermedad = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")
        cur.execute('SELECT * FROM enfermedad ORDER BY cod_enfermedad')
        datos = cur.fetchall()
        if datos[0][0]==0:
           datos=np.delete(datos, 0 , axis=0)
        datos=sorted(datos, key=lambda cod : cod[0])
    return render_template('enfermedad.html', datos = datos)


#SALIDA
@app.route("/salidas", methods=["GET"])
def salidas():
    id=request.args.get('id')
    if(id == '1c'): #consulta general
        cur.execute('SELECT cod_registro,razon,fecha,venta,sacrificio_enfermedad FROM Salida')
        datos = cur.fetchall()
        datos=np.delete(datos, 0 , axis=0)
        for dato in datos:
            if dato[3]==0:
                dato[3]="No aplica"
            if dato[4]==0:
                dato[4]="No aplica"
        return render_template('salida.html',datos = datos)
    else:
        if id=="Vigente":
            id=0
        cur.execute('SELECT cod_registro,razon,fecha,venta,sacrificio_enfermedad FROM Salida WHERE cod_registro = {0}'.format(id))
        datos = cur.fetchall()
        return render_template('salida.html',datos = datos)

@app.route("/añadir_salida", methods=["POST"])
def add_salida():
    if request.method == "POST":
        #Determina el código del último registro médico
        cur.execute('SELECT * FROM salida ORDER BY cod_registro DESC LIMIT 1')
        datos = cur.fetchone()
        cod_registro = int(datos[0]) + 1 
        razon= request.form["razon"]
        fecha= request.form["fecha"]
        venta= request.form["venta"]
        sacrificio_enfermedad= request.form["sacrificio_enfermedad"]
        if venta=="":
            venta=0
        if sacrificio_enfermedad=="":
            sacrificio_enfermedad=0
        args=[int(cod_registro), razon, fecha, int(venta), int(sacrificio_enfermedad)]
        #Comando sql
        cur.execute("INSERT INTO salida (cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES (?, ?, ?, ?, ?)", args)
        #Confirmar comando
        conn.commit()
        cad="Salida añadida correctamente con cod "+ str(cod_registro)
        flash(cad)
        cur.execute('SELECT * FROM salida ORDER BY cod_registro')
        datos = cur.fetchall()
        if datos[0][0]==0:
           datos=np.delete(datos, 0 , axis=0)
        for dato in datos:
            if dato[3]==0:
                dato[3]="No aplica"
            if dato[4]==0:
                dato[4]="No aplica"
        datos=sorted(datos, key=lambda cod : cod[0])
    return render_template('salida.html', datos = datos)

@app.route("/delete_salida", methods=["GET"])
def delete_salida():
    try:
        id=request.args.get('id')
        cur.execute("DELETE FROM salida WHERE cod_registro = ? VALUES(?)", id)
        conn.commit()
        flash("La salida ha sido eliminada correctamente")
    except:
        flash("No se puede eliminar porque hay animales asociados")
    #Mostrar tabla
    cur.execute('SELECT cod_registro,razon,fecha,venta,sacrificio_enfermedad FROM salida')
    datos = cur.fetchall()
    datos=np.delete(datos, 0 , axis=0)
    for dato in datos:
        if dato[3]==0:
            dato[3]="No aplica"
        if dato[4]==0:
            dato[4]="No aplica"
    return render_template('salida.html',datos = datos)

@app.route("/update_salida", methods = ["POST"])
def update_salida():
    if request.method == "POST":    
        cod_registro = request.form["cod_registro"]
        razon= request.form["razon"]
        fecha= request.form["fecha"]
        venta= request.form["venta"]
        sacrificio_enfermedad= request.form["sacrificio_enfermedad"]
        if venta=="":
            venta=0
        if sacrificio_enfermedad=="":
            sacrificio_enfermedad=0
        args=[razon, fecha, int(venta), int(sacrificio_enfermedad), int(cod_registro)]
        cad="Salida actualizada correctamente"
        cur.execute("SELECT * FROM salida WHERE cod_registro = ?", cod_registro)
        dato = cur.fetchone()
        if dato:
            cur.execute("UPDATE salida SET razon= ?, fecha= ?, venta= ?, sacrificio_enfermedad= ? WHERE cod_registro = ?", args)
            flash(cad)
        else: 
            flash("El código ingresado no se encuentra registrado")
        cur.execute('SELECT * FROM salida ORDER BY cod_registro')
        datos = cur.fetchall()
        if datos[0][0]==0:
           datos=np.delete(datos, 0 , axis=0)
        for dato in datos:
            if dato[3]==0:
                dato[3]="No aplica"
            if dato[4]==0:
                dato[4]="No aplica"
        datos=sorted(datos, key=lambda cod : cod[0])
    return render_template('salida.html', datos = datos)

#----------PONER AQUÍ LAS CONSULTAS---------

#Se conecta por el puerto 3000
if __name__ == '__main__':
    app.run(port = 3000, debug=True)
