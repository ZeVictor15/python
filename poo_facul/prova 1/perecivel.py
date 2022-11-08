import datetime
from produto import Produto
from datetime import *

class ProdutoPerecivel(Produto):
    def __init__(self, nome, marca, qtd_arma, preco,data_validade):
        super().__init__(nome, marca, qtd_arma, preco)
        self._data_validade = data_validade

    def __str__(self):
         var_super = super().__str__()
         return  var_super + f' Data validade:  {self.data_validade}'

    @property
    def data_validade(self):
        return self._data_validade

    @data_validade.setter
    def data_validade(self,nova_data):
        self._data_validade = nova_data

    def retirar_estoque(self, quantidade,data_validade):
        super().retirar_estoque(quantidade)
        data = datetime.strptime(self.data_validade, '%d/%m/%Y').date()
        if data == data_validade or data_validade >= data:
            print('Produtos acima da data de validade estoque zerado')
            self.qtd_arma = 0
            return 0
    
    def inserir_estoque(self, quantidade):
        if self.qtd_arma == 0:
            nova_data = input('Digite a nova data de validade: ')
            self.data_validade = nova_data
            super().inserir_estoque(quantidade)
        else:
            print('Não foi possivel cadastrar estoque cheio')
        
       



