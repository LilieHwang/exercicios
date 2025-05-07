def cadastrar_filme(nome, descricao, classificacao, categoria01, caterogia02, categoria03):
    filmes = []

    filme = {
        "nome": nome,
        "descricao": descricao,
        "classificacao": classificacao, 
        "categoria": {categoria01, caterogia02, categoria03}
    } 

    filmes.append(filme)
    return filme

print(cadastrar_filme("Como Treinar O Seu Dragão, Um jovem Viking encontra um dragão cruel e descobre a verdade sobre eles, Livre, aventura, infantil, ação "))