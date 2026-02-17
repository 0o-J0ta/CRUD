#CRUD

import mysql.connector

conexao = mysql.connector.connect(
    host="IP_HOST",
    user='USUARIO',
    password='SENHA_USUARIO',
    database='NOME_DB',

)

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

cursor.close()
conexao.close()
