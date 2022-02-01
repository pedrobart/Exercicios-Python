'''
formatos parametrizados para arredondamentos

'''

# programa que imprima 4.78905 arredondado a três, duas a zero casas decimais, usando o formato com dois parametros:
# NC :
# que significa o numero total de carateres - espaços, ponto decimal e digitos.
# CD : 
# que significa o numero de casas decimais

numero = 4.78905

fstring = "{0:{NC}.{CD}f}"

print(fstring.format(numero, NC=5, CD=3))
print(fstring.format(numero, NC=4, CD=2))
print(fstring.format(numero, NC=1, CD=0))
