# Importações
from persistencia import gravar_carros, carregar_carros, gravar_stand, carregar_stand
from stand import obter_nome_stand, obter_localizacao_stand, obter_contato_stand, obter_email_stand, obter_password_stand, Stand
from carro import obter_marca, obter_modelo, obter_cor, obter_ano, obter_preco, obter_potencia, obter_matricula, obter_disponibilidade, Carro

# Ficheiros para armazenar os dados
FICHEIRO_CARROS = "carros.txt"
FICHEIRO_STAND = "stand.txt"

# Função Principal
def main():
    Carro.carregar_modelos("marcas_modelos.txt")

    carros = []  # Lista para armazenar carros
    stand_lista = []  # Lista para armazenar stands

    while True:
        print("\n🏡 Menu Principal:")
        print("1. 🚗 Adicionar Carro")
        print("2. 🧾 Listar Carros")
        print("3. 📂 Carregar Carros")
        print("4. ✏️ Editar carros")
        print("5. 🏢 Adicionar Stand")
        print("6. 📃 Listar Stands")
        print("7. 📤 Carregar Stands")
        print("8. ✏️ Editar Stands")
        print("9. ❌ Sair")
        opcao = input("🔹Escolha uma opção: ").strip()

        if opcao == "1":
            marca = obter_marca()
            modelo = obter_modelo(marca)
            cor = obter_cor()
            ano = obter_ano()
            preco = obter_preco()
            potencia = obter_potencia()
            disponibilidade = obter_disponibilidade()
            matricula = obter_matricula()

            carro = Carro(marca, modelo, cor, ano, preco, potencia, disponibilidade, matricula)
            carros.append(carro)
            gravar_carros(FICHEIRO_CARROS, carros)

            print("\nCarro cadastrado com sucesso!✅")
            print(f"▫️Marca: {carro.marca}")
            print(f"▫️Modelo: {carro.modelo}")
            print(f"▫️Cor: {carro.cor}")
            print(f"▫️Ano: {carro.ano}")
            print(f"▫️Preço: {carro.preco}€")
            print(f"▫️Potência: {carro.potencia} CV")
            print(f"▫️Disponível: {'Sim' if carro.disponibilidade else 'Não'}")
            print(f"▫️Matrícula: {carro.matricula}")



        elif opcao == "2":
            carros = carregar_carros(FICHEIRO_CARROS)
            if not carros:
                print("Nenhum carro cadastrado.")
            else:
                print("Lista de Carros:")
                for carro in carros:
                    print(carro)

        elif opcao == "3":
            carros = carregar_carros(FICHEIRO_CARROS)


        elif opcao == "4":
            if not carros:
                print("Nenhum carro cadastrado para editar.")
            else:
                print("Lista de carros disponíveis para edição:")
                for i, carro in enumerate(carros, start=1):
                    print(f"{i}. {carro.marca} {carro.modelo} - Matrícula: {carro.matricula}")

                matricula_editar = input("\n🔍 Insira a matrícula do carro que deseja editar: ").strip().upper()
                carro_encontrado = next((c for c in carros if c.matricula == matricula_editar), None)

                if carro_encontrado:
                    print(f"\n🔧 A editar o carro: {carro_encontrado.marca} {carro_encontrado.modelo}")
                    carro_encontrado.editar_info()
                    gravar_carros(FICHEIRO_CARROS, carros)
                    print("✅ Edição concluída com sucesso e guardada no ficheiro.")

                else:
                    print("❌ Carro com a matrícula especificada não encontrado.")


        elif opcao == "5":
            nome = obter_nome_stand()
            localizacao = obter_localizacao_stand()
            contato = obter_contato_stand()
            email = obter_email_stand()
            password = obter_password_stand()

            stand = Stand(nome, localizacao, contato, email, password)
            stand_lista.append(stand)
            gravar_stand(FICHEIRO_STAND, stand_lista)

            print("\nStand cadastrado com sucesso!✅")
            print(f"▫️Nome do Stand: {stand.nome}")
            print(f"▫️Localização: {stand.localizacao}")
            print(f"▫️Contato: {stand.contato}")
            print(f"▫️Email: {stand.email}")


        elif opcao == "6":
            stand_lista = carregar_stand(FICHEIRO_STAND)
            if not stand_lista:
                print("Nenhum stand cadastrado.")
            else:
                print("\n📃 Lista de Stands:")
                for stand in stand_lista:
                    print(f"🏢 Nome: {stand.nome}")
                    print(f"📍 Localização: {stand.localizacao}")
                    print(f"📞 Contato: {stand.contato}")
                    print(f"📧 Email: {stand.email}")
                    print("────────────────────────")

        elif opcao == "7":
            stand_lista = carregar_stand(FICHEIRO_STAND)

        elif opcao == "8":
            stand_lista = carregar_stand(FICHEIRO_STAND)
            if not stand_lista:
                print("Nenhum stand cadastrado para editar.")
            else:
                print("\nLista de Stands disponíveis para edição:")
                for i, stand in enumerate(stand_lista, start=1):
                    print(f"{i}. {stand.nome} - Localização: {stand.localizacao}")

                indice_editar = input("\n🔍 Insira o número do stand que deseja editar: ").strip()

                if indice_editar.isdigit() and 1 <= int(indice_editar) <= len(stand_lista):
                    stand_encontrado = stand_lista[int(indice_editar) - 1]
                    stand_encontrado.editar_info()
                    gravar_stand(FICHEIRO_STAND, stand_lista)
                    print("✅ Edição do stand concluída com sucesso.")
                else:
                    print("❌ Número inválido. Nenhum stand editado.")

        elif opcao == "9":
            print("Muito obrigado, volte sempre 👋")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
