from random import randint
class Artistas():
   def __init__(self,nome,nacionalidade):
      self.nome = nome
      self.nacionalidade = nacionalidade
      self.codigo = __class__.geraCodigo()
      
   def __str__(self) -> str:
       pass
    
   @staticmethod
   def geraCodigo():
      codigo = str(randint(1000,9999))
      return codigo
   
a = Artistas('victor','brasileiro')
print(a.codigo)