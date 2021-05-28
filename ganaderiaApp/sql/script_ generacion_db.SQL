

--DROP DATABASE IF EXISTS GANTV;
--CREATE DATABASE GANTV;
--USE DATABASE GANTV;
--1
DROP TABLE IF EXISTS  registro_venta,cliente,salida,defuncion,salida,enfermedad;

CREATE TABLE  cliente(

    codigo INTEGER PRIMARY KEY,
		nombre VARCHAR(30),
    telefono VARCHAR(20),
    credito FLOAT,
    calificacion INTEGER

);

--2
CREATE TABLE registro_venta(

	factura INTEGER PRIMARY KEY,
	cliente INTEGER FOREIGN KEY REFERENCES cliente(codigo),
	precio FLOAT,
	fecha DATETIME

);


CREATE TABLE enfermedad(
	cod_enfermedad INTEGER PRIMARY KEY,
	nom_enfermedad VARCHAR(20),
	duracion_promedio FLOAT, 	--duracion de la enfermedad en semanas
	indice_letalidad INTEGER,	--cuantas vacas q han sido infectadas con esta enfermedad han muerto
	tratamiento_estandar VARCHAR(40) --descripcion de los medicamentos a dar por parte de un veterinario

);


CREATE TABLE defuncion(
	reg_defuncion INTEGER PRIMARY KEY,
	causa INTEGER FOREIGN KEY REFERENCES enfermedad(cod_enfermedad),
	veterinario_certifica INTEGER FOREIGN KEY REFERENCES veterinario(cod_vet)

);

--3
CREATE TABLE salida(
	cod_registro INTEGER PRIMARY KEY,
	razon VARCHAR(40),
	fecha DATETIME,
	venta INTEGER FOREIGN KEY REFERENCES registro_venta(factura),
	sacrificio_enfermedad INTEGER FOREIGN KEY REFERENCES defuncion(reg_defuncion) UNIQUE

);

--4
CREATE defuncion(
	reg_defuncion INTEGER PRIMARY KEY,
	causa INTEGER FOREIGN KEY REFERENCES enfermedad(cod_enfermedad),
	veterinario_certifica INTEGER FOREIGN KEY REFERENCES veterinario(cod_vet)

);

--5
CREATE TABLE enfermedad(
	cod_enfermedad INTEGER PRIMARY KEY,
	nom_enfermedad VARCHAR(20),
	duracion_promedio FLOAT, 	--duracion de la enfermedad en semanas
	indice_letalidad INTEGER,	--cuantas vacas q han sido infectadas con esta enfermedad han muerto
	tratamiento_estandar VARCHAR(40) --descripcion de los medicamentos a dar por parte de un veterinario

);

--6
CREATE TABLE estuvo_enfermo (
  reg_enfermo INTEGER PRIMARY KEY,
  paciente INTEGER FOREIGN KEY REFERENCES  registro_medico(cod_medico),
	duracion_enfermedad FLOAT,
	fecha_de_diagnostico DATETIME,
	enfermedad INTEGER FOREIGN KEY REFERENCES enfermedad(cod_enfermedad)

);

--7
CREATE TABLE registro_medico(
	cod_medico INTEGER PRIMARY KEY,
	estado VARCHAR(15),  ---enfermo, saludable, o cosas por el estilo
	descripcion VARCHAR(40),
	fecha DATETIME,
	emitido_por INTEGER FOREIGN KEY REFERENCES veterinario(cod_vet)
);

--8
CREATE TABLE veterinario(
	cod_vet PRIMARY KEY,
	nombre VARCHAR(20),
	telefono VARCHAR(20),
	correo VARCHAR(20),
	empresa VARCHAR(20),
	telefono_emergencia VARCHAR(20) --de alguien a contactar en caso de emergencia

);


--9
CREATE TABLE aplicacion_vacunas(
	cod_apva INTEGER PRIMARY KEY,
	vacuna_aplicada INTEGER FOREIGN KEY REFERENCES vacuna(cod_vacuna),
	paciente INTEGER FOREIGN KEY REFERENCES registro_medico(cod_medico),
	fecha DATETIME

);

--10
CREATE TABLE vacuna(
	cod_vacuna INTEGER PRIMARY KEY,
	nombre VARCHAR(20),
	duracion INTEGER, --duracion de la inmmunidad garantizada por la vacuna
	descripcion VARCHAR(40)

);

