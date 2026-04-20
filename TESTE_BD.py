#CRUD
#Para importar essa biblioteca certifique-se que instalou o pacote mysql-connector-python na sua IDE
#comando: pip install mysql-connector-python
import mysql.connector

#Nessa primeira parte você precisa criar a conexão com o seu banco de dados e importar as seguintes infos para acessar
conexao = mysql.connector.connect(
    host="IP_HOST",
    user='USUARIO',
    password='SENHA_USUARIO',
    database='NOME_DB',

)

#Aqui e criado a função de "cursor" que vai servir como um mecanismo de controle que permite executar os comandos do CRUD
cursor = conexao.cursor()

#Create
produto = 'Salgadinho'
valor = 3.5

comando_create = f'INSERT INTO VENDAS (NOME_PRODUTO, VALOR_PRODUTO) VALUES ("{produto}", {valor})'
cursor.execute(comando_create)
conexao.commit()

#Read
comando_read = f'SELECT * FROM VENDAS'
cursor.execute(comando_read)
comando_read = cursor.fetchall()
lista = comando_read
for itens in lista:
    print(itens)


#Update
comando_update = f'UPDATE VENDAS SET VALOR_PRODUTO = 10 WHERE ID_VENDA=5'
cursor.execute(comando_update)
conexao.commit()

#Delete
comando_delete = f'DELETE FROM VENDAS WHERE ID_VENDA=5'
cursor.execute(comando_delete)
conexao.commit()

#Essas funções vão finalizar a conexão a cada um dos comados utilizados.
cursor.close()
conexao.close()
