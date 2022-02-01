'''
formatos para data e hora correntes

https://docs.python.org/pt-br/3/library/datetime.html#
'''
import datetime

dataHoje=datetime.datetime.today()

print("dataHoje",datetime.date.today().strftime("%d-%m-%y"))
print(dataHoje.strftime("%d-%m-%Y %H:%M:%S"))
print(dataHoje.strftime("%m-%d-%y %H:%M:%S"))
print(dataHoje.strftime("%d-%m-%y"))
print(dataHoje.strftime("%H:%M:%S"))