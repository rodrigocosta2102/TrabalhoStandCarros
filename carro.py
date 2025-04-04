import re

# Classe para Carro
class Carro:
    # Regex para a matrícula (AA-00-AA)
    regex_matricula = r"^[A-Z]{2}-\d{2}-[A-Z]{2}$"

    lista_marcas = ["Mercedes", "BMW", "Bugatti", "Porsche", "Ferrari", "Lexus"]
    lista_cores = ["Preto", "Azul", "Vermelho", "Laranja", "Cinzento", "Branco", "Verde"]
    marcas_modelos = {}

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
        if not self.disponibilidade:
            print("Este carro já foi vendido.")
        else:
            self.disponibilidade = False
            print(f"O carro {self.marca} {self.modelo} foi vendido com sucesso!")

    def __str__(self):
        return f"{self.marca}; {self.modelo}; {self.cor}; {self.ano}; {self.preco}; {self.potencia}; {self.disponibilidade}; {self.matricula}"

    @staticmethod
    def validar_marca(marca):
        return marca in Carro.lista_marcas

    @staticmethod
    def carregar_modelos(ficheiro_modelos="marcas_modelos.txt"):
        try:
            with open(ficheiro_modelos, "r") as f:
                for linha in f:
                    marca, modelos = linha.strip().split(":")
                    Carro.marcas_modelos[marca] = [m.strip() for m in modelos.split(",")]
            print("Modelos carregados com sucesso.")
        except FileNotFoundError:
            print(f"Ficheiro '{ficheiro_modelos}' não encontrado.")
        except Exception as e:
            print(f"Erro ao processar o ficheiro: {e}")

    @staticmethod
    def validar_modelo(marca, modelo):
        if marca in Carro.marcas_modelos and modelo in Carro.marcas_modelos[marca]:
            return True
        print(f"Modelo inválido! Modelos válidos para {marca}: {Carro.marcas_modelos.get(marca, [])}")
        return False

    @staticmethod
    def validar_cor(cor):
        return cor in Carro.lista_cores

    @staticmethod
    def validar_ano(ano):
        return isinstance(ano, int) and 1900 <= ano <= 2025

    @staticmethod
    def validar_preco(preco):
        return isinstance(preco, (int, float)) and preco > 0

    @staticmethod
    def validar_potencia(potencia):
        return isinstance(potencia, int) and potencia > 0

    @staticmethod
    def validar_matricula(matricula):
        return re.match(Carro.regex_matricula, matricula) is not None

    def is_valid(self):
        return (self.validar_marca(self.marca) and
                self.validar_modelo(self.modelo, self.marca) and
                self.validar_cor(self.cor) and
                self.validar_ano(self.ano) and
                self.validar_preco(self.preco) and
                self.validar_potencia(self.potencia) and
                self.validar_matricula(self.matricula))

    def editar_info(self):
        print("✏️ Edição de informações do carro")
        while True:
            nova_cor = input(f"Cor atual: {self.cor} ➡️ Nova cor (ENTER para manter): ").strip()
            if not nova_cor:
                break
            if Carro.validar_cor(nova_cor):
                self.cor = nova_cor
                break
            else:
                print(f"❌ Cor inválida. Escolha entre: {', '.join(Carro.lista_cores)}.")


        while True:
            try:
                novo_ano = input(f"Ano atual: {self.ano} ➡️ Novo ano (ENTER para manter): ").strip()
                if not novo_ano:
                    break
                novo_ano = int(novo_ano)
                if 1900 <= novo_ano <= 2025:
                    self.ano = novo_ano
                    break
                else:
                    print("❌ Ano inválido. Deve estar entre 1900 e 2025.")
            except ValueError:
                print("❌ Insira um ano válido (número).")


        while True:
            try:
                novo_preco = input(f"Preço atual: {self.preco}€ ➡️ Novo preço (ENTER para manter): ").strip()
                if not novo_preco:
                    break
                novo_preco = float(novo_preco)
                if novo_preco >= 0:
                    self.preco = novo_preco
                    break
                else:
                    print("❌ Preço inválido. Deve ser um valor positivo.")
            except ValueError:
                print("❌ Insira um valor numérico para o preço.")


        while True:
            try:
                nova_potencia = input(
                    f"Potência atual: {self.potencia} CV ➡️ Nova potência (ENTER para manter): ").strip()
                if not nova_potencia:
                    break
                nova_potencia = int(nova_potencia)
                if nova_potencia > 0:
                    self.potencia = nova_potencia
                    break
                else:
                    print("❌ Potência inválida. Deve ser um número positivo.")
            except ValueError:
                print("❌ Insira um número válido para a potência.")


        while True:
            nova_disp = input(
                f"Disponível atualmente: {'Sim' if self.disponibilidade else 'Não'} (S/N, ENTER para manter): ").strip().lower()
            if not nova_disp:
                break
            if nova_disp in ["s", "n"]:
                self.disponibilidade = (nova_disp == "s")
                break
            else:
                print("❌ Resposta inválida. Introduza 'S' para Sim ou 'N' para Não.")


        while True:
            nova_matricula = input(
                f"Matrícula atual: {self.matricula} ➡️ Nova matrícula (ENTER para manter): ").strip().upper()
            if not nova_matricula:
                break
            if Carro.validar_matricula(nova_matricula):  # Supondo que tens esta função
                self.matricula = nova_matricula
                break
            else:
                print("❌ Matrícula inválida. Introduza uma matrícula válida.")

