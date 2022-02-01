"""
elabore um programa que alinhe uma mensagem á direita, esquerda e ao centro.
num campo de edição com 50 carateres.
"""
    
# ____________alinhamentos de mensagem_____________:

#exemplo 1 com Fstring + simbolos
'''
if __name__ == '__main__':
    mensagem='blablabla!\n'
    print(f"{mensagem:>50}")
    print(f"{mensagem:^50}")
    print(f"{mensagem:<50}")
'''

# exemplo 2 com comandos de alinhamento de mensagem
if __name__ == '__main__':
    mensagem='blablabla!\n'
    print(f"{mensagem}".rjust(50))
    print(f"{mensagem}".center(50))
    print(f"{mensagem}".ljust(50))

    
    
    