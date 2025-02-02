# Importações
from carro import Carro
from persistencia import gravar_carros, carregar_carros

#Ficheiro para gravar ou carregar os carros
FICHEIRO = "carros.txt"

#Func_Princ
def main():
    carros = [] #Lista para Histórico
    while True:
        print("\n1. Adicionar Carro")
        print("2. Listar Carros")
        print("3. Gravar Carros")
        print("4. Carregar Carros")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            marca = input("Marca do Carro: ")
            modelo = input("Modelo do Carro: ")
            cor = input("Cor do Carro: ")
            ano = int(input("Ano do Carro: "))
            preco = input("Preço do Carro")
            potencia = int(input("Potência do Carro: "))
            disponibilidade = input("Vendido ou Disponível (True ou False): ")
            matricula = input("Matrícula: ")

            try:
                ano = int(ano)
                preco = float(preco)
                potencia = int(potencia)
                disponibilidade = disponibilidade.lower() == "true"

                carro = Carro(marca, modelo, cor, ano, preco, potencia, disponibilidade, matricula)

                # Validar carro antes de adicionar à lista
                if carro.is_valid():
                    carros.append(carro)
                    print("Carro adicionado com sucesso.")
                else:
                    print("Falha ao adicionar o carro. Dados inválidos.")

            except ValueError:
                print("Erro: Verifique os valores de ano, preço, potência ou disponibilidade.")


        elif opcao == "2":
            if not carros:
                print("Nenhum carro cadastrado.")
            for carro in carros:
                print(carro)
        elif opcao == "3":
            gravar_carros(FICHEIRO, carros)
        elif opcao == "4":
            carros = carregar_carros(FICHEIRO)
        elif opcao == "5":
            break
        else:
            print("Opção inválida, tente novamente.")
