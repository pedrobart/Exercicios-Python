'''
capital acumulado

'''

# elaborar um programa que calcule o capital que resulta da capitalizaçao composta de X €, 
# durante N anos, á taxa de juros anual de 1%

import math 

x = 1000
i = 0.01
n = 2

capital_acumulado = x * math.pow((1+i), n)

print(f"{x:5.2f}€ capitalizados, durante {n} anos, á taxa anual de {i:1.0%} resultam, em {capital_acumulado:1.2f}€")