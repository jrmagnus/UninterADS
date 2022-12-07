#Q 1 / 4 - 25 Points

print('Bem vindo a Loja de Alcione Magnus Homem Junior')

value = float(input('Entre com o valor do produto: '))
qtd = int(input('Entre com a quantidade do produto: '))

#verifica a quantidade se é maior de zero.
if qtd >= 0 and value >= 0:
    if qtd in range (0,12):
        frete = 30
    elif qtd in range (12,101):
        frete = 60
    elif qtd in range (101,1001):
        frete = 120
    else:
        frete = 240

    #saida quantidade do valor sem frete
    print(f'O valor sem frete é de: R${value*qtd:.2f}')

    #saida quantidade do valor mais o frete
    print(f'O valor com frete é de: R${frete+(value*qtd):.2f}')

#saida caso valor seja negativo
else:
    print('Quantidade invalida!')