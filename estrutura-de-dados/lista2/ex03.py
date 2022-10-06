nota = []
for i in range(1,6):
    qual = int(input(f"Digite qual a nota da qualidade da proposta {i}: "))
    prec = int(input(f"Digite qual a nota do preço da proposta {i}: "))
    praz = int(input(f"Digite qual a nota do prazo da proposta {i}: "))
    
    if qual < 7:
        notaGeral = 0
    
    if qual >= 7 and prec >=7:
        notaGeral = (qual + prec + praz) / 3
    
    if qual >= 7 and prec <=7:
        notaGeral = (qual + (2 * prec) + praz) / 4
    
    nota.append(notaGeral) 
    notaGanh = max(nota)
    
print(f"O ganhador foi a proposta de número {nota.index(notaGanh) + 1} com a nota maxíma de {notaGanh}")