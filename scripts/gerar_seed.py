from faker import Faker
import random
import bcrypt

fake = Faker('pt_BR')

def gerar_hash(senha:str):
  return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def gerar_sql(qtd_clientes:int):
  sql = "-- seed sendo gerado"
  sql += f"""
  INSERT INTO usuario (idusuario,nome,email,senha,perfil) VALUES
  (1,'fernando','fernandoribeiro270806@gmaiil.com','{gerar_hash('92539788')}','administrador'),
  (2,'barbeiro','barbeiro@gmail.com','{gerar_hash('12345')}','barbeiro'),
  (3,'cliente','cliente@gmail.com','{gerar_hash('23456')}','cliente');
  """

  sql += """
  INSERT INTO barbeiro (idbarbeiro,nome,usuario_idusuario) VALUES
  (1,'rogerio',2),
  (2,'vitor',2);
  """
  sql += f"""
  INSERT INTO cortes (idcortes,corte,valor) VALUES
  (1,'tesoura + barba',30),
  (2,'maquina + barba',35),
  (3,'maquina + tesoura + barba',45),
  (4,'barba',20),
  (5,'maquina',25),
  (6,'tesoura',20),
  (7,'maquina + tesoura',30);
  """
  linha_cliente = []
  for i in range(1,qtd_clientes):
    id = i
    nome = fake.name_male()
    idusuario = 3
    linha_cliente.append(f"""(
    {id},
    '{nome}',
    {idusuario}                     
    )""")
  sql += """
  INSERT INTO cliente 
  (idcliente,nome,usuario_idusuario)
  VALUES
  """ + ",\n".join(linha_cliente)+";\n"
  
  linha_log = []
  for i in range(1,qtd_clientes):
    id = i
    usuario_idusuario = random.choice([1,2,3])
    datahora = fake.date_time()
    linha_log.append(f"""(
    {id},
    {usuario_idusuario},
    '{datahora}'
    )""")
  
  linha_agenda = []
  for i in range(1,10):
    id = i
    datahora = fake.date_time()
    idbarbeiro = random.choice([1,2])
    idcliente = i
    linha_agenda.append(f"""(
    {id},
    '{datahora}',
    {idbarbeiro},
    {idcliente}                    
    )""")
  sql += f"""
  INSERT INTO agenda (idagenda,data_hora,barbeiro_idbarbeiro,cliente_idcliente)
  VALUES
  """+",\n".join(linha_agenda)+";\n"

  sql += """
  INSERT INTO log (idlog,usuario_idusuario,datahora)
  VALUES
  """ + ",\n".join(linha_log)+";\n"

  return sql

if __name__ == "__main__":
  while True:
    try:
      qtd = int(input("Quantos clientes deseja inserir? ")) 
      if qtd >= 10:
        break
      else:
        print("por favor, insira uma quantidade maior que 10")
    except ValueError:
      print("Erro: valor inválido")

  sql = gerar_sql(qtd)
  with open("seed.sql","w", encoding="utf-8") as f:
    f.write(sql)
  print("\nSeed gerado com sucesso!")