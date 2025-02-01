# Classe para Carro
class Carro:
   lista_marcas = ["Mercedes", "BMW", "Bugatti", "Porsche", "Ferrari", "Lexus"]
   lista_cores = ["Preto", "Azul", "Vermelho", "Laranja", "Cinzento", "Branco", "Verde"]
  
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

      if not self.cor or self.cor not in Carro.lista_cores:
            print(f"Erro: A cor '{self.cor}' não é válida. Cores permitidas: {', '.join(Carro.lista_cores)}.")
            return False

      if not isinstance(self.ano, int) or self.ano <= 0:
            print("Erro: O ano deve ser um número inteiro positivo.")
            return False

      if not isinstance(self.preco, (int, float)) or self.preco <= 0:
            print("Erro: O preço deve ser um número positivo.")
            return False

      if not isinstance(self.potencia, int) or self.potencia <= 0:
            print("Erro: A potência deve ser um número inteiro positivo.")
            return False

      if not isinstance(self.disponibilidade, bool):
            print("Erro: A disponibilidade deve ser um valor booleano (True ou False).")
            return False

      # Regex para a matrícula (AA-00-AA)
        if not self.matricula or not re.fullmatch(r"[A-Z]{2}-\d{2}-[A-Z]{2}", self.matricula):
            print(
                "Erro: O campo 'matrícula' deve seguir o formato 'AA-00-AA', onde 'A' são letras maiúsculas e '0' são números."
            )
            return False

      # Se todos os dados estiverem válidos
        print("O carro foi cadastrado com sucesso.")
        return True

