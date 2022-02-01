'''
despesa diaria media

elabore um programa que calcule a despesa diaria media de um turista 
numa viagem de 4dias ao porto, sabendo que cada dia gastou mais 20%
do que no dia anterior.
'''
# ler a despesa do 1º dia   
# calcular a despesa do 2º 3º 4º dias
# calcular a despesa media diaria:
#   -> add as despesas dos quatro dias
#   -> dividir o total das despesas por 4
# imprimir a despesa media diaria

aumento = 20

d1 = float(input("digite a despesa do primeiro dia: "))
d2 = d1 * (1 + aumento/100)
d3 = d2 * (1 + aumento/100)
d4 = d3 * (1 + aumento/100)

media = (d1+d2+d3+d4)/4

print(f"A despesa media diaria é: {media:1.2f}€")