--11
CREATE TABLE reg_alimentacion(
	cod_alimentacion INTEGER PRIMARY KEY,
	proviene_de INTEGER FOREIGN KEY REFERENCES registro_medico(cod_medico),
	peso_kg FLOAT,
	liquido_lt FLOAT,
	fecha DATETIME
);

--12
CREATE TABLE inseminacion(
	cod_inseminacion INTEGER PRIMARY KEY,
	fecha DATETIME,
	exito BOOLEAN, -- se logro una inseminacion o no
	veterinario INTEGER FOREIGN KEY REFERENCES veterinario(cod_veterinario) UNIQUE,
	vaca INTEGER FOREIGN KEY REFRENCES vaca(cod_vaca)

);

--13
CREATE TABLE estado_inseminacion(
	cod_registro INTEGER PRIMARY KEY,
	mes INTEGER, --,meses desde que empezo la inseminacion
	fecha DATETIME,
	estado VARCHAR(15), --descripcion de una palabra del estado de la concepcion "terminado","saludable","riesgoso"
	cod_inseminacion INTEGER FOREIGN KEY REFERENCES inseminacion(cod_inseminacion),
	peso_vaca FLOAT

);

--14
CREATE TABLE pajilla(
	id_pajilla INTEGER PRIMARY KEY,
	fecha_embase DATETIME,
	toro INTEGER FOREIGN KEY REFERENCES toro(cod_toro),
	empleado_en INTEGER FOREIGN KEY REFERENCES inseminacion(cod_inseminacion) UNIQUE,
	vendido_en INTEGER FOREIGN KEY REFERENCES registro_venta(factura)

);

--15
CREATE TABLE destete(
	cod_destete INTEGER PRIMARY KEY,
	fecha DATETIME,
	vaca REFERENCES vaca(cod_vaca) UNIQUE,
	toro INTEGER FOREIGN KEY REFERENCES toro(cod_toro) UNIQUE,
	engorde INTEGER FOREIGN KEY REFERENCES engorde(cod_engorde) UNIQUE,
	ternero INTEGER FOREIGN KEY REFERENCES ternero(cod_ternero) UNIQUE

)

--16
CREATE TABLE reg_lechero(
	cod_lec INTEGER PRIMARY KEY,
	pertenece_a INTEGER FOREIGN KEY REFERENCES vaca(cod_vaca),
	inseminacion_asociada INTEGER FOREIGN KEY REFERENCES inseminacion(cod_inseminacion) UNIQUE,
	fecha DATETIME,
	cantidad_lt FLOAT
)

--17
CREATE TABLE engorde (
	cod_engorde INTEGER PRIMARY KEY,
	nombre VARCHAR(20),
	valor_estimado FLOAT,
	categoria VARCHAR(20),
	historial_medico INTEGER FOREIGN KEY REFERENCES  registro_medico(cod_medico) UNIQUE,
	salida INTEGER FOREIGN KEY salida(cod_registro) UNIQUE

);

--18
CREATE TABLE toro (
	cod_toro INTEGER PRIMARY KEY,
	nombre VARCHAR(20),
	rating FLOAT, -- cuantos de las pajillas que fueron usados de el han dado embarazos exitosos
	historial_medico INTEGER FOREIGN KEY REFERENCES  registro_medico(cod_medico) UNIQUE,
	salida INTEGER FOREIGN KEY REFERENCES  salida(cod_registro) UNIQUE

);

--19
CREATE TABLE vaca (
	cod_vaca INTEGER PRIMARY KEY,
	nombre VARCHAR(20),
	genetica_lechera VARCHAR(20),
  inseminaciones INTEGER FOREIGN KEY REFERENCES  inseminacion(cod_inseminacion),
	historial_medico INTEGER FOREIGN KEY REFERENCES  registro_medico(cod_medico) UNIQUE,
	salida INTEGER FOREIGN KEY REFERENCES  salida(cod_registro) UNIQUE

);

--20
CREATE TABLE ternero (
	cod  INTEGER PRIMARY KEY,
	nombre VARCHAR(20),
	sexo  VARCHAR(15),
	fecha_nacimiento DATETIME,
	edad INTEGER,
	peso_nacimiento FLOAT,
	prospecto VARCHAR(20),
	historial_medico INTEGER FOREIGN KEY REFERENCES  registro_medico(cod_medico) UNIQUE,
	salida INTEGER FOREIGN KEY REFERENCES  salida(cod_registro) UNIQUE,
  nacido_de INTEGER FOREIGN KEY REFERENCES  inseminacion(cod_inseminacion)

);
