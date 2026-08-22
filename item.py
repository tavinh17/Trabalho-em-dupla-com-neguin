class Item:
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo
        self.disponivel = True 

    def exibir_informacoes(self):
        return f"Item: {self.titulo} | Código: {self.codigo}"

    def emprestar(self):
         self.disponivel = False 

    def devolver(self):
        self.disponivel = True