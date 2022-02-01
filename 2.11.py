'''
elabore um programa que calcule e imprima o maior de tres numeros diferentes
'''
# ler três numeros 
# determinar o maior, comparando os numeros, dois a dois
# imprimir o maior

a = float(input("digite o numero1: "))
b = float(input("digite o numero2: "))
c = float(input("digite o numero3: "))

if a > b:
    if a > c:
        maior = a
    else:
        maior = c
elif b > c:
    maior = b
else:
    maior = c
    
print(f"{maior:3.2f} é o maior de:\n{a:3.2f}, \n{b:3.2f}, \n{c:3.2f}")

    
    
    