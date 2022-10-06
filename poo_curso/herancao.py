class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade  
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeClasse} Falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeClasse} Comprando...')

class Aluno(Pessoa): 
    def estudar(self):
        print(f'{self.nomeClasse} Estudando...')

a1 = Aluno('Victor', 23)
print(a1.nome)
a1.falar()
a1.estudar()

c1 = Cliente('José', 32)
print(c1.nome)
c1.falar()
c1.comprar()