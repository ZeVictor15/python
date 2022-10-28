class Contato():
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
        self.telefone = []
    
    def __str__(self):
        return f'o nome é:  {self.nome} o email é: {self.email} o telefone é: {self.telefone}'
    
    def alterar_email(self,email):
        self.email = email
        
    def add_telefone(self,ddd,numero,descricao):
        self.telefone.append(Telefone(ddd,numero,descricao))
        
    def alterar_nome(self,nome):
        self.nome = nome
    
class Telefone():
    def __init__(self,ddd,numero,descicao):
        self.ddd = ddd
        self.numero = numero
        self.descricao = descicao
        
    def alterar_numero(self,numero):
        self.numero = numero
        
