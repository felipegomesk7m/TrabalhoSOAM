print('\nProdutos disponíveis: Lapiseira, Lápis, Borracha, Estojo ou Caneta')
Produto = input('\nQual produto deseja adquirir? ')

if Produto == 'Lapiseira':
    print('Lapiseira custa 2 reais')
    Quantidade = float(input('Quantas deseja comprar? \n'))
    if Quantidade <= 10:
        print('O Valor total a pagar é R${}'.format(Quantidade*2))
    else:
        print('O limite permitido é 10 lapiseiras por cliente')
elif Produto == 'Lápis':
    print('Lápis custa 1 real')
elif Produto == 'Borracha':
    print('Borracha custa 0.50 centavos')
elif Produto == 'Estojo':
    print('Estojo custa 3 reais')
elif Produto == 'Caneta':
    print('Caneta custa R$ 1.50')
else:
    print('Valor não encontrado')
