from random import randint
class Artistas():
   def __init__(self,nome,nacionalidade):
      self.nome = nome
      self.nacionalidade = nacionalidade
      self.codigo = __class__.geraCodigo()
      
   def __str__(self):
       return f'O nome do artista é {self.nome} e sua nacionalidade é {self.nacionalidade} o código é: {self.codigo}'
    
   @staticmethod
   def geraCodigo():
      codigo = str(randint(1000,9999))
      return codigo
   
