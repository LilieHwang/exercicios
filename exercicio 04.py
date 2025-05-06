def somar_pares(lista):
    total = 0 
    for i in lista: 
        total += i
 
    media = total / len(lista)
    return media 

numeros [6, 7, 9, 143, 127]

print(somar_pares(numeros))