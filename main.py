value = float(input('Qual o valor do produto?'))
descount = float(input('Qual a porcentagem de desconto?'))

valuedesc = value * (descount / 100)

print(f'O valor de desconto é de R${valuedesc}, valor final ficou de R${value-valuedesc}')