# Imput dados na tabela de bd

import mysql.connector
from mysql.connector import Error

try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='lequinha',
        database='dbdesafio3jean'
    )

    imput_dados = """INSERT INTO contato
                    (ctto_email, ctto_assunto, ctto_descricao)
                Values
                ('nprimeiro@primeiro.com.br', 'primeiro', 'primeira inserção de dados'),
                ('nsegundo@segundo.com.br', 'segundo', 'segunda inserção de dados'),
                ('nterceiro@terceiro.com.br', 'terceiro', 'terceiro inserção de dados')"""
    

    cursor = conexao.cursor()
    cursor.execute(imput_dados)
    conexao.commit()
    print(cursor.rowcount, 'Requisitos inseridos com sucesso!')
    cursor.close()

except Error as erro:
    print('Falha ao inserir dados na tabela: {}' .format(erro))

finally:
    if (conexao.is_connected()):
        conexao.close()
        print('Conexão ao MySQL finalizada')
