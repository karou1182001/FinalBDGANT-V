/*Inserción*/
--NOTA: Siempre antes de correr este, deben correr el Script de generación porque o sino aparecerá error de que varios datos ya están

--Nivel 1

--Cliente
INSERT INTO cliente (codigo, nombre, telefono, credito, calificacion) VALUES(0, 'Nadie', '000',  0,  0);
INSERT INTO cliente VALUES(1001, 'Juan Garcia', '3574587543',  1.2,  5);
INSERT INTO cliente  VALUES(1002, 'Santiago Peña', '3574678754',  1.0,  5);
INSERT INTO cliente  VALUES(1003, 'Juana Marquez', '3574678754',  1.2,  4.2);
INSERT INTO cliente  VALUES(1004, 'Sandra Castro', '3574678754',  1.1,  4.6);
INSERT INTO cliente  VALUES(1005, 'Asbel Fernandez', '3574678754',  1.9,  4.9);
INSERT INTO cliente  VALUES(1006, 'Joe Regules', '3574678754',  1.2,  5);
INSERT INTO cliente  VALUES(1007, 'Marc Mattos', '3574678754',  1.5,  3.5);
INSERT INTO cliente  VALUES(1008, 'Jeny Haner', '3574678754',  1.5,  3);

--Enfermedad
INSERT INTO enfermedad (cod_enfermedad, nom_enfermedad, duracion_promedio, indice_letalidad, tratamiento_estandar) VALUES(0, 'Ninguna', 0,  0, 'Ninguno' );
INSERT INTO enfermedad VALUES(301, 'Gripa', 2,  4, 'Cuidados' );
INSERT INTO enfermedad VALUES(302, 'Fiebre', 48,  6, 'Cuidados' );
INSERT INTO enfermedad VALUES(303, 'Nauseas', 1,  2, 'Descanso' );
INSERT INTO enfermedad VALUES(304, 'Dolor', 1,  1, 'Descanso' );
INSERT INTO enfermedad VALUES(305, 'Ceguera', 2,  2, 'Cuidados' );
INSERT INTO enfermedad VALUES(306, 'Lesion', 84,  9, 'Cuidados' );
INSERT INTO enfermedad VALUES(3312, 'Infeccion', 64,  10, 'Cuidados' );

--Vacuna
INSERT INTO vacuna (cod_vacuna, nombre, duracion, descripcion) VALUES (0,  ' Ninguna', 0,  ' Nada' );
INSERT INTO vacuna VALUES (401,  ' Brucelosis', 3,  'A partir de los 3 meses');

--Veterinario
INSERT INTO veterinario(cod_vet,nombre,telefono,correo,empresa,telefono_emergencia) VALUES(0,  'Nadie',  '000',  'correo@nadie.com',  'Ninguna',  ' 000' );
INSERT INTO veterinario  VALUES(501,  'Diego',  '3748763425',  'diego123@hotmail.com',  'Particular',  ' 000' );

--Nivel 2

