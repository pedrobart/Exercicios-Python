'''
leitura de datas cronologicas

'''

# elabore um programa que leia a data de nascimento de uma pessoa, e a imprima em diversos formatos
import datetime
dnasci = input("Digite a sua data de nascimento (dd/mm/aaa): ")

dia, mes, ano = map(int, dnasci.split('/'))
DataNasc = datetime.date(ano, mes, dia)
print(DataNasc.strftime("%d-%m-%Y"))
print(DataNasc.strftime("%d-%m-%y"))
