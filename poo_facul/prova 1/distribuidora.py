class Distribuidor():
    def __init__(self,nome,numero):
        self._nome = nome
        self._numero = numero
        self._produtos = []

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self,numero):
        self._numero = numero

    @property
    def produtos(self):
        return self._produtos

    @produtos.setter
    def produtos(self,produto):
        self._produtos.append(produto)

    
    def buscar_produto(self,nome):
        for i in self.produtos:
            if i.nome == nome:
                return i.nome
            else:
                return None

    def cadastrar_produto(self,produto):
        if self.buscar_produto(produto.nome) == None:
            self.produtos = produto
            print('Produto cadastrado!!!!')
        else:
            print(f'Produto ja está cadastrado: {produto}')

    def listar_produtos(self):
        for i in self.produtos:
            print(i)

