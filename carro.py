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