--Registro médico
--Cada individuo tiene un solo registro médico
INSERT INTO registro_medico(cod_medico,estado,descripcion,fecha,emitido_por) VALUES(0, 'Ninguno', 'Ninguna', '0001-01-01',  0 );
INSERT INTO registro_medico VALUES(1,'Ninguno', 'Ninguna', '0001-01-01',  0 );
INSERT INTO registro_medico VALUES(2,'Ninguno', 'Ninguna', '0001-01-01',  0 );
INSERT INTO registro_medico VALUES(3, 'Ninguno', 'Ninguna', '0001-01-01',  0 );
INSERT INTO registro_medico VALUES(4, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(5, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(6, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(7, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(8, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(9, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(10, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(11, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(12, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(13, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(14, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(15, 'Saludable', 'No presenta patologías', '2020-02-03', 1 );

----Registro venta
INSERT INTO registro_venta(factura,cliente,precio,fecha) VALUES(0, 0, 0, '0001-01-01');
INSERT INTO registro_venta VALUES(601, 12, 1000000, '2021-04-06');
INSERT INTO registro_venta VALUES(602, 16, 1600000, '2021-02-01');
INSERT INTO registro_venta VALUES(603, 15, 1005000, '2021-03-03');
INSERT INTO registro_venta VALUES(604, 12, 2000000, '2021-02-01');
INSERT INTO registro_venta VALUES(605, 10, 160000, '2021-02-02');

--Defunción
INSERT INTO defuncion(reg_defuncion,causa,veterinario_certifica) VALUES(0, 0, 0 );
INSERT INTO defuncion VALUES(500, 100, 200 );

--Nivel 3

--Estuvo_ enfermo
INSERT INTO estuvo_enfermo(reg_enfermo,paciente,duracion_enfermedad,fecha_de_diagnostico,enfermedad) VALUES(0, 0, 0, '0001-01-01',  0 );
INSERT INTO estuvo_enfermo VALUES(1, 2, 500000 , '2021-05-12',  2 );

--Aplicación vacunas
INSERT INTO aplicacion_vacunas(cod_apva,vacuna_aplicada,paciente,fecha) VALUES(0, 0, 0, '0001-01-01');
INSERT INTO aplicacion_vacunas VALUES(1, 5, 0, '2021-02-08');
INSERT INTO aplicacion_vacunas VALUES(2, 6, 0, '0001-01-08');

--Registro alimentación
INSERT INTO reg_alimentacion(cod_alimentacion	, proviene_de , peso_kg, liquido_lt, fecha) VALUES(0, 0, 0, 0,  '0001-01-01');


--Salida
INSERT INTO salida(cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES(0,  'No ha salido',  '0001-01-01', 0, 0);
INSERT INTO salida VALUES(901,  'No ha salido',  '2021-05-11', 0, 0);
INSERT INTO salida VALUES(902,  'No ha salido',  '2021-06-01', 0, 0);
INSERT INTO salida VALUES(903,  'No ha salido',  '2021-01-01', 0, 0);
INSERT INTO salida VALUES(904,  'No ha salido',  '2021-11-01', 0, 0);

--Nivel 4

--Vaca
--Recuerde que por cada individuo a insertar, debe crear un registro médico (Relación uno a uno)
INSERT INTO vaca(cod_vaca,nombre,genetica_lechera,historial_medico,salida) VALUES(0, 'Nadie', 'Nada', 0, 0 );
INSERT INTO vaca VALUES(1, 'Teresa', 'Sobresaliente', 4, 0 );
INSERT INTO vaca VALUES(2, 'Virginia', 'Sobresaliente', 5, 0 );
INSERT INTO vaca VALUES(3, 'Anastacia', 'Sobresaliente', 6, 0 );
INSERT INTO vaca VALUES(4, 'Petra', 'Normal', 7, 0 );

--Toro
--Recuerde que por cada individuo a insertar, debe crear un registro médico (Relación uno a uno)
INSERT INTO toro(cod_toro,nombre,rating,historial_medico,salida) VALUES(0, 'Nadie', 0, 1, 0 );
INSERT INTO toro VALUES(1, 'Pepe', 5, 8, 0 );
INSERT INTO toro VALUES(2, 'Thomy', 4, 9, 0 );
INSERT INTO toro VALUES(3, 'Dylano', 2, 10, 0 );
INSERT INTO toro VALUES(4, 'Sancho', 5, 11, 0 );

--Engorde
--Recuerde que por cada individuo a insertar, debe crear un registro médico (Relación uno a uno)
INSERT INTO engorde(cod_engorde,nombre,valor_estimado,categoria,historial_medico,salida) VALUES(0, 'Juancho', 100.0, 'cat 1', 2, 0 );
INSERT INTO engorde VALUES(1, 'Nino', 200, 'cat 1' , 12, 0 );
INSERT INTO engorde VALUES(2, 'Joty', 300, 'cat 1', 13, 0 );
INSERT INTO engorde VALUES(3, 'Pin', 300, 'cat 1', 14, 0 );

--Nivel 5

--Inseminación
INSERT INTO inseminacion(cod_inseminacion,fecha,exito,veterinario,vaca) VALUES(0, '0001-01-01', 'no', 0, 0 );
INSERT INTO inseminacion  VALUES(1, '2020-02-03', 'si', 1, 1 );
INSERT INTO inseminacion  VALUES(2, '2020-02-03', 'no', 1, 2 );
INSERT INTO inseminacion  VALUES(3, '2020-02-03', 'si', 1, 3 );
INSERT INTO inseminacion  VALUES(4, '2020-02-03', 'si', 1, 4 );

--Nivel 6

--Ternero
--Recuerde que por cada individuo a insertar, debe crear un registro médico (Relación uno a uno)
INSERT INTO ternero(cod_ternero,nombre,sexo,fecha_nacimiento,edad,peso_nacimiento,prospecto,historial_medico,salida,nacido_de) VALUES(0, 'Nadie', 'Ninguno',  '0001-01-01', 0, 0,  'Nada', 3, 0, 0);
INSERT INTO ternero VALUES(1, 'Lily', 'F',  '2021-02-01', 0, 4,  'Nada', 15, 0, 1);
INSERT INTO ternero VALUES(2, 'Jeny', 'F',  '2021-01-11', 0, 5,  'Nada', 5, 0, 1);
INSERT INTO ternero VALUES(3, 'Jony', 'M',  '2020-12-12', 0, 8,  'Nada', 4, 0, 1);

--Pajilla
INSERT INTO pajilla(id_pajilla,fecha_embase,toro,empleado_en,vendido_en)  VALUES(0, '0001-01-01', 0, 0, 0);
INSERT INTO pajilla  VALUES(1, '2021-01-01', 1, 1, 0);
INSERT INTO pajilla  VALUES(2, '2021-02-01', 1, 2, 0);
INSERT INTO pajilla  VALUES(3, '2021-03-01', 2, 3, 0);
INSERT INTO pajilla  VALUES(4, '2021-04-01', 3, 4, 0);
INSERT INTO pajilla  VALUES(5, '2021-05-01', 4, 0, 0);


--Estado inseminación
INSERT INTO estado_inseminacion(cod_registro,mes,fecha,estado,cod_inseminacion,peso_vaca) VALUES(0, 0, '0001-01-01', 'nada', 0, 0 );
INSERT INTO estado_inseminacion VALUES(1, 3, '2021-01-01', 'embarazo', 1, 300 );
INSERT INTO estado_inseminacion VALUES(2, 2, '2021-01-01', 'iniciando', 2, 500 );
INSERT INTO estado_inseminacion VALUES(3, 2, '2021-01-01', 'embarazo', 3, 400 );
INSERT INTO estado_inseminacion VALUES(4, 5, '2021-01-01', 'finalizada', 4, 200 );

--Nivel 7

--Destetee
INSERT INTO destete(cod_destete,fecha,vaca,toro,engorde,ternero) VALUES(0, '0001-01-01', 0, 0, 0, 0 );
INSERT INTO destete VALUES(50, '2021-05-11', 1, 2, 500, 2 );


--Reg lechero
INSERT INTO reg_lechero(cod_lec,pertenece_a,inseminacion_asociada,fecha,cantidad_lt) VALUES(0, 0, 0, '0001-01-01', 0 );
INSERT INTO reg_lechero VALUES(1, 0, 0, '2020-02-02', 200 );
