import re

# Classe para Stand
class Stand:
    # Regex para validar o email e contato
    regex_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    regex_contato = r"^9\d{8}$"

    lista_localizacoes = ["Lisboa", "Porto", "Coimbra", "Faro", "Braga", "Setúbal"]

    def __init__(self, nome, localizacao, contato, email, password):
        self.nome = nome
        self.localizacao = localizacao
        self.contato = contato
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.nome}; {self.localizacao}; {self.contato}; {self.email}; {self.password}"

    @staticmethod
    def validar_nome(nome):
        return bool(nome.strip()) and len(nome.strip()) >= 3

    @staticmethod
    def validar_localizacao(localizacao):
        return localizacao in Stand.lista_localizacoes

    @staticmethod
    def validar_contato(contato):
        return re.match(Stand.regex_contato, contato) is not None

    @staticmethod
    def validar_email(email):
        return re.match(Stand.regex_email, email) is not None

    @staticmethod
    def validar_password(password):
        return isinstance(password, str) and len(password) >= 6

    def is_valid(self):
        return (self.validar_nome(self.nome) and
                self.validar_localizacao(self.localizacao) and
                self.validar_contato(self.contato) and
                self.validar_email(self.email) and
                self.validar_password(self.password))

    def editar_info(self):
        print("✏️ Edição de informações do stand")

        while True:
            novo_nome = input(f"Nome atual: {self.nome} ➡️ Novo nome (ENTER para manter): ").strip()
            if not novo_nome:
                break
            if Stand.validar_nome(novo_nome):
                self.nome = novo_nome
                break
            else:
                print("❌ Nome inválido. O nome não pode estar vazio.")

        while True:
            nova_localizacao = input(
                f"Localização atual: {self.localizacao} ➡️ Nova localização (ENTER para manter): ").strip()
            if not nova_localizacao:
                break
            if self.validar_localizacao(nova_localizacao):
                self.localizacao = nova_localizacao
                break
            else:
                print(f"❌ Localização inválida. Escolha entre: {', '.join(self.lista_localizacoes)}.")

        while True:
            novo_contato = input(f"Contato atual: {self.contato} ➡️ Novo contato (ENTER para manter): ").strip()
            if not novo_contato:
                break
            if Stand.validar_contato(novo_contato):
                self.contato = novo_contato
                break
            else:
                print("❌ Contato inválido. Deve começar com '9' e ter 9 dígitos.")

        while True:
            novo_email = input(f"Email atual: {self.email} ➡️ Novo email (ENTER para manter): ").strip()
            if not novo_email:
                break
            if Stand.validar_email(novo_email):
                self.email = novo_email
                break
            else:
                print("❌ Email inválido. Introduza um email válido.")


def obter_nome_stand():
    while True:
        nome = input("Nome do Stand (mín: 3 caracteres): ").strip()
        if Stand.validar_nome(nome):
            return nome
        print("❌ Erro: O nome não pode estar vazio e deve ter pelo menos 3 caracteres.")

def obter_localizacao_stand():
    while True:
        localizacao = input(f"Localização do Stand ({', '.join(Stand.lista_localizacoes)}): ").strip()
        if Stand.validar_localizacao(localizacao):
            return localizacao
        print(f"❌ Erro: Localização inválida! Escolha entre: {', '.join(Stand.lista_localizacoes)}.")

def obter_contato_stand():
    while True:
        contato = input("Contato do Stand (9 dígitos, começando com 9): ").strip()
        if not contato.isdigit():
            print("❌ Erro: O contato deve conter apenas dígitos.")
        elif len(contato) != 9:
            print("❌ Erro: O contato deve ter exatamente 9 dígitos.")
        elif not Stand.validar_contato(contato):
            print("❌ Erro: O contato deve começar com '9' e ter 9 dígitos.")
        else:
            return contato

def obter_email_stand():
    while True:
        email = input("Email do Stand: ").strip()
        if Stand.validar_email(email):
            return email
        print("❌ Erro: Introduza um email válido.")

def obter_password_stand():
    while True:
        password = input("Password do Stand (mínimo 6 caracteres): ").strip()
        if Stand.validar_password(password):
            return password
        print("❌ Erro: A password deve ter pelo menos 6 caracteres.")
