

def cadastrar_filmes(nome, descricao, classificacao, categoria01, caterogia02, categoria03):
    filmes = []

    filme = {
        "nome": nome,
        "descricao": descricao,
        "classificacao": classificacao, 
        "categoria": [categoria01, caterogia02, categoria03]
    } 

    filmes.append(filme)
    return (filmes)

print(cadastrar_filmes("Como Treinar O Seu Dragão", "Um jovem Viking encontra um dragão cruel e descobre a verdade sobre eles", "Livre", "aventura", "infantil", "ação"))