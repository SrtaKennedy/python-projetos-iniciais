# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava{:.2f}, com 15% de aumento, para a receber R${:.2f}'.format(salário, novo))