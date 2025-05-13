from exercicio_04 import calcular_media 

alunos = []

def obter_dados_aluno():
    nome_aluno = input("informe o nome completo do aluno: ")
    email_aluno = input("informe o email do aluno: ")
    serie_aluno = input("informe a serie do aluno: ")
    nota01_aluno = int(input("informe a primeira nota do aluno: "))
    nota02_aluno = int(input("informe a segunda nota do aluno: "))
    nota033_aluno = int(input("informe a terceira nota do aluno: "))

def cadastrar_aluno(nome, email, serie, nota_01=0, nota_02=0, nota_03=0):

    nota = [nota_01, nota_02, nota_03]

    aluno = {
       "nome": nome, 
       "email": email,
       "serie": serie,
       "nota": nota,
       "media": calcular_media(nota),
    }
    alunos.append(aluno)
   
    return aluno

def mostrar_dados_alunos(dados_alunos):
    return print(dados_alunos)

mostrar_dados_alunos(alunos)