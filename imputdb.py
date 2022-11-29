# Imput dados na tabela de bd
from flask import Flask,render_template, request
import mysql.connector
from flask import MySQL

app = Flask(__name__)

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='lequinha',
    database='dbdesafio3jean'
)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        email = request.form['femail']
        assunto = request.form['fassunto']
        descricao = request.form['fdescricao']
        
        cur = connection.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descricao) VALUES (?, ?, ?)", (email, assunto, descricao))
       
        connection.commit()
        
        cur.close()

        return 'Contato Enviado!'
    return render_template('contatos.html')



# @app.route('/contato', methods=['GET','POST'])
# def contato():
#     if request.method == "POST":
#         email = request.form['email']
#         assunto = request.form['assunto']
#         descricao = request.form['descricao']

#         # imput_dados = f'INSERT INTO contatos (email, assunto, descricao) VALUE ("{email}", "{assunto}", "{descricao}")'
#         imput_dados = ("INSERT INTO contato(email, assunto, descricao) VALUES (%s, %s, %s)",(email, assunto, descricao))

#         cursor = conexao.cursor()
#         cursor.execute(imput_dados)
#         conexao.commit() # edita o bando de dados
#         print(cursor.rowcount, 'Requisitos inseridos com sucesso!')
#         cursor.close()
#         return "dados enviados jean"
    
#     return render_template('contato.html')








# import mysql.connector
# from mysql.connector import Error

# try:
#     conexao = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='lequinha',
#         database='dbdesafio3jean'
#     )

#     email = "naaula@naaula.com.br"
#     assunto = "naaula"
#     descricao = "teste rodando na aula ao vivo"

#    imput_dados = """INSERT INTO contato
#                    (ctto_email, ctto_assunto, ctto_descricao)
#                Values
#                ('nprimeiro@primeiro.com.br', 'primeiro', 'primeira inserção de dados'),
#                ('nsegundo@segundo.com.br', 'segundo', 'segunda inserção de dados'),
#                ('nterceiro@terceiro.com.br', 'terceiro', 'terceiro inserção de dados')"""

#     cursor = conexao.cursor()
#     cursor.execute(imput_dados)
#     conexao.commit() # edita o bando de dados
#     print(cursor.rowcount, 'Requisitos inseridos com sucesso!')
#     cursor.close()

# except Error as erro:
#     print('Falha ao inserir dados na tabela: {}' .format(erro))

# finally:
#     if (conexao.is_connected()):
#         conexao.close()
#         print('Conexão ao MySQL finalizada')

    # imput_dados = """INSERT INTO contato
    #                 (ctto_email, ctto_assunto, ctto_descricao)
    #             Values
    #             ('nprimeiro@primeiro.com.br', 'primeiro', 'primeira inserção de dados'),
    #             ('nsegundo@segundo.com.br', 'segundo', 'segunda inserção de dados'),
    #             ('nterceiro@terceiro.com.br', 'terceiro', 'terceiro inserção de dados')"""
