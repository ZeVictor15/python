class Galeria:
    def __init__(self,nome,telefone,nomeResp):
        self.nome = nome
        self.telefone = telefone
        self.nomeResp = nomeResp
        self.obra = []
    
    def __str__(self):
        return f'Nome da galeria: {self.nome} telefone: {self.telefone} nome do respónsavel: {self.nomeResp}'
    
    def cadastrarObras(self,obra):
        if obra.autor == None:
            print('Autor não Cadastrado, é necessario cadastra o autor')
        else:
            print('Obra cadastrada com sucesso')
            self.obra.append(obra)
        
    def cadastrarPintu(self,pintura):
        if pintura.autor == None:
            print('Autor não Cadastrado, é necessario cadastra o autor')
        else:
            print('Obra cadastrada com sucesso')
            self.obra.append(pintura)
    
    def cadastrarEscul(self,escultura):
        if escultura.autor == None:
            print('Autor não Cadastrado, é necessario cadastra o autor')
        else:
            print('Obra cadastrada com sucesso')
            self.obra.append(escultura)

    def pesquisarObras(self,nome):
        for i in self.obra:
            if i.autor.nome == nome:
                print(f'{i}\n')

    def pesquisarArtis(self,artistas):
        for i in self.obra:
            if i.autor.nome == artistas:
                print(f'{i.autor}\n')
                break
    
    def pesquisarCodig(self,codigo):
        for i in self.obra:
            if i.codigo == codigo:
                print(i)
    
    def imprimirObras(self):
        for i in self.obra:
            print(f'{i}\n')
