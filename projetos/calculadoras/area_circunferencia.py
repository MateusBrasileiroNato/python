from math import pi

def calculo(raio):
    return pi * float(raio) ** 2

raio = input('Informe o raio da circunferência: ')
area_circunferencia = calculo(raio)

print('Área da circunferência = ', area_circunferencia)