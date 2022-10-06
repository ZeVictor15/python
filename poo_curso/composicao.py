class Cliente:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []
    
    def insere_indereco(self,cidade,estado):
        self.endereco.append(Endereco(cidade,estado))
        
    def lista_enderecos(self):
        for i in self.endereco:
            print(i.cidade, i.estado)
            
    def __del__(self):
        print(f'{self.nome} FOI APAGADO!!!!!')
        
class Endereco:
    def __init__(self,cidade,estado):
        self.cidade = cidade
        self.estado = estado
    
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO!!!!!')  