class ItemEmprestado:
    def __init__(self, item):
        self.item = item

    def exibir_item(self):
        return self.item.exibir_informacoes()