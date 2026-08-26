class Usuario:
    def __init__(self, id_usuario, nome, email,):      
        self.id_usuario = id_usuario
        self.nome = nome 
        self.email = email
        self.emprestimos = []


    def realizar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def listar_emprestimos(self, emprestimo):
        if not self.emprestimo:
            return  "O usuário {self.nome} não possui empréstimos."

        resultado = f"Empréstimos de {self.nome}:\n"

        for emprestimo in self.emprestimos:
            resultado += f"- Empréstimo #{emprestimo.codigo}\n"

        return resultado