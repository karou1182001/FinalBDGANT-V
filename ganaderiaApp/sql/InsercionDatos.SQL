/*Inserción*/
--NOTA: Siempre antes de correr este, deben correr el Script de generación porque o sino aparecerá error de que varios datos ya están

--Nivel 1

--Cliente
INSERT INTO cliente (codigo, nombre, telefono, credito, calificacion) VALUES(0, 'Nadie', '000',  0,  0);
INSERT INTO cliente (codigo, nombre, telefono, credito, calificacion) VALUES(1, 'Juan Garcia', '3574587543',  1.2,  5);
INSERT INTO cliente  VALUES(2, 'Santiago Pena', '3574678754',  1.5,  5);
INSERT INTO cliente  VALUES(3, 'Juana Marquez', '3105698159',  1.2,  4.2);
INSERT INTO cliente  VALUES(4, 'Sandra Castro', '3028569874',  1.1,  4.6);
INSERT INTO cliente  VALUES(5, 'Asbel Fernandez', '3204678754',  1.9,  4.9);
INSERT INTO cliente  VALUES(6, 'Joe Regules', '3004678754',  1.2,  5);
INSERT INTO cliente  VALUES(7, 'Marc Mattos', '3982156432',  1.5,  3.5);
INSERT INTO cliente  VALUES(8, 'Jeny Haner', '3001000650',  1.5,  3);
INSERT INTO cliente  VALUES(9, 'Juan Miguel', '3968452020',  0.9,  3.5);
INSERT INTO cliente  VALUES(10, 'Carlos Zuniga', '3458955555',  2,  3);
INSERT INTO cliente  VALUES(11, 'Aliz Contreras', '3559806545',  1.5,  3.5);
INSERT INTO cliente  VALUES(12, 'Mikaela Camargo', '3000003215',  1.9,  3.4);
INSERT INTO cliente  VALUES(13, 'Jonatan Mandonaldo', '3114568978',  1.4,  3.5);
INSERT INTO cliente  VALUES(14, 'Mulan Galindo', '3986123456',  1.3,  4.3);
INSERT INTO cliente  VALUES(15, 'Khalil Mazuelos', '3111234567',  2.2,  3.5);
INSERT INTO cliente  VALUES(16, 'Nera Walden', '3458956545',  2,  4.3);
INSERT INTO cliente  VALUES(17, 'Lana Ronel', '3789855285',  2.1,  3.2)
INSERT INTO cliente  VALUES(18, 'Sol Vadini', '3777777777',  1.1,  3.9);
INSERT INTO cliente  VALUES(19, 'Daniel Perez', '3127806585',  1.2,  4.9);
INSERT INTO cliente  VALUES(20, 'Rugal Rodrez', '3568527535',  1.5,  3.1);

--Enfermedad
INSERT INTO enfermedad (cod_enfermedad, nom_enfermedad, duracion_promedio, indice_letalidad, tratamiento_estandar) VALUES(0, 'Ninguna', 0,  0, 'Ninguno' );
INSERT INTO enfermedad VALUES(1, 'Gripa', 1,  4, 'Cuidados' );
INSERT INTO enfermedad VALUES(2, 'Fiebre', 48,  6, 'Cuidados' );
INSERT INTO enfermedad VALUES(3, 'Nauseas', 1,  2, 'Descanso' );
INSERT INTO enfermedad VALUES(4, 'Dolor', 1,  1, 'Descanso' );
INSERT INTO enfermedad VALUES(5, 'Ceguera', 2,  2, 'Cuidados' );
INSERT INTO enfermedad VALUES(6, 'Lesion', 84,  9, 'Cuidados' );
INSERT INTO enfermedad VALUES(7, 'Infeccion', 64,  10, 'Cuidados' );
INSERT INTO enfermedad VALUES(8, 'Tuberculosis', 84,  12, 'Cuidados' );
INSERT INTO enfermedad VALUES(9, 'Clostridiosis', 36,  9, 'Cuidados' );
INSERT INTO enfermedad VALUES(10, 'Problema de pezuñas', 24,  1, 'Cuidados' );
INSERT INTO enfermedad VALUES(11, 'Mastitis', 56,  9, 'Cuidados' );
INSERT INTO enfermedad VALUES(12, 'Parasitos', 84,  9, 'Cuidados' );
INSERT INTO enfermedad VALUES(13, 'Leptospirosis', 56,  10, 'Cuidados' );
INSERT INTO enfermedad VALUES(14, 'Babesiosis', 34,  5, 'Cuidados' );

