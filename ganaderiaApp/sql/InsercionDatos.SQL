/*Inserción*/

--Nivel 1

--Cliente
INSERT INTO cliente (codigo, nombre, telefono, credito, calificacion) VALUES(0, 'Nadie', '000',  0,  0);
INSERT INTO cliente (codigo, nombre, telefono, credito, calificacion) VALUES(1, 'Juan Garcia', '3574587543',  1.2,  5);
INSERT INTO cliente  VALUES(2, 'Santiago Peña', '3574678754',  1.5,  5);

--Enfermedad
INSERT INTO enfermedad (cod_enfermedad, nom_enfermedad, duracion_promedio, indice_letalidad, tratamiento_estandar) VALUES(0, 'Ninguna', 0,  0, 'Ninguno' );
INSERT INTO enfermedad VALUES(1, 'Gripa', 1,  4, 'Cuidados' );

--Vacuna
INSERT INTO vacuna (cod_vacuna, nombre, duracion, descripcion) VALUES (0,  ' Ninguna', 0,  ' Nada' );
INSERT INTO vacuna VALUES (1,  ' Brucelosis', 3,  'A partir de los 3 meses');

--Veterinario
INSERT INTO veterinario(cod_vet,nombre,telefono,correo,empresa,telefono_emergencia) VALUES(0,  'Nadie',  '000',  'correo@nadie.com',  'Ninguna',  ' 000' );
INSERT INTO veterinario  VALUES(1,  'Diego',  '3748763425',  'diego123@hotmail.com',  'Particular',  ' 000' );

--Nivel 2

--Registro médico
INSERT INTO registro_medico(cod_medico,estado,descripcion,fecha,emitido_por) VALUES(0, 'Ninguno', 'Ninguna', '0001-01-01',  0 );
INSERT INTO registro_medico VALUES(1, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );

----Registro venta
INSERT INTO registro_venta(factura,cliente,precio,fecha) VALUES(0, 0, 0, '0001-01-01');
INSERT INTO registro_venta(factura,cliente,precio,fecha) VALUES(1, 2, 1000000, '2021-02-01');

--Defunción
INSERT INTO defuncion(reg_defuncion,causa,veterinario_certifica) VALUES(0, 0, 0 );

--Nivel 3

--Estuvo_ enfermo
INSERT INTO estuvo_enfermo(reg_enfermo,paciente,duracion_enfermedad,fecha_de_diagnostico,enfermedad) VALUES(0, 0, 0, '0001-01-01',  0 );

--Aplicación vacunas
INSERT INTO aplicacion_vacunas(cod_apva,vacuna_aplicada,paciente,fecha) VALUES(0, 0, 0, '0001-01-01');

--Registro alimentación
INSERT INTO reg_alimentacion(cod_alimentacion	, proviene_de , peso_kg, liquido_lt, fecha) VALUES(0, 0, 0, 0,  '0001-01-01');


--Salida
INSERT INTO salida(cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES(0,  'No ha salido',  '0001-01-01', 0, 0);

--Nivel 4

--Vaca
INSERT INTO vaca(cod_vaca,nombre,genetica_lechera,historial_medico,salida) VALUES(0, 'Nadie', 'Nada', 0, 0 );
INSERT INTO vaca VALUES(1, 'Teresa', 'Sobresaliente', 1, 0 );

--Toro
INSERT INTO toro(cod_toro,nombre,rating,historial_medico,salida) VALUES(0, 'Nadie', 0, 0, 0 );
INSERT INTO toro VALUES(1, 'Pepe', 5, 1, 0 );

--Engorde
INSERT INTO engorde(cod_engorde,nombre,valor_estimado,categoria,historial_medico,salida) VALUES(0, 'Juancho', 100.0, 'cat 1', 1, 0 );

--Nivel 5

--Inseminación
INSERT INTO inseminacion(cod_inseminacion,fecha,exito,veterinario,vaca) VALUES(0, '0001-01-01', 0, 0, 0 );
INSERT INTO inseminacion  VALUES(1, '2020-02-03', 'si', 1, 1 );

--Nivel 6

--Ternero
INSERT INTO ternero(cod_ternero,nombre,sexo,fecha_nacimiento,edad,peso_nacimiento,prospecto,historial_medico,salida,nacido_de) VALUES(0, 'Nadie', 'Ninguno',  '0001-01-01', 0, 0,  'Nada', 0, 0, 0);
INSERT INTO ternero VALUES(1, 'Lily', 'F',  '2021-02-01', 0, 4,  'Nada', 1, 0, 1);

--Pajilla
INSERT INTO pajilla(id_pajilla,fecha_embase,toro,empleado_en,vendido_en)  VALUES(0, '0001-01-01', 0, 0, 0);
INSERT INTO pajilla(id_pajilla,fecha_embase,toro,empleado_en,vendido_en)  VALUES(1, '2021-01-01', 1, 1, 1);

--Estado inseminación
INSERT INTO estado_inseminacion(cod_registro,mes,fecha,estado,cod_inseminacion,peso_vaca) VALUES(0, 0, '0001-01-01', 'nada', 0, 0 );
INSERT INTO estado_inseminacion VALUES(1, 2, '2021-01-01', 'proceso', 1, 300 );

--Nivel 7

--Destetee
INSERT INTO destete(cod_destete,fecha,vaca,toro,engorde,ternero) VALUES(0, '0001-01-01', 0, 0, 0, 0 );

--Reg lechero
INSERT INTO reg_lechero(cod_lec,pertenece_a,inseminacion_asociada,fecha,cantidad_lt) VALUES(0, 0, 0, '0001-01-01', 0 );