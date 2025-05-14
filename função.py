# 1. Cadastrar ao banco de dados

import mysql.connector as my


# 2. Criar uma função para conectar ao banco de dados
def conectar_banco():
    conexao = my.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'estoque'
    )
    return conexao
# 3. Criar uma função para cadastrar produtos
def cadastrar_produto(nome, quantidade, preco):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO produtos (nome, quantidade, preco) VALUES (%s, %s, %s)"
    valores = (nome, quantidade, preco)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

# função de busca larissa
def buscar_produtos():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'SELECT * FROM produto'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    print(resultado)
    conexao.close()
    return resultado



# Função Ismael
