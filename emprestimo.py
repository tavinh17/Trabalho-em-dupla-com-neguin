from item_emprestado import ItemEmprestado

class Emprestimo:
    def __init__(self, codigo, data_emprestimo):
        self.codigo = codigo 
        self.data_emprestimo  = data_emprestimo
        self.devolucao = None
        self.iten = []

    def adicionar_item(self, item):
        item_emprestado = ItemEmprestado(item)
        self.itens.appened(item_emprestado)

    def finalizar(self,data_devolucao):
        self.data_devolucao = data_devolucao

    def listar_itens(self):
        if not self.itens:
            return "Nenhum item neste empréstimo."

        resultado = f"Itens do empréstimo #{self.codigo}:\n"

        for item_emprestado in self.itens:
            resultado += f"- {item_emprestado.exibir_item()}:\n"

        return resultado 
