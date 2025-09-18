velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO!! Você execedeu o limite permitido de 80 Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa no valor de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija cuidado!')    