'''
leitura de dados logicos

'''

# elabore um programa que pergunte ao utilizador se o resultado de uma determinada,
# operaçao aritmetica é verdadeiro ou falso e imprima a resposta correta.

print("3*5=18", end=" \t")
result = input("True ou False? ")
print("A tua resposta foi: ", result)
print(f"A resposta correta é: {bool(3*5==18)}")