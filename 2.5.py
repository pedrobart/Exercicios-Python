carros = int(input("Numero de carros vendidos: "))
nome = input(("Nome do vendedor: "))
p = float(input("Digite a percentagem sobre o valor das vendas: "+ " (%) "))
salariobase = float(input("Digite o salario base: "))
comissao = float(input("digite a comissao por cada carro vendido: "))
vendas = float(input("Digite o valor das vendas: "))

sal = salariobase + carros * comissao + vendas * p / 100
print(f"O salario a processar para {nome} é: {sal:7.2f} €")