def obter_marca():
    while True:
        marca = input(f"Marca do Carro ({', '.join(Carro.lista_marcas)}):").strip()
        if Carro.validar_marca(marca):
            return marca
        print(f"❌ Erro: Marca inválida! Escolha entre: {', '.join(Carro.lista_marcas)}.")

def obter_modelo(marca):
    while True:
        modelos_validos = Carro.marcas_modelos.get(marca, [])
        modelo = input(f"Modelo do Carro {modelos_validos}: ").strip()
        if Carro.validar_modelo(marca, modelo):
            return modelo
        print("❌ Modelo inválido. Tente novamente.")


def obter_cor():
    while True:
        cor = input(f"Cor do Carro ({', '.join(Carro.lista_cores)}): ").strip()
        if Carro.validar_cor(cor):
            return cor
        print(f"❌ Erro: Cor inválida! Escolha entre: {', '.join(Carro.lista_cores)}.")

def obter_ano():
    while True:
        try:
            ano = int(input("Ano do Carro: ").strip())
            if Carro.validar_ano(ano):
                return ano
            else:
                print("Erro: O ano deve ser de 1900 a 2025.")
        except ValueError:
            print("❌ Erro: Digite um número inteiro válido.")

def obter_preco():
    while True:
        try:
            preco = float(input("Preço do Carro: ").strip())
            if Carro.validar_preco(preco):
                return preco
            else:
                print("Erro: O preço deve ser maior que zero.")
        except ValueError:
            print("❌ Erro: Digite um valor numérico válido.")

def obter_potencia():
    while True:
        try:
            potencia = int(input("Potência do Carro (CV): ").strip())
            if Carro.validar_potencia(potencia):
                return potencia
            else:
                print("Erro: A potência deve ser um número inteiro positivo.")
        except ValueError:
            print("❌ Erro: Digite um número inteiro válido.")

def obter_disponibilidade():
    while True:
        disponibilidade = input("Disponível? (S para Sim / N para Não): ").strip().lower()
        if disponibilidade in ["s", "n"]:
            return disponibilidade == "s"
        print("❌ Erro: Introduza 'S' para Sim ou 'N' para Não.")

def obter_matricula():
    while True:
        matricula = input("Matrícula (AA-00-AA): ").strip().upper()
        if Carro.validar_matricula(matricula):
            return matricula
        print("❌ Erro: A matrícula deve seguir o formato 'AA-00-AA'.")
