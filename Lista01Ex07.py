'''
7.	Escreva um programa que pergunte a
quantidade de km percorridos por um
carro alugado pelo usuário, assim como
a quantidade de dias pelos quais o carro
foi alugado. Calcule o preço a pagar,
sabendo que o carro custa
R$ 60 por dia e R$ 0,15 por km rodado.
'''

print("Informe os dados do carro alugado")
km = float(input("Quantidade de km rodados >> "))
dias = int(input("Dias de aluguel >> "))
custo = km * 0.15 + dias * 60
print(f"O aluguel ficou em R$ {custo:.2f}")
