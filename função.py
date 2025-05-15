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
def cadastrar_produto(nome, categoria, quantidade, preco):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = "INSERT INTO produto (nome, categoria, quantidade, preco) VALUES (%s, %s, %s, %s)"
    valores = (nome, categoria, quantidade, preco)
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
    for i in resultado:
        print(f'Nome: {i['nome']} - Categoria: {i['categoria']} - Quantidade: {i['quantidade']} - Preço: {i['preco']}')
    conexao.close()
    return resultado

# Função Ismael

def atualizar_produto(preco, id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = 'UPDATE produto SET preco = %s WHERE id = %s'
    cursor.execute(sql, (preco, id ))
    conexao.commit()
    conexao.close()
    print('Produto Atualizado com Sucesso!!!')

    def remover_produto(nome):
        conexao = conectar_banco()
        cursor = conexao.cursor()
        sql = 'DELETE FROM produto WHERE nome = %s'
        cursor.execute(sql, (nome,))
        conexao.commit()
        conexao.close()
        print('Produto Removido com Sucesso!!!')
    # 4. Criar uma função para atualizar produtos