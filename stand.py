class Stand:
    def __init__(self, nome, localizacao, contato):
        """Construtor para inicializar os atributos do Stand."""
        if not nome.strip():
            raise ValueError("O nome do stand é obrigatório.")
        if not localizacao.strip():
            raise ValueError("A localização do stand é obrigatória.")

        # Verifica se o contato possui 9 dígitos, como é o caso de números em Portugal
        if not str(contato).isdigit() or len(str(contato)) != 9:
            raise ValueError("O contato deve ser um número válido de telefone português com 9 dígitos.")

        self.nome = nome
        self.localizacao = localizacao
        self.contato = str(contato)  # Garantir que o contato seja uma string com 9 dígitos

    def __str__(self):
        """Retorna uma representação em string da instância."""
        return f"Stand: {self.nome}, Localização: {self.localizacao}, Contato: {self.contato}"

    @staticmethod
    def from_string(data_str):
        """Cria uma instância de Stand a partir de uma string CSV."""
        try:
            nome, localizacao, contato = data_str.strip().split(", ")
            return Stand(nome, localizacao, int(contato))
        except ValueError:
            print("Erro ao converter string para Stand. Verifique o formato correto.")
            return None

    def get_info(self):
        """Retorna um dicionário com as informações do stand."""
        return {
            "nome": self.nome,
            "localizacao": self.localizacao,
            "contato": self.contato
        }
