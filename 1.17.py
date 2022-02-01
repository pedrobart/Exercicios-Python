'''
formatos para arredondamentos
'''
'''

'''
# elabore um programa que imprima os seguintes numeros, arredondados respetivamente a:
# três , duas, uma e duas casas decimais:
'''
4.78905;
4.7;
5.8954;
5.

'''

n1, n2, n3, n4 = 4.78905, 4.7, 5.8954, 5
print(f"Numeros:\n{n1,n2,n3,n4}")
print("arredondamentos:\n ")
print(f"{n1} arredondado a 3casas decimais fica: {n1:4.3f}")
print(f"{n2} arredondado a 2casas decimais fica: {n2:4.2f}")
print(f"{n3} arredondado a 1casa decimal fica: {n3:1.1f}")
print(f"{n4} acrescentando 2casas decimais: {n4:1.2f}")