--Vacuna
INSERT INTO vacuna (cod_vacuna, nombre, duracion, descripcion) VALUES (0,  ' Ninguna', 0,  ' Nada' );
INSERT INTO vacuna VALUES (1,  ' Antibrucelosis', 3,  'A partir de los 3 meses');
INSERT INTO vacuna VALUES (2,  ' Antianilosis', 24,  'Tratamiennto cada dia');
INSERT INTO vacuna VALUES (3,  ' Heparina', 5,  'Cada 5 horas');
INSERT INTO vacuna VALUES (4,  ' Dextrosina', 8,  'Tomar cada 8 horas');
INSERT INTO vacuna VALUES (5,  ' Lipido emulsivo', 12,  'Dos veces cada dia');
INSERT INTO vacuna VALUES (6,  ' Clindamicina', 48,  'A partir de cada dos dias');

--Veterinario
INSERT INTO veterinario(cod_vet,nombre,telefono,correo,empresa,telefono_emergencia) VALUES(0,  'Nadie',  '000',  'correo@nadie.com',  'Ninguna',  '000' );
INSERT INTO veterinario  VALUES(1,  'Diego',  '3748763425',  'diego123@hotmail.com',  'Particular',  '000' );
INSERT INTO veterinario  VALUES(2,  'Nath',  '3565426985',  'nathlch@hotmail.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(3,  'Miguel',  '3748763425',  'miguel@gmail.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(4,  'Juan',  '3222226545',  'juandi@hotmail.com',  'VeterinariaSA',  '3748763425' );
INSERT INTO veterinario  VALUES(5,  'Dwigth',  '3232357892',  'dw123@hotmail.com',  'VeterinariaSA',  '000' );
INSERT INTO veterinario  VALUES(6,  'Nicolas',  '3468952581',  'nicolasr@hotmail.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(7,  'Evelin',  '3995202598',  'evee01@hotmail.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(8,  'Charles',  '3995200598',  'charlie23@hotmail.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(9,  'Eva',  '3995120598',  'eva05@outlook.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(10,  'Jean',  '3995202565',  'jeanb@hotmail.com',  'AnimanSA',  '3748763425' );
INSERT INTO veterinario  VALUES(11,  'Nicole',  '3995202756',  'nicol@hotmail.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(12,  'Alexander',  '3995202123',  'alexc54@hotmail.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(13,  'Beigin',  '3115602598',  'byin45hotmail.com',  'AnimanSA',  '3748763425' );
INSERT INTO veterinario  VALUES(14,  'Camilo',  '3032202598',  'camiloe@hotmail.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(15,  'Josela',  '3123202598',  'jhanner@hotmail.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(16,  'Valery',  '3000202598',  'valerym@gmail.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(17,  'Paula',  '3997823312',  'paulab@hotmail.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(18,  'Luna',  '3123123312',  'luna45@hotmail.com',  'VeterinariaSA',  '3748763425' );
INSERT INTO veterinario  VALUES(19,  'Jupiter',  '3004505859',  'jupiter45@yahoo.com',  'Particular',  '3748763425' );
INSERT INTO veterinario  VALUES(20,  'Claudio',  '3110006565',  'claudiop@hotmail.com',  'Particular',  '3748763425' );

--Nivel 2

--Registro médico
--Cada individuo tiene un solo registro médico
INSERT INTO registro_medico(cod_medico,estado,descripcion,fecha,emitido_por) VALUES(0, 'Ninguno', 'Ninguna', '0001-01-01',  0 );
INSERT INTO registro_medico VALUES(1,'Ninguno', 'Ninguna', '0001-01-01',  0 );
INSERT INTO registro_medico VALUES(2,'Ninguno', 'Ninguna', '0001-01-01',  0 );
INSERT INTO registro_medico VALUES(3, 'Ninguno', 'Ninguna', '0001-01-01',  0 );
INSERT INTO registro_medico VALUES(4, 'Saludable', 'No presenta patologias', '2020-02-03', 1 );
INSERT INTO registro_medico VALUES(5, 'Saludable', 'No presenta patologias', '2020-02-03', 2 );
INSERT INTO registro_medico VALUES(6, 'Saludable', 'No presenta patologias', '2020-02-03', 3 );
INSERT INTO registro_medico VALUES(7, 'Saludable', 'No presenta patologias', '2020-02-03', 4 );
INSERT INTO registro_medico VALUES(8, 'Enfermo', 'Presenta cansansio', '2020-02-03', 5 );
INSERT INTO registro_medico VALUES(9, 'Enfermo', 'Presencia Mareos', '2020-02-03', 6 );
INSERT INTO registro_medico VALUES(10, 'Saludable', 'No presenta patologias', '2020-02-03',7 );
INSERT INTO registro_medico VALUES(11, 'Saludable', 'No presenta patologias', '2020-05-03', 8 );
INSERT INTO registro_medico VALUES(12, 'Saludable', 'No presenta patologias', '2020-06-03', 18 );
INSERT INTO registro_medico VALUES(13, 'Saludable', 'No presenta patologias', '2020-07-03', 9 );
INSERT INTO registro_medico VALUES(14, 'Saludable', 'No presenta patologias', '2020-08-03', 9 );
INSERT INTO registro_medico VALUES(15, 'Saludable', 'No presenta patologias', '2020-09-03', 10 );
INSERT INTO registro_medico VALUES(16, 'Saludable', 'No presenta patologias', '2020-10-03', 20 );
INSERT INTO registro_medico VALUES(17, 'Saludable', 'No presenta patologias', '2020-11-03', 10 );
INSERT INTO registro_medico VALUES(18, 'Enfermo', 'Presenta goteo de nariz y calentura', '2020-12-03', 11 );
INSERT INTO registro_medico VALUES(19, 'Saludable', 'No presenta patologias', '2020-13-03', 19 );
INSERT INTO registro_medico VALUES(20, 'Enfermo', 'Presenta sangrado al toser', '2020-14-03', 11 );
INSERT INTO registro_medico VALUES(21, 'Saludable', 'No presenta patologias', '2020-15-03', 11 );
INSERT INTO registro_medico VALUES(22, 'Saludable', 'No presenta patologias', '2020-16-03', 12 );
INSERT INTO registro_medico VALUES(23, 'Saludable', 'No presenta patologias', '2020-17-03', 12 );
INSERT INTO registro_medico VALUES(24, 'Saludable', 'No presenta patologias', '2020-18-03', 12 );
INSERT INTO registro_medico VALUES(25, 'Saludable', 'No presenta patologias', '2020-18-03', 9 );
INSERT INTO registro_medico VALUES(26, 'Saludable', 'No presenta patologias', '2020-18-03', 10 );
INSERT INTO registro_medico VALUES(27, 'Enfermo', 'Presenta vomitos', '2020-19-03', 20 );
INSERT INTO registro_medico VALUES(28, 'Saludable', 'No presenta patologias', '2020-20-03', 10 );
INSERT INTO registro_medico VALUES(29, 'Enfermo', 'Presenta goteo de nariz y calentura', '2020-21-03', 11 );
INSERT INTO registro_medico VALUES(30, 'Saludable', 'No presenta patologias', '2020-22-03', 19 );
INSERT INTO registro_medico VALUES(31, 'Enfermo', 'Presenta sangrado al toser', '2020-23-03', 11 );
INSERT INTO registro_medico VALUES(32, 'Saludable', 'No presenta patologias', '2020-24-03', 11 );
INSERT INTO registro_medico VALUES(33, 'Saludable', 'No presenta patologias', '2020-24-03', 18 );
INSERT INTO registro_medico VALUES(34, 'Saludable', 'No presenta patologias', '2020-26-03', 15 );
INSERT INTO registro_medico VALUES(35, 'Saludable', 'No presenta patologias', '2020-26-03', 20 );
INSERT INTO registro_medico VALUES(36, 'Saludable', 'No presenta patologias', '2020-26-03', 15 );
INSERT INTO registro_medico VALUES(37, 'Saludable', 'No presenta patologias', '2020-26-03', 20 );
INSERT INTO registro_medico VALUES(38, 'Saludable', 'No presenta patologias', '2020-26-03', 20 );
INSERT INTO registro_medico VALUES(39, 'Saludable', 'No presenta patologias', '2020-26-03', 18 );
INSERT INTO registro_medico VALUES(40, 'Saludable', 'No presenta patologias', '2020-26-03', 20 );

----Registro venta
INSERT INTO registro_venta(factura,cliente,precio,fecha) VALUES(0, 0, 0, '0001-01-01');
INSERT INTO registro_venta(factura,cliente,precio,fecha) VALUES(1, 2, 1000000, '2021-02-01');
INSERT INTO registro_venta VALUES(2, 5, 1000000, '2021-02-01');
INSERT INTO registro_venta VALUES(3, 6, 1600000, '2021-02-01');
INSERT INTO registro_venta VALUES(4, 7, 1005000, '2021-13-01');
INSERT INTO registro_venta VALUES(5, 8, 2000000, '2021-16-01');
INSERT INTO registro_venta VALUES(6, 4, 760000, '2021-01-02');
INSERT INTO registro_venta VALUES(7, 4, 460000, '2021-02-02');
INSERT INTO registro_venta VALUES(8, 9, 160000, '2021-03-02');
INSERT INTO registro_venta VALUES(9, 11, 180000, '2021-06-02');
INSERT INTO registro_venta VALUES(10, 12, 450000, '2021-08-02');
INSERT INTO registro_venta VALUES(11, 13, 120000, '2021-09-02');
INSERT INTO registro_venta VALUES(12, 11, 450000, '2021-10-02');


--Defunción
INSERT INTO defuncion(reg_defuncion,causa,veterinario_certifica) VALUES(0, 0, 0 );
INSERT INTO defuncion VALUES(1, 2, 3 );
INSERT INTO defuncion VALUES(2, 3, 5 );
INSERT INTO defuncion VALUES(3, 4, 5 );


--Nivel 3

--Estuvo_ enfermo
INSERT INTO estuvo_enfermo(reg_enfermo,paciente,duracion_enfermedad,fecha_de_diagnostico,enfermedad) VALUES(0, 0, 0, '0001-01-01',  0 );
INSERT INTO estuvo_enfermo VALUES(1, 5, 500000 , '2020-01-12',  2 );
INSERT INTO estuvo_enfermo VALUES(2, 6, 500000 , '2020-06-12',  5 );
INSERT INTO estuvo_enfermo VALUES(3, 7, 500000 , '2020-20-12',  3 );

--Aplicación vacunas
INSERT INTO aplicacion_vacunas(cod_apva,vacuna_aplicada,paciente,fecha) VALUES(0, 0, 0, '0001-01-01');
INSERT INTO aplicacion_vacunas VALUES(1, 5, 6, '2020-02-11');
INSERT INTO aplicacion_vacunas VALUES(2, 6, 5, '2020-01-11');
INSERT INTO aplicacion_vacunas VALUES(3, 4, 7, '2020-26-11');

--Registro alimentación
INSERT INTO reg_alimentacion(cod_alimentacion	, proviene_de , peso_kg, liquido_lt, fecha) VALUES(0, 0, 0, 0,  '0001-01-01');
INSERT INTO reg_alimentacion VALUES(1, 1, 100, 50,  '2020-01-01');
INSERT INTO reg_alimentacion VALUES(2, 2, 150, 50,  '2021-02-01');
INSERT INTO reg_alimentacion VALUES(3, 3, 100, 50,  '2021-03-01');
INSERT INTO reg_alimentacion VALUES(4, 4, 120, 50,  '2021-04-01');
INSERT INTO reg_alimentacion VALUES(5, 5, 120, 50,  '2021-05-01');
INSERT INTO reg_alimentacion VALUES(6, 6, 150, 50,  '2021-06-01');
INSERT INTO reg_alimentacion VALUES(7, 7, 100, 50,  '2021-08-01');
INSERT INTO reg_alimentacion VALUES(8, 8, 100, 50,  '2021-09-01');
INSERT INTO reg_alimentacion VALUES(9, 9, 150, 50,  '2021-11-01');
INSERT INTO reg_alimentacion VALUES(10, 10, 120, 50,  '2021-11-01');
INSERT INTO reg_alimentacion VALUES(11, 11, 120, 50,  '2021-11-01');
INSERT INTO reg_alimentacion VALUES(12, 12, 110, 50,  '2021-12-01');
INSERT INTO reg_alimentacion VALUES(13, 13, 90, 50,  '2021-13-01');
INSERT INTO reg_alimentacion VALUES(14, 14, 100, 50,  '2021-16-01');
INSERT INTO reg_alimentacion VALUES(15, 15, 110, 50,  '2021-17-01');
INSERT INTO reg_alimentacion VALUES(16, 16, 150, 50,  '2021-19-01');
INSERT INTO reg_alimentacion VALUES(17, 17, 110, 50,  '2021-20-01');


--Salida
INSERT INTO salida(cod_registro, razon, fecha, venta, sacrificio_enfermedad) VALUES(0,  'No ha salido',  '0001-01-01', 0, 0);
INSERT INTO salida VALUES(1,  'Llego su hora',  '2021-05-11', 0, 2);

--Nivel 4

--Vaca
--Recuerde que por cada individuo a insertar, debe crear un registro médico (Relación uno a uno)
INSERT INTO vaca(cod_vaca,nombre,genetica_lechera,historial_medico,salida) VALUES(0, 'Nadie', 'Nada', 0, 0 );
INSERT INTO vaca VALUES(1, 'Teresa', 'Sobresaliente', 4, 0 );
INSERT INTO vaca VALUES(2, 'Virginia', 'Sobresaliente', 5, 0 );
INSERT INTO vaca VALUES(3, 'Anastacia', 'Sobresaliente', 6, 0 );
INSERT INTO vaca VALUES(4, 'Artillera', 'Normal', 7, 0 );
INSERT INTO vaca VALUES(5, 'Gallarda', 'Sobresaliente', 8, 0 );
INSERT INTO vaca VALUES(6, 'Patricia', 'Normal', 10, 0 );
INSERT INTO vaca VALUES(7, 'Duquesa', 'Normal', 12, 0 );
INSERT INTO vaca VALUES(8, 'Majita', 'Normal', 14, 0 );
INSERT INTO vaca VALUES(9, 'Noble', 'Normal', 16, 0 );
INSERT INTO vaca VALUES(10, 'Paloma', 'Regular', 18, 0 );
INSERT INTO vaca VALUES(11, 'Petina', 'Regular', 31, 0 );
INSERT INTO vaca VALUES(12, 'Pezuña', 'Regular', 33, 0 );



--Toro
--Recuerde que por cada individuo a insertar, debe crear un registro médico (Relación uno a uno)
INSERT INTO toro(cod_toro,nombre,rating,historial_medico,salida) VALUES(0, 'Nadie', 0, 1, 0 );
INSERT INTO toro VALUES(1, 'Pepe', 5, 9, 0 );
INSERT INTO toro VALUES(2, 'Thomy', 4, 11, 0 );
INSERT INTO toro VALUES(3, 'Dylano', 2, 13, 0 );
INSERT INTO toro VALUES(4, 'Sancho', 5, 15, 0 );
INSERT INTO toro VALUES(5, 'Tango', 5, 17, 0 );
INSERT INTO toro VALUES(6, 'Tombo', 4, 19, 0 );
INSERT INTO toro VALUES(7, 'Manolo', 2, 20, 0 );
INSERT INTO toro VALUES(8, 'Amoroso', 4, 21, 0 );
INSERT INTO toro VALUES(9, 'Litch', 4, 22, 0 );
INSERT INTO toro VALUES(10, 'Kazui', 5, 23, 0 );
INSERT INTO toro VALUES(11, 'Cantaro', 4, 24, 0 );
INSERT INTO toro VALUES(12, 'Zuvero', 5, 25, 0 );


--Engorde
--Recuerde que por cada individuo a insertar, debe crear un registro médico (Relación uno a uno)
INSERT INTO engorde(cod_engorde,nombre,valor_estimado,categoria,historial_medico,salida) VALUES(0, 'Juancho', 100.0, 'cat 1', 2, 0 );
INSERT INTO engorde VALUES(1, 'Nino', 200, 'cat 1' , 38, 0 );
INSERT INTO engorde VALUES(2, 'Joty', 300, 'cat 1', 39, 0 );
INSERT INTO engorde VALUES(3, 'Pin', 300, 'cat 1', 40, 0 );

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
INSERT INTO ternero VALUES(1, 'Lily', 'F',  '2021-02-04', 0, 4,  'Nada', 26, 0, 1);
INSERT INTO ternero VALUES(1, 'Leny', 'F',  '2021-02-04', 0, 4,  'Nada', 27, 0, 1);
INSERT INTO ternero VALUES(1, 'Auri', 'F',  '2021-02-05', 0, 4,  'Nada', 28, 0, 2);
INSERT INTO ternero VALUES(1, 'Calos', 'M',  '2021-02-05', 0, 4,  'Nada', 29, 0, 3);
INSERT INTO ternero VALUES(1, 'Milk', 'F',  '2021-02-06', 0, 4,  'Nada', 30, 0, 4);
INSERT INTO ternero VALUES(1, 'Peti', 'F',  '2021-05-06', 0, 4,  'Nada', 32, 0, 6);
INSERT INTO ternero VALUES(1, 'Cams', 'M',  '2021-08-06', 0, 4,  'Nada', 34, 0, 7);
INSERT INTO ternero VALUES(2, 'Jeny', 'F',  '2021-01-07', 1, 5,  'Nada', 35, 0, 8);
INSERT INTO ternero VALUES(3, 'Jony', 'M',  '2020-12-07', 2, 8,  'Nada', 36, 0, 9);
INSERT INTO ternero VALUES(3, 'Pili', 'M',  '2020-16-08', 2, 8,  'Nada', 37, 0, 11);


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

--Reg lechero
INSERT INTO reg_lechero(cod_lec,pertenece_a,inseminacion_asociada,fecha,cantidad_lt) VALUES(0, 0, 0, '0001-01-01', 0 );
INSERT INTO reg_lechero VALUES(1, 1, 2, '2020-02-02', 200 );