from contato import *
class Agenda():
    def __init__(self):
        self.contatos = []
        
    def pesquisar_nome(self,nome):
        for i in self.contatos:
            if i.nome == nome:
                str(print(i))
    
    def alterar_contato(self,nome):
        for i in self.contatos:
            if i == nome:
                i.nome = nome
    
    def add_contato(self,contato):
        self.contatos.append(contato)
        
