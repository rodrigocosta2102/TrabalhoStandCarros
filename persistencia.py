# persistencia.py

from carro import Carro
from stand import Stand

def gravar_carros(ficheiro, lista_carros):
    if not lista_carros:
        print("A lista de carros está vazia.")
        return

    try:
        with open(ficheiro, "w") as f:
            for carro in lista_carros:
                f.write(str(carro) + "\n")
        print(f"Carros gravados em '{ficheiro}' com sucesso!")
    except Exception as e:
        print(f"Erro ao gravar carros: {e}")


def carregar_carros(ficheiro):
    carros = []
    try:
        with open(ficheiro, "r") as f:
            for linha in f:
                try:
                    carro = Carro.from_string(linha.strip())  # Criar objeto Carro
                    if carro.is_valid():  # Validar carro antes de adicionar
                        carros.append(carro)
                    else:
                        print(f"Dados inválidos ignorados: {linha.strip()}")
                except Exception as e:
                    print(f"Erro ao processar linha: {linha.strip()} - {e}")
        print(f"Carros carregados de '{ficheiro}' com sucesso!")
    except FileNotFoundError:
        print(f"O ficheiro '{ficheiro}' não foi encontrado.")
    return carros


def gravar_stand(ficheiro, lista_stands):
    if not lista_stands:
        print("A lista de stands está vazia.")
        return

    try:
        with open(ficheiro, "w") as f:
            for stand in lista_stands:
                f.write(f"{stand.nome}, {stand.localizacao}, {stand.contato}\n")
        print(f"Stands gravados em '{ficheiro}' com sucesso!")
    except Exception as e:
        print(f"Erro ao gravar stands: {e}")


def carregar_stand(ficheiro):
    stands = []
    try:
        with open(ficheiro, "r") as f:
            for linha in f:
                stand = Stand.from_string(linha.strip())  # Criar objeto Stand
                if stand:
                    stands.append(stand)
        print(f"Stands carregados de '{ficheiro}' com sucesso!")
    except FileNotFoundError:
        print(f"O ficheiro '{ficheiro}' não foi encontrado.")
    return stands
