# Importações
from carro import Carro
from persistencia import gravar_carros, carregar_carros

# Ficheiro para gravar ou carregar os carros
FICHEIRO = "carros.txt"

# Função Principal
def main():
    #Lista para histórico
    carros = [] 

    while True:
        print("1. Adicionar Carro")
        print("2. Listar Carros")
        print("3. Gravar Carros")
        print("4. Carregar Carros")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            marca = input("Marca do Carro: ").strip()
            modelo = input("Modelo do Carro: ").strip()
            cor = input("Cor do Carro: ").strip()
            ano = input("Ano do Carro: ").strip()
            preco = input("Preço do Carro: ").strip()
            potencia = input("Potência do Carro: ").strip()
            matricula = input("Matrícula: ").strip().upper()

            while True:
                disponibilidade = input("Vendido ou Disponível (True ou False): ").strip().lower()
                if disponibilidade in ["true", "false"]:
                    disponibilidade = disponibilidade == "true"
                    break
                print("Erro: Digite 'True' ou 'False'.")

            try:
                ano = int(ano)
                preco = float(preco)
                potencia = int(potencia)

                carro = Carro(marca, modelo, cor, ano, preco, potencia, disponibilidade, matricula)

                # Validar carro antes de adicionar à lista
                if carro.is_valid():
                    carros.append(carro)
                    print("Carro adicionado com sucesso!")
                else:
                    print("Falha ao adicionar o carro. Dados inválidos.")

            except ValueError:
                print("Erro: Verifique os valores de ano, preço ou potência.")

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
            print("Programa encerrado.")
            break

        else:
            print(" Opção inválida, tente novamente.")

# Executar a Função Principal
if __name__ == "__main__":
    main()
