"""
Elabore um programa que calcule o valor de verdade/booleano 
das seguintes proposições:

4 == 5

4! = 6

4 < 5  e  6 > 10

40 < 50 ou 60 > 90

not(40 > 5 ou 60 > 145)
  
"""
e1 = 4 == 5
e2 = 4 != 6
e3 = 4 > 5 and 6 > 10
e4 = 40 < 50 or 60 > 90
e5 = not((40 > 5 or 60 > 145))

print(f"{e1},\n{e2},\n{e3},\n{e4},\n{e5}\n")