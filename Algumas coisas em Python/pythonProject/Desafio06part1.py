euro = float(input('Quanto dinheiro você tem na carteira? EUR'))
real = euro / 0.19
print('Com EUR{} você pode comprar R${:.2f}'.format(euro, real))
