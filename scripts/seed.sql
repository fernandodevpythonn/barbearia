-- seed sendo gerado
  INSERT INTO usuario (idusuario,nome,email,senha,perfil) VALUES
  (1,'fernando','fernandoribeiro270806@gmaiil.com','$2b$12$NoFU1qdDH8X.EB6AbSTDRO4Pz/qrntskyKvk5HUTDDM3S05xRIgSm','administrador'),
  (2,'barbeiro','barbeiro@gmail.com','$2b$12$dr4VrhMT19TGYMFvNSqP5Ouz2ONEGlwnAMIuHpUngjLFgOao6B/92','barbeiro'),
  (3,'cliente','cliente@gmail.com','$2b$12$iJxHMS1.RlREh8f1iS7cbu4m9u2yw.s1dEoqFOP2bUjbFJw3yEUWu','cliente');
  
  INSERT INTO barbeiro (idbarbeiro,nome,usuario_idusuario) VALUES
  (1,'rogerio',2),
  (2,'vitor',2);
  
  INSERT INTO cortes (idcortes,corte,valor) VALUES
  (1,'tesoura + barba',30),
  (2,'maquina + barba',35),
  (3,'maquina + tesoura + barba',45),
  (4,'barba',20),
  (5,'maquina',25),
  (6,'tesoura',20),
  (7,'maquina + tesoura',30);
  
  INSERT INTO cliente 
  (idcliente,nome,usuario_idusuario)
  VALUES
  (
    1,
    'Sr. Theo Vasconcelos',
    3                     
    ),
(
    2,
    'Anthony Marques',
    3                     
    ),
(
    3,
    'Thiago Pacheco',
    3                     
    ),
(
    4,
    'Pedro Lucas Andrade',
    3                     
    ),
(
    5,
    'Heitor Nogueira',
    3                     
    ),
(
    6,
    'José Pedro Rios',
    3                     
    ),
(
    7,
    'Thales Cavalcante',
    3                     
    ),
(
    8,
    'Vinícius Jesus',
    3                     
    ),
(
    9,
    'Mathias Machado',
    3                     
    );

  INSERT INTO agenda (idagenda,data_hora,barbeiro_idbarbeiro,cliente_idcliente)
  VALUES
  (
    1,
    '2001-04-12 22:22:08',
    2,
    1                    
    ),
(
    2,
    '1970-05-23 16:06:25',
    2,
    2                    
    ),
(
    3,
    '1973-09-10 23:59:46',
    2,
    3                    
    ),
(
    4,
    '2007-12-24 06:27:21',
    2,
    4                    
    ),
(
    5,
    '2010-06-26 04:18:23',
    2,
    5                    
    ),
(
    6,
    '2011-08-04 08:10:43',
    1,
    6                    
    ),
(
    7,
    '1998-02-02 23:26:36',
    2,
    7                    
    ),
(
    8,
    '1980-11-29 20:01:06',
    1,
    8                    
    ),
(
    9,
    '1986-04-17 16:18:26',
    2,
    9                    
    );

  INSERT INTO log (idlog,usuario_idusuario,datahora)
  VALUES
  (
    1,
    2,
    '1976-10-03 10:43:42'
    ),
(
    2,
    1,
    '1997-11-28 13:16:05'
    ),
(
    3,
    2,
    '1984-03-16 01:51:17'
    ),
(
    4,
    2,
    '2023-09-27 20:51:29'
    ),
(
    5,
    1,
    '2000-09-28 03:50:58'
    ),
(
    6,
    3,
    '2007-06-15 21:35:46'
    ),
(
    7,
    2,
    '1997-07-23 20:20:14'
    ),
(
    8,
    2,
    '2021-10-16 10:46:39'
    ),
(
    9,
    1,
    '2000-07-27 22:38:23'
    );
