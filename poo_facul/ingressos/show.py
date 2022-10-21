from ingressos import Camarote, Ingressos

class Show():
    def __init__(self,artista,dataShow,localShow):
        self.artista = artista
        self.dataShow = dataShow
        self.localShow = localShow
        self.ingressos = []
        self.camarote = []
        self.vendidos = []
        
    def __str__(self):
        return f'O nome do artista é: {self.artista} a data do show é: {self.dataShow} o local do show é: {self.localShow}'
    
    def gerarIngressos(self,quantidade,valor,tipo=0):
        if tipo == 1:
            adicional = input('Digite o valor adicional do camarote: ')
            for i in range(quantidade):
                vip = Camarote(valor,adicional)
                self.camarote.append(vip)
        else: 
            for i in range(quantidade):
                normal = Ingressos(valor)
                self.ingressos.append(normal)
                
    def venderIngresso(self,quantidade,tipo=0):
         valorTotal = 0
         if tipo == 1:
            for i in range(quantidade):
                if len(self.camarote) == 0:
                    print('Ingressos Esgostado')
                    break
                else:
                    valorTotal += self.camarote[i-1].valor
                    self.camarote[i-1].status = 'Vendido'
                    self.vendidos.append(self.camarote.pop(i-1))
            return valorTotal  
         else: 
             for i in range(quantidade):
                 if len(self.ingressos) == 0:
                    print('Ingressos Esgostado')
                    break
                 else:   
                     valorTotal += self.ingressos[i-1].valor
                     self.ingressos[i].status = 'Vendido'
                     self.vendidos.append(self.ingressos.pop(i-1))
             return valorTotal  
    
    def relatorioVendas(self):
        valorTotal = 0
        for i in self.vendidos:
                valorTotal += int(i.valor)
                print(i)
        
        print(f'O valor total das vendas foi: {valorTotal}')
    

