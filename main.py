import função as mf

while True:
    print('---------- Menu ----------')
    print('')
    opçoes = input('1 - Cadastrar Produto\n2 - Listar Produtos\n3 - Atualizar Produto\n4 - Remover Produto\n5 - Sair\n\nDigite uma Opção: ')
    print('')
    if opçoes == '5':
        input('Pressione Enter para Sair...')
        break
    if opçoes == '1':
        print('---------- Cadastrar Produto ----------')
        print('')
        nome = input('Nome do Produto: ')
        categoria = input('Categoria do Produto: ')
        quantidade = input('Quantidade do Produto: ')
        preco = input('Preço do Produto: ')
        mf.cadastrar_produto(nome, categoria, quantidade, preco)
        print('')
        print('Produto Cadastrado com Sucesso!!!')
        print('')
        input('Pressione Enter para Voltar ao Menu...')
        print('')
    if opçoes == '2':
        print('---------- Lista De Produtos ----------')
        print('')
        mf.buscar_produtos()
        print('')
        input('Pressione Enter para Voltar ao Menu...')
        print('')
    if opçoes == '3':
        print('---------- Atualizar Produto ----------')
        print('')
        id = int(input('Id do Produto: '))
        preco = input('Digite o Novo Preço Do Produto: ')
        mf.atualizar_produto(preco, id)
        print('')
    if opçoes == '4':
        print('---------- Remover Produto ----------')
        print('')
        nome = input('Digite o Nome Do Produto: ')
        print('')