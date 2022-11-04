from random import randint
from datetime import date

class Curso:
    def __init__(self,nome,descricao):
        self.codigo = __class__.gerar_codigo()
        self.nome = nome
        self.descricao = descricao
        self._coordenador = None
        self._docentes = []
    
    def __str__(self):
        return f'Codigo: {self.codigo}, Nome: {self.nome}, Descrição: {self.descricao}, Coordenador: {self.coordenador}, Docentes: {self.docentes}'
    
    @property
    def coordenador(self):
        return self._coordenador    

    @coordenador.setter
    def coordenador(self,professor):
        self._coordenador = professor
    
    @property
    def docentes(self):
        return self._docentes
    
    @docentes.setter
    def docentes(self,docente):
        self._docentes.append(docente)
    
    @staticmethod
    def gerar_codigo():
        codigo = str(randint(1000,9000))
        return codigo

        
class Aluno:
    def __init__(self,nome,cpf,email):
        self.matricula = __class__.gerar_codigo()
        self.nome = nome
        self._cpf = cpf
        self.email = email
        self.cursos = None
    
    def __str__(self):
        return f'Matricula: {self.matricula}, Nome: {self.nome}, CPF: {self.cpf}, E-mail: {self.email}, Cursos: {self.cursos}'
    
    @property
    def cpf(self):
        return self._cpf
    
    def matricular(self,cursos):
        self.cursos = cursos 
        
    @staticmethod
    def gerar_codigo():
        codigo = str(randint(1000,9000))
        return codigo
        
class Professor:
    def __init__(self,nome,cpf,email):
        self.nome = nome
        self._cpf = cpf
        self.email = email
        self.lotacao = None
        self.matricula = __class__.gerar_codigo()
        self.admissao  = __class__.data_admisão()
    
    def __str__(self):
        return f'Matricula: {self.matricula}, Nome: {self.nome}, CPF: {self.cpf}, E-mail: {self.email}, Cursos: {self.cursos}, Data de Admissão: {self.admissao}'
    
    @property
    def cpf(self):
        return self._cpf
    
    @staticmethod
    def gerar_codigo():
        codigo = str(randint(1000,9000))
        return codigo  
    
    @staticmethod
    def data_admisão():
        data = date.today()
        return data 
    
    def set_lotacao(self,lotacao):
        self.lotacao = lotacao