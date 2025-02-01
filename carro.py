# Classe para Carro
class Carro:

  def __init__(self, marca, modelo, cor, ano, preco, potencia, disponibilidade, matricula):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco = preco
        self.potencia = potencia
        self.disponibilidade = disponibilidade
        self.matricula = matricula

    def vender(self):
        self.disponibilidade = False

    def __str__(self):
        return f"{self.marca}; {self.modelo}; {self.cor}; {self.ano}; {self.preco}; {self.potencia}; {self.disponibilidade}; {self.matricula}"

    @staticmethod
    def from_string(data_str):
        marca, modelo, cor, ano, preco, potencia, disponibilidade, matricula = data_str.strip().split(";")
        return Carro(marca, modelo, cor, int(ano), float(preco), int(potencia), disponibilidade == "True", matricula)
