def verificar_idade(nome, idade): 
    if idade >= 118:
        return f"{nome} é maior de idade."
    else:
        return f"{nome} é menor de idade."
    
print(verificar_idade("Lilie", 16))