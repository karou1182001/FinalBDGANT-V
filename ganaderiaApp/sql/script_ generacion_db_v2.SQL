

--DROP DATABASE IF EXISTS GANTV;
--CREATE DATABASE GANTV;
--USE DATABASE GANTV;
--1

DROP TABLE IF EXISTS destete,reg_lechero; --n7
DROP TABLE IF EXISTS pajilla, estado_inseminacion,ternero; --n6
DROP TABLE IF EXISTS inseminacion; --n5
DROP TABLE IF EXISTS vaca, toro, engorde; --n4
DROP TABLE IF EXISTS salida,estuvo_enfermo,aplicacion_vacunas,reg_alimentacion; --n3
DROP TABLE IF EXISTS registro_medico,defuncion,registro_venta; --n2
DROP TABLE IF EXISTS cliente,vacuna, veterinario, enfermedad;  --n1

---Nivel 1

CREATE TABLE  cliente(

    codigo INTEGER PRIMARY KEY,
		nombre VARCHAR(30),
    telefono VARCHAR(20),
    credito FLOAT,
    calificacion INTEGER

);

CREATE TABLE enfermedad(
	cod_enfermedad INTEGER PRIMARY KEY,
	nom_enfermedad VARCHAR(20),
	duracion_promedio FLOAT, 	--duracion de la enfermedad en semanas
	indice_letalidad INTEGER,	--cuantas vacas q han sido infectadas con esta enfermedad han muerto
	tratamiento_estandar VARCHAR(40) --descripcion de los medicamentos a dar por parte de un veterinario

);

CREATE TABLE vacuna(
	cod_vacuna INTEGER PRIMARY KEY,
	nombre VARCHAR(20),
	duracion INTEGER, --duracion de la inmmunidad garantizada por la vacuna
	descripcion VARCHAR(40)

);


CREATE TABLE veterinario(
	cod_vet INTEGER PRIMARY KEY,
	nombre VARCHAR(20),
	telefono VARCHAR(20),
	correo VARCHAR(20),
	empresa VARCHAR(20),
	telefono_emergencia VARCHAR(20) --de alguien a contactar en caso de emergencia

);

---Nivel 2


CREATE TABLE registro_medico(
	cod_medico INTEGER PRIMARY KEY,
	estado VARCHAR(15),  ---enfermo, saludable, o cosas por el estilo
	descripcion VARCHAR(40),
	fecha DATE,
	emitido_por INTEGER FOREIGN KEY REFERENCES veterinario(cod_vet)
);

CREATE TABLE registro_venta(

	factura INTEGER PRIMARY KEY,
	cliente INTEGER FOREIGN KEY REFERENCES cliente(codigo),
	precio FLOAT,
	fecha DATE

);

CREATE TABLE defuncion(
	reg_defuncion INTEGER PRIMARY KEY,
	causa INTEGER FOREIGN KEY REFERENCES enfermedad(cod_enfermedad),
	veterinario_certifica INTEGER FOREIGN KEY REFERENCES veterinario(cod_vet)

);

---Nivel 3

CREATE TABLE estuvo_enfermo (
  reg_enfermo INTEGER PRIMARY KEY,
  paciente INTEGER FOREIGN KEY REFERENCES  registro_medico(cod_medico),
	duracion_enfermedad FLOAT,
	fecha_de_diagnostico DATE,
	enfermedad INTEGER FOREIGN KEY REFERENCES enfermedad(cod_enfermedad)

);

CREATE TABLE aplicacion_vacunas(
	cod_apva INTEGER PRIMARY KEY,
	vacuna_aplicada INTEGER FOREIGN KEY REFERENCES vacuna(cod_vacuna),
	paciente INTEGER FOREIGN KEY REFERENCES registro_medico(cod_medico),
	fecha DATE

);


CREATE TABLE reg_alimentacion(
	cod_alimentacion INTEGER PRIMARY KEY,
	proviene_de INTEGER FOREIGN KEY REFERENCES registro_medico(cod_medico),
	peso_kg FLOAT,
	liquido_lt FLOAT,
	fecha DATE
);

CREATE TABLE salida(
	cod_registro INTEGER PRIMARY KEY,
	razon VARCHAR(40),
	fecha DATE,
	venta INTEGER FOREIGN KEY REFERENCES registro_venta(factura),
	--sacrificio_enfermedad INTEGER UNIQUE FOREIGN KEY REFERENCES defuncion(reg_defuncion)
	sacrificio_enfermedad INTEGER FOREIGN KEY REFERENCES defuncion(reg_defuncion)

);



---Nivel 4
CREATE TABLE vaca (
	cod_vaca INTEGER PRIMARY KEY,
	nombre VARCHAR(20),
	genetica_lechera VARCHAR(20),
	--historial_medico INTEGER UNIQUE FOREIGN KEY REFERENCES  registro_medico(cod_medico) ,
	historial_medico INTEGER UNIQUE FOREIGN KEY REFERENCES  registro_medico(cod_medico) ,
	--salida INTEGER UNIQUE FOREIGN KEY REFERENCES  salida(cod_registro)
	salida INTEGER FOREIGN KEY REFERENCES  salida(cod_registro)

);

