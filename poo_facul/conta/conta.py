from random import randint

class Conta():
    def __init__(self,nome):
        self._nome = nome
        self._numero_conta = __class__.gerar_num_conta()
        self._total = 0
    
    def __str__(self):
        return f'Nome: {self.nome}, Numero da Conta: {self.numero_conta}, Saldo: {self.total}'
     
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    
    @property
    def numero_conta(self):
        return self._numero_conta
    
    @numero_conta.setter
    def numero(self,numero_conta):
        self._numero_conta = numero_conta
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self,valor):
        self._total = valor
     
    def sacar(self,valor):
        if self.total == 0:
            print('Conta não possui saldo')
        elif valor > self.total:
            print(f'Saldo insuficiente. saldo disponivel: {self.total}')
        elif valor <= self.total:
            self.total -= valor
            print(f'Saque realizado com sucesso. saldo disponivel: {self.total}')
    
    def depositar(self,valor):
        self.total += valor

    @staticmethod
    def gerar_num_conta():
        numero = str(randint(10000,90000))    
        return numero

class ContaPoupanca(Conta):
    def __init__(self, nome,dia_rendimento):
        super().__init__(nome)
        self._dia_rendimento = dia_rendimento    
    
    @property
    def dia_rendimento(self):
        return self._dia_rendimento
    
    @dia_rendimento.setter
    def dia_rendimento(self,dia_rendimento):
        self.dia_rendimento = dia_rendimento
        
    def calcular_saldo(self,taxa_rendimento):
        pass
    
class ContaEspecial(Conta):
    def __init__(self,nome,limite):
      super().__init__(nome)
      self._limite = limite 
      self.total += self.limite  
    
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self,limite):
        self._limite = limite
        
    def sacar_especial(self,valor):
        if self.total == 0:
            print('Conta não possui saldo')
        elif valor > self.total:
            print(f'Saldo insuficiente. saldo disponivel: {self.total}')
        elif valor <= self.total:
            self.total -= valor
            print(f'Saque realizado com sucesso. saldo disponivel: {self.total}')