class Prateleira:

    def __init__(self, numero, localizacao):
        self.numero = numero
        self.localizacao = localizacao
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def listar_itens(self):
        if not self.itens:
            return "Prateleira vazia."

        texto = f"Prateleira {self.numero} - {self.localizacao}\n"

        for item in self.itens:
            texto += f"- {item.titulo}\n"

        return texto