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
