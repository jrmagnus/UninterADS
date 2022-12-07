# Q 2 / 4 - 25 Points
# Apresentação e menu
print('Bem vindo a sorveteria de Alcione Magnus Homem Junior')
print('-------------------------------------------Cardápio--------------------------------------------')
print('| Código | Descrição            | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |')
print('|   TR   | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |      R$ 18,00      |')
print('|   ES   | Sabores Especiais    |      R$ 7,00      |      R$ 12,00      |      R$ 21,00      |')
print('|   PR   | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |      R$ 24,00      |')
print('-----------------------------------------------------------------------------------------------')

# definindo variaveis dos valores
trp = 6
trm = 10
trg = 18
esp = 7
esm = 12
esg = 21
prp = 8
prm = 14
prg = 24
total = 0

# função para pedido
def inputs():
    size = input('Entre com o TAMANHO do pote desejada (P/M/G): ')
    type = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR) :')

    if (size == 'P' or size == 'M' or size == 'G') and (type == 'TR' or type == 'ES' or type == 'PR'):
        while size == 'P':
            if type == 'TR':
                value = trp
                type = 'TRADICIONAL'
                break
            elif type == 'ES':
                value = esp
                type = 'ESPECIAL'
                break
            elif type == 'PR':
                value = prp
                type = 'PREMIUM'
                break
        while size == 'M':
            if type == 'TR':
                value = trm
                type = 'TRADICIONAL'
                break
            elif type == 'ES':
                value = esm
                type = 'ESPECIAL'
                break
            elif type == 'PR':
                value = prm
                type = 'PREMIUM'
                break
        while size == 'G':
            if type == 'TR':
                value = trg
                type = 'TRADICIONAL'
                break
            elif type == 'ES':
                value = esg
                type = 'ESPECIAL'
                break
            elif type == 'PR':
                value = prg
                type = 'PREMIUM'
                break

        total = value + total
        print(f'Você pediu um sorvete sabor {type} {size} de R${value},00')

    else:
        print('!!! TAMANHO OU CÓDIGO INVALIDO !!!')
        inputs()

inputs()
