class Curso:
    def __init__(self,codigo,nome,descricao,coordenador,docentes):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.coordenador = Professor
        self.docentes = Professor
    
    def definir_coordenador(self,cordenador):
        self.coordenador = Professor
    
    def add_docente(self,professor):
        self.professor = Professor
        
class Aluno:
    def __init__(self,matricula,nome,cpf,email,cursos):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.cursos = Curso 
    
    def matricular(self,cursos):
        self.cursos = Curso 
        
    def imprimir(self):
        print(f"Aluno matriculado no curso {self.cursos}")
        
class Professor:
    def __init__(self,matricula,nome,cpf,admissao,email,lotacao):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.admissao = admissao
        self.email = email
        self.lotacao = Curso
        
    def set_lotacao(self,lotacao):
        self.lotacao = Curso
        
    def imprimir():
        pass
        
        