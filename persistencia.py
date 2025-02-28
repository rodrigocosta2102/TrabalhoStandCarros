# persistencia.py

from carro import Carro
from stand import Stand

def gravar_carros(ficheiro, lista_carros):
    with open(ficheiro, "w") as f:
        for carro in lista_carros:
            linha = f"{carro.marca}; {carro.modelo}; {carro.cor}; {carro.ano}; {carro.preco}; {carro.potencia}; {carro.disponibilidade}; {carro.matricula}\n"
            f.write(linha)
    print("💾 Carros gravados com sucesso.")



def carregar_carros(ficheiro):
    carros = []
    try:
        with open(ficheiro, "r") as f:
            for linha in f:
                marca, modelo, cor, ano, preco, potencia, disponibilidade, matricula = linha.strip().split("; ")
                carro = Carro(marca, modelo, cor, int(ano), float(preco), int(potencia), disponibilidade == "True", matricula)
                carros.append(carro)
        print("📂 Carros carregados com sucesso.")
    except FileNotFoundError:
        print(f"⚠️ Ficheiro {ficheiro} não encontrado.")
    return carros


def gravar_stand(ficheiro, lista_stands):
    with open(ficheiro, "w") as f:
        for stand in lista_stands:
            linha = f"{stand.nome}; {stand.localizacao}; {stand.contato}; {stand.email}; {stand.password}\n"
            f.write(linha)
    print("💾 Stands gravados com sucesso.")


def carregar_stand(ficheiro):
    stands = []
    try:
        with open(ficheiro, "r") as f:
            for linha in f:
                nome, localizacao, contato, email, password = linha.strip().split("; ")
                stand = Stand(nome, localizacao, contato, email, password)
                stands.append(stand)
        print("📂 Stands carregados com sucesso.")
    except FileNotFoundError:
        print(f"⚠️ Ficheiro {ficheiro} não encontrado.")
    return stands
