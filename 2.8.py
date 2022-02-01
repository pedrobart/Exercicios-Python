'''
elabore um programa que, de acordo com a hora corrente, afixe uma mensagem
de 'bom dia ou boa tarde'

'''

# -> extrair a hora corrente da data de hoje
# -> determinar o conteudo da mensagem, comparando a hora corrente com o meio-dia (12)
# -> escrever a mensagem

import datetime

meiodia = 12
msg = "bom dia!"
horacorrente = datetime.datetime.now().hour
if horacorrente > meiodia:
    msg = "boa tarde!"
print(msg)