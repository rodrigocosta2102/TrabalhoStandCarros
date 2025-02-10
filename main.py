# Importações
from persistencia import gravar_carros, carregar_carros, gravar_stand, carregar_stand

# Ficheiros para armazenar os dados
FICHEIRO_CARROS = "carros.txt"
FICHEIRO_STAND = "stand.txt"

# Função Principal
def main():
    carros = []  # Lista para armazenar carros
    stand_lista = []  # Lista para armazenar stands

    while True:
        print("\n1. Adicionar Carro")
        print("2. Listar Carros")
        print("3. Gravar Carros")
        print("4. Carregar Carros")
        print("5. Adicionar Stand")
        print("6. Listar Stands")
        print("7. Gravar Stands")
        print("8. Carregar Stands")
        print("9. Sair")
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
                carro = f"{marca};{modelo};{cor};{ano};{preco};{potencia};{disponibilidade};{matricula}"
                carros.append(carro)
                print("Carro adicionado com sucesso!")

            except ValueError:
                print("Erro: Verifique os valores de ano, preço ou potência.")

        elif opcao == "2":
            if not carros:
                print("Nenhum carro cadastrado.")
            else:
                print("Lista de Carros:")
                for carro in carros:
                    print(carro)

        elif opcao == "3":
            gravar_carros(FICHEIRO_CARROS, carros)

        elif opcao == "4":
            carros = carregar_carros(FICHEIRO_CARROS)

        elif opcao == "5":
            nome = input("Nome do Stand: ").strip()
            localizacao = input("Localização do Stand: ").strip()
            contato = input("Contato do Stand (9 dígitos): ").strip()

            if contato.isdigit() and len(contato) == 9:
                stand = f"{nome};{localizacao};{contato}"
                stand_lista.append(stand)
                print("Stand adicionado com sucesso!")
            else:
                print("Erro: O contato deve ter exatamente 9 dígitos.")

        elif opcao == "6":
            if not stand_lista:
                print("Nenhum stand cadastrado.")
            else:
                print("Lista de Stands:")
                for stand in stand_lista:
                    print(stand)

        elif opcao == "7":
            gravar_stand(FICHEIRO_STAND, stand_lista)

        elif opcao == "8":
            stand_lista = carregar_stand(FICHEIRO_STAND)

        elif opcao == "9":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
