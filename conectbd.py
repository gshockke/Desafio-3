# Script para conectar ao bando de dados

import mysql.connector

# criando o objeto de coneccao
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='lequinha',
    database='dbdesafio3jean'
)

# verificar se o objeto de coneccao esta funciondo
if conexao.is_connected():
    conectado = conexao.get_server_info()
    print('Conectado ao servidor MySQL', conectado)

    cursor = conexao.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('Conectado ao bando de dados', linha)


# desconecta o obeto de coneccao com o bd
if conexao.is_connected():
    cursor.close()
    conexao.close()
    print('Conexão ao MySQL esta encerrada')

# Script para conectar ao bando de dados
