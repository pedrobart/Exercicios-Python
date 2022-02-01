'''
maior de dois
'''

# elabore um programa que imprima o maior de dois numeros reais


# algoritmo:

# ler os dois numeros
# determinar o maior, comparando os dois numeros
# imprimir o maior

a = float(input("digite o numero1 para comparar: "))
b = float(input("Digite o numero2 para comparar: "))

if a > b:
    maior = a
else:
    maior = b
print(f"O maior numero entre {a} e {b} é {maior}.")