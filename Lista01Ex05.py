'''
5.	Implemente um programa para ler
o salário mensal atual de um funcionário
e o percentual de reajuste. Calcular
e escrever o valor do novo salário.
'''

salMensal = float(input("Informe o salário mensal -> "))
reaj = float(input("Informe o percentual de aumento -> "))
nSal = salMensal*reaj/100 + salMensal
print(f"O novo salário é R$ {nSal:.2f}")
