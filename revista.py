from item import Item

class Revista(Item):
    def __init__(self, codigo, titulo, edicao):
        super().__init__(codigo, titulo)
        self.edicao = edicao 

    def exibir_informacoes(self):
        return f"Revista | Código: {self.codigo} | Título: {self.titulo} | Ediçãoe: {self.edicao}"