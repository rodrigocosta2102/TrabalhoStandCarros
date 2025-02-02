# persistencia.py
from carro import Carro

def gravar_carros(ficheiro, lista_carro):
    if not lista_carro:
        print("A lista de carros está vazia.")
        return

    with open(ficheiro, "w") as f:
        for carro in lista_carro:
            f.write(str(carro) + "\n")
    print(f"Carros gravados em '{ficheiro}' com sucesso!")

def carregar_carros(ficheiro):
    carros = []
    try:
        with open(ficheiro, "r") as f:
            for linha in f:
                try:
                    carro = Carro.from_string(linha) #Criar um objeto através da string feita no ficheiro carro.py
                    if carro.is_valid(): #Para validar o carro antes de guardar os dados
                        carros.append(carro)
                    else:
                        print(f"Dados inválidos ignorados: {linha.strip()}")
                except Exception as e:
                    print(f"Erro ao processar linha: {linha.strip()} - {e}")
        print(f"Carros carregados de '{ficheiro}' com sucesso!")
    except FileNotFoundError:
        print(f"O ficheiro '{ficheiro}' não foi encontrado.")
    return carros
