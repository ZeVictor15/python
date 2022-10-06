from http import client
from associacao import Escritor
from associacao import Caneta
from associacao import MaquinaDeEscrever

from agregação import CarrinhoDeCompras, Produto

from composicao import Cliente, Endereco

'''
escritor = Escritor('Victor')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# Associação de classes
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
# print(escritor)
print(caneta.marca)
maquina.escrever()

'''
# Agregação de classes

'''
carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Celular', 1000)
p3 = Produto('PC', 2000)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produtos()
print(carrinho.soma_total())

'''

cliente1 = Cliente('Victor', 23)
cliente1.insere_indereco('Aracaju', 'SE')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()


cliente2 = Cliente('José', 32)
cliente2.insere_indereco('Salvador','BA')
cliente2.insere_indereco('Rio de Janeiro','RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('Vitoria',13)
cliente3.insere_indereco('Florianopolis', 'SC')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

print('#############################################')