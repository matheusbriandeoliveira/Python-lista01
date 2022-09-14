'''
6. Implemente um programa para ler o preço do litro do combustível de um carro, ler o desempenho
do veículo (km/l) e a distância entre duas cidades (km), e informar quantos litros, e quanto dinheiro
vai ser gasto para fazer uma viagem entre as duas cidades.
'''
print('Entre com as informações da viagem')
precoLitro = float(input('Preço do combustível >> '))
desempenho = float(input('Desempenho do veículo >> '))
distancia = float(input('Distância >> '))
litros = distancia / desempenho
total = litros * precoLitro
print(f'Você precisará de {litros:.2f} litros e '
      f'gastará R$ {total:.2f} para fazer a viagem')