# Classe para Carro
class Carro:
   lista_marcas = ["Mercedes", "BMW", "Bugatti", "Porsche", "Ferrari", "Lexus"]
  
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

    def is_valid(self):
        if not self.marca or not self.modelo:
            print("Erro: O carro deve ter uma marca e um modelo.")
            return False

        if self.marca not in Carro.lista_marcas:
            print(f"Erro: A marca '{self.marca}' não é válida. Marcas permitidas: {', '.join(Carro.lista_marcas)}.")
            return False
