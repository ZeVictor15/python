from pessoa import Pessoa

p1 = Pessoa('José',32)
p2 = Pessoa('Victor', 23)

'''
p1.comer('Pizza')
p1.parar_comer()
p1.falar('POO')
p1.parar_falar()
p1.parar_comer()
p1.falar('POO')
p1.comer('Pizza')
'''

'''
p2.comer('Pizza')
p2.falar('POO')
p2.parar_comer()
p2.falar('POO')
p2.comer('Pizza')
p2.falar('Python')
'''

p1 = Pessoa.por_ano_nascimento('Victor', 2000)
print(p1.nome,p1.idade)
print(p1.get_ano_nascimento())
print(Pessoa.gerar_id())