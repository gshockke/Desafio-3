import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'lequinha',
    database = 'dbdesafio3jean',
) 

cursor = conexao.cursor()

# #CRUD 

email = "adffsadfo@terceiro.com.br"
assunto = "afdasfsdgga"
descricao = "udlfjsaoidjkdsjfosiea"
comando = f'INSERT INTO contato (ctto_email, ctto_assunto, ctto_descricao) VALUE ("{email}", "{assunto}", "{descricao}")'
cursor.execute(comando)
conexao.commit() # edita o bando de dados
resultado = cursor.fetchall() # ler o banco de dados

cursor.close()
conexao.close()

# # CREATE 'etapa de criar dados'
# # email = "segundo@segundo.com.br"
# # assunto = "jabuticaba"
# # descricao = "é redonda na cor preta"
# # comando = f'INSERT INTO contato (ctto_email, ctto_assunto, ctto_descricao) VALUE ("{email}", "{assunto}", "{descricao}")'
# # cursor.execute(comando)
# # conexao.commit() # edita o bando de dados


# # READ
# # comando = f'SELECT * FROM contato'
# # cursor.execute(comando)
# # conexao.commit() #edita o bando de dados
# # resultado = cursor.fetchall() # ler o bando de dados
# # print(resultado)

# # UPDATE
# email = "Rsegundo@segundo.com.br"
# # assunto = "Rjabuticaba"
# # descricao = "R é redonda na cor preta"
# comando = f'UPDATE contato SET ctto_email = "{email}" WHERE ctto_email = "{email}"'
# # comando = f'UPDATE contato SET ctto_assunto = "{assunto}" WHERE ctto_assunto = "{assunto}"'
# # comando = f'UPDATE contato SET ctto_descricao = "{descricao}" WHERE ctto_descricao = "{descricao}"'
# cursor.execute(comando)
# conexao.commit() # edita o bando de dados

# # DELETE
# email = "aeiou@aeiou.com"
# comando = f'DELETE FROM contato WHERE ctto-email = "{email}"'
# cursor.execute(comando)
# conexao.commit() #edita o bando de dados
