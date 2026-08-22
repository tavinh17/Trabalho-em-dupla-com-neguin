from item import Item

class Livro(Item):
    def __init__(self, codigo, titulo, autor):
        super().__init__(codigo, titulo)
        self.autor = autor 

    def exibir_informacoes(self):
        return f"Livro | Código: {self.codigo} | Título: {self.titulo}  | Autor: {self.autor}"

