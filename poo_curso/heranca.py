class Animal():
    def __init__(self,nome,comprimento,num_patas,cor,ambiente,velocidade):
        self.nome = nome
        self.comprimento = comprimento
        self.num_patas = num_patas
        self.cor = cor
        self.ambiente = ambiente
        self.velocidade = velocidade

    def dados(self):
        print(f'O nome do animal é {self.nome} o comprimento {self.comprimento} o número de patas é {self.num_patas} a cor é {self.cor} e vive no ambiente {self.ambiente} e a velocidade é {self.velocidade}') 

    
class Mamifero(Animal):
    def __init__(self, nome, comprimento, num_patas, cor, ambiente, velocidade,alimento):
        super().__init__(nome, comprimento, num_patas, cor, ambiente, velocidade)
        self.alimento = alimento
    
    def dadosMamifero(self):
        super().dados()
        print('Alimento: {}'.format(self.alimento))

class Peixe(Animal):
    def __init__(self, nome, comprimento, num_patas, cor, ambiente, velocidade,caracteristica):
        super().__init__(nome, comprimento, num_patas, cor, ambiente, velocidade)
        self.caracteristica = caracteristica

    def dadosPeixe(self):
        super().dados()
        print('Alimento: {}'.format(self.caracteristica))

