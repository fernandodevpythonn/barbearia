from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
import os#importa variáveis do sistema operacional

load_dotenv()#carrega as variáveis do .env

def get_connection():
    try:#pegando as variáveis de ambiente, direto do .env
      host = os.getenv("DB_HOST")
      user = os.getenv("DB_USER")
      password = os.getenv("DB_PASS")
      database = os.getenv("DB_NAME")

      if not all([host,user,password,database]):#se não encontrar todos esses parametros, retorna erro de variáveis de ambiente
         raise Exception("Variáveis de ambiente não configuradas")
      conn = mysql.connector.connect(#fazendo conexão
         host = host,
         user = user,
         password = password,
         database = database,
         autocommit = True#faz commit automatico
      )
      return conn#retorna a conexão
    except Error as e:
       print(f"[Erro banco de dados] {e}")
       return None#para indicar erro na conexão