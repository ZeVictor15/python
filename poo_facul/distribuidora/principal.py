from datetime import date
from produto import Produto
from perecivel import ProdutoPerecivel
from distribuidora import Distribuidor

p1=Produto('detergente', 'Ypê',10,2.48)
print(p1)
print('Quantidade retirada: ', p1.retirar_estoque(8))
print(p1)
print('Quantidade retirada: ', p1.retirar_estoque(5))
print(p1)
p2=ProdutoPerecivel('arroz', 'Sepé',10,3.69,'05/11/2022')
print(p2)
print('Quantidade retirada: ', p2.retirar_estoque(4,date.today()))
print(p2)
p2.inserir_estoque(12)
print(p2)
d1=Distribuidor('JP',1)
d1.cadastrar_produto(p1)
d1.cadastrar_produto(p1)
d1.cadastrar_produto(p2)
d1.listar_produtos()