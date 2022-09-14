'''
8.	Escreva um programa para ler um
uma temperatura em graus Fahrenheit,
calcular e escrever o valor correspondente
em graus Celsius:
C = ((F – 32)/9)*5
'''
F = float(input("graus Fahrenheit >> "))
C = ((F - 32)/9)*5
print(f"{F}°F = {C:.1f}°C")
