from random import randint

class Produto():
    def __init__(self,nome,marca,qtd_arma,preco):
        self._nome = nome
        self._marca = marca
        self._qtd_arma = qtd_arma
        self._preco = preco
        self._codgio = __class__.gerar_codigo()
    
    def __str__(self):
        return f'Nome: {self.nome}, Marca: {self.marca} Quatidade armazenada: {self.qtd_arma}, Preço: {self.preco}, Códdigo: {self.codigo}'

    @property
    def nome(self):
            return self._nome

    @nome.setter
    def nome(self,nome):
            self._nome = nome

    @property
    def marca(self):
            return self._marca

    @marca.setter
    def marca(self,marca):
            self._marca = marca

    @property
    def qtd_arma(self):
            return self._qtd_arma

    @qtd_arma.setter
    def qtd_arma(self,qtd_arma):
            self._qtd_arma = qtd_arma

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self,preco):
        self._qtd_arma = preco

    @property
    def codigo(self):
        return self._codgio


    @staticmethod
    def gerar_codigo():
        codigo = str(randint(1000,90000))
        return  codigo

    def retirar_estoque(self,quantidade):
        aux= 0
        for i in range(quantidade):
            
            if self.qtd_arma != 0:
                self.qtd_arma -= 1
            else:
                break
            aux += 1
        return aux

    def inserir_estoque(self,quantidade):
        self.qtd_arma += quantidade

