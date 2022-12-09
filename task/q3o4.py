# Q 3 / 4 - 25 Points
#Apresentação
print('Olá, bem vindo(a) Programa de Serviços de Limpesa de Alcione Magnus Homem Junior')
print('*'*100)

totalplus= 0


#definir funcoes
def valid_int(pergunta, min, max):
    try:
        x = int(input(pergunta))
        while (( x < min )or( x > max )):
            x = int(input(pergunta))
        return x
    except ValueError:
        valid_int(pergunta, min, max)
def metragem_limpeza():
    pessoa = ''
    price = 0
    metragem = 0
    try:
        metragem = int(input('Informe a metragem em m² da casa: '))
    except ValueError:
        metragem = int(input('Informe a metragem em m² da casa: '))
    if (metragem < 30) or (metragem > 699):
        print('Só trabalhamos com casas entre 30m² em 699m².')
        metragem = int(input('Informe a metragem em m² da casa: '))
    elif metragem < 301:
        price = 60 + (metragem * 0.3)
        pessoa = '1 pessoa'
    else:
        price = 120 + (metragem * 0.5)
        pessoa = '2 pessoas'

    print(f'É necessário contratar {pessoa}.')
    return price
def tipo_limpeza():
    print('Informe o tipo de limpeza')
    print('B - Básica - Indicada para sujeiras mais leves.')
    print('C - Completa 30% a mais - Indicada para sujeiras mais pesadas')
    type = str.upper(input('Escolha o tipo (B ou C): '))
    if type == 'B':
        multi = 1
    elif type == 'C':
        multi = 1.3
    else:
        print('Opção inválida!')
        tipo_limpeza()
    return multi

def choice_option():
    print('Deseja algum adicional de limpeza?')
    print('0 - Não obrigado (encerrar)')
    print('1 - Passar 10 peças de roupas (R$ 10,00)')
    print('2 - Limpeza de 1 Forno ou Microondas (R$ 12,00)')
    print('3 - Limpeza de 1 Geladeira ou Freezer (R$ 20,00)')

    try:
        option = int(input('>>'))
        while ((option < 0) or (option > 3)):
            option = int(input('>>'))
    except ValueError:
        option = int(input('>>'))

    return option

def adicional_limpeza():
    if option == 1:
        plusvalue = 10
    elif option == 2:
        plusvalue = 12
    elif option == 3:
        plusvalue = 20
    return plusvalue


#inicia programa
print('------------------------ Menu 1 de 3 - Metragem Limpeza -------------------------')
metro_value = metragem_limpeza()
print('------------------------ Menu 2 de 3 - Tipo de Limpeza --------------------------')
multiply = tipo_limpeza()
print('------------------------ Menu 3 de 3 - Adicional Limpeza ------------------------')
option = choice_option()
while option > 0:
    plus = adicional_limpeza()
    totalplus += plus
    print(f'Total de add esta em {totalplus}')
    option = choice_option()

print(f'TOTAL: R${(metro_value + totalplus) * multiply:.2f} (metragem: R${metro_value:.2f}, tipo X{multiply}, + adicionais R${totalplus:.2f}')