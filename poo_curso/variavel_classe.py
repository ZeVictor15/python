class Variavel:
    variavel_clase = 23
    
    def __init__(self):
        self.variavel_clase = 45
    
v1 = Variavel()
v2 = Variavel()

v1.variavel_clase = 321

print(v1.__dict__)
print(v2.__dict__)
print(Variavel.__dict__)

print(v1.variavel_clase)
print(v2.variavel_clase)
print(Variavel.variavel_clase)