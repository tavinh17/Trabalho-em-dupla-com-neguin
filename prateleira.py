class Prateleira:
    def __init__(self, numero, localizacao):
        self.numero = numero
        self.localizacao = localizacao
        self.itens = []

    def adicionar_item(self, item):
        self.itens.appened(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)

        def listar_itens(self):
            if not self.itens:
                return "A pratileira está vazia."

        resultado = f"Prateleira {self.numero} - {self.localizacao}:\n"

        for item in self.itens:
            resultado += f"- {item.exibir_informacoes()}\n"

        return resultado