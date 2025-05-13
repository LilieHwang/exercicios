def somar_pares(lista):
    total = 0 
    for i in lista: 
            total += i
    return total 

numeros = [1, 2, 6, 18, 12, 20]

print(somar_pares(numeros))