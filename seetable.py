
# Sprint para consultar tabela em bd

import mysql.connector
from mysql.connector import Error


try: # try realiza teste
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='lequinha',
        database='dbdesafio3jean'
    )

    see_contato = 'select * from contato'
    cursor = conexao.cursor()
    cursor.execute (see_contato)
    linhas = cursor.fetchall()
    print('\nNúmero total de registros retornados = ', cursor.rowcount)

    print('\nMostrando dados solicitados:')
    for linha in linhas:
        print('e-mail :', linha[1])
        print('Assunto :', linha[2])
        print('Descrisção :', linha[3], '\n')
    
except Error as e:
    print('Erro ao acessar tabela no MySql', e)

finally:
    if(conexao.is_connected()):
        conexao.close()
        cursor.close()
        print('Conexão ao MySql encerrada')
    