CREATE TABLE toro (
	cod_toro INTEGER PRIMARY KEY,
	nombre VARCHAR(20),
	rating FLOAT, -- cuantos de las pajillas que fueron usados de el han dado embarazos exitosos
	--historial_medico INTEGER UNIQUE FOREIGN KEY REFERENCES  registro_medico(cod_medico) ,
	historial_medico INTEGER UNIQUE FOREIGN KEY REFERENCES  registro_medico(cod_medico) ,
	--salida INTEGER UNIQUE FOREIGN KEY REFERENCES  salida(cod_registro)
	salida INTEGER FOREIGN KEY REFERENCES  salida(cod_registro)

);

CREATE TABLE engorde (
	cod_engorde INTEGER PRIMARY KEY,
	nombre VARCHAR(20),
	valor_estimado FLOAT,
	categoria VARCHAR(20),
	--historial_medico INTEGER UNIQUE FOREIGN KEY REFERENCES  registro_medico(cod_medico) ,
	historial_medico INTEGER UNIQUE FOREIGN KEY REFERENCES  registro_medico(cod_medico) ,
	--salida INTEGER UNIQUE FOREIGN KEY REFERENCES  salida(cod_registro)
	salida INTEGER FOREIGN KEY REFERENCES  salida(cod_registro)

);

---Nivel 5

CREATE TABLE inseminacion(
	cod_inseminacion INTEGER PRIMARY KEY,
	fecha DATE,
	exito VARCHAR(2), -- se logro una inseminacion o no ("si" o "no" )
	--	veterinario INTEGER UNIQUE FOREIGN KEY REFERENCES veterinario(cod_vet),
	veterinario INTEGER FOREIGN KEY REFERENCES veterinario(cod_vet),
	vaca INTEGER FOREIGN KEY REFERENCES vaca(cod_vaca)

);
---Nivel 6

CREATE TABLE ternero (
	cod_ternero  INTEGER PRIMARY KEY,
	nombre VARCHAR(20),
	sexo  VARCHAR(15),
	fecha_nacimiento DATETIME,
	edad INTEGER,
	peso_nacimiento FLOAT,
	prospecto VARCHAR(20),
	--historial_medico INTEGER UNIQUE FOREIGN KEY REFERENCES  registro_medico(cod_medico) ,
	historial_medico INTEGER UNIQUE FOREIGN KEY REFERENCES  registro_medico(cod_medico) ,
	--salida INTEGER UNIQUE FOREIGN KEY REFERENCES  salida(cod_registro)
	salida INTEGER FOREIGN KEY REFERENCES  salida(cod_registro),
  nacido_de INTEGER FOREIGN KEY REFERENCES  inseminacion(cod_inseminacion)

);

CREATE TABLE pajilla(
	id_pajilla INTEGER PRIMARY KEY,
	fecha_embase DATE,
	toro INTEGER FOREIGN KEY REFERENCES toro(cod_toro),
	--empleado_en INTEGER UNIQUE FOREIGN KEY REFERENCES inseminacion(cod_inseminacion) ,
	empleado_en INTEGER FOREIGN KEY REFERENCES inseminacion(cod_inseminacion) ,
	vendido_en INTEGER FOREIGN KEY REFERENCES registro_venta(factura)

);

CREATE TABLE estado_inseminacion(
	cod_registro INTEGER PRIMARY KEY,
	mes INTEGER, --,meses desde que empezo la inseminacion
	fecha DATE,
	estado VARCHAR(15), --descripcion de una palabra del estado de la concepcion "terminado","saludable","riesgoso"
	cod_inseminacion INTEGER FOREIGN KEY REFERENCES inseminacion(cod_inseminacion),
	peso_vaca FLOAT

);


--- Nivel 7

CREATE TABLE destete(
	cod_destete INTEGER PRIMARY KEY,
	fecha DATE,
	vaca INTEGER UNIQUE FOREIGN KEY REFERENCES vaca(cod_vaca),
	toro INTEGER UNIQUE FOREIGN KEY REFERENCES toro(cod_toro) ,
	engorde INTEGER UNIQUE FOREIGN KEY REFERENCES engorde(cod_engorde) ,
	ternero INTEGER UNIQUE FOREIGN KEY REFERENCES ternero(cod_ternero)

)

CREATE TABLE reg_lechero(
	cod_lec INTEGER PRIMARY KEY,
	pertenece_a INTEGER FOREIGN KEY REFERENCES vaca(cod_vaca),
	inseminacion_asociada INTEGER UNIQUE FOREIGN KEY REFERENCES inseminacion(cod_inseminacion) ,
	fecha DATE,
	cantidad_lt FLOAT
)