from calculo import Calculo

def main():

    print(
        """
        Olá!
        
        Esta calculadora tem como finalidade demonstrar os valores que serão gastos
        com combustível durante uma viagem, com base no consumo do seu veículo, e
        com a distância determinada por você!
        """
    )

    print("Os combustíveis disponíveis para o cálculo são:")
    print("    ° Álcool")
    print("    ° Díesel")
    print("    ° Gasolina")
    print(" ")

    try: 
        distancia = float(input("Qual a distância em Quilômetros a ser percorrida? "))
        consumo = float(input("Qual o consumo médio de combustível do veículo (Km/l)? "))
        calculo = Calculo()
        print(
            calculo.calcular_gasto(distancia, consumo)
        )
    except ValueError as erro:
        print("O valor recebido não é válido.")

if __name__ == "__main__":
    main()