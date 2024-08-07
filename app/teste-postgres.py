import psycopg2

# Parâmetros de conexão
dbname   = 'postgres'
user     = 'postgres'
password = 'password'
host     = 'localhost'
port     = '5432' 

# Criar uma conexão
conn = psycopg2.connect(dbname=dbname,
                        user=user,
                        password=password,
                        host=host,
                        port=port)


cur = conn.cursor()# Criar um cursor  deixa manipular os dados

#comandos sql transct-sql
conn.commit() # validar alterações que agente fez  e subir para o banco de dados 

# Fechar o cursor e a conexão
cur.close()
conn.close()