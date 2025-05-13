from exercicio_04 import calcular_media 

alunos = []

def obter_dados_aluno():
    nome_aluno = input("informe o nome completo do aluno: ")
    email_aluno = input("informe o email do aluno: ")
    serie_aluno = input("informe a serie do aluno: ")
    nota01_aluno = int(input("informe a primeira nota do aluno: "))
    nota02_aluno = int(input("informe a segunda nota do aluno: "))
    nota03_aluno = int(input("informe a terceira nota do aluno: "))

    return cadastrar_aluno(nome_aluno, email_aluno, serie_aluno, nota01_aluno, nota02_aluno, nota03_aluno)

def cadastrar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):

    nota = [nota01, nota02, nota03]

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
    for aluno in dados_alunos:
        print(f"Nome do Aluno: {aluno["nome"]} | Email do Aluno: {aluno["email"]}) | Série do aluno: {aluno["serie"]} | Notas do aluno: {aluno["notas"]} | Média do aluno: {aluno["media"]}")

    return 

def iniciar_sistema():
    while True: 
        print("="*80)
        print("Opção 1 => mostrar alunos cadastrados")
        print("Opção 2 => Cadastrar alunos.")
        print("Opção 3 => Sair do sistema.")
        print("="*80)

        opcao = input("Escolha uma das opcões acima: ")

        if opcao == "1":
            mostrar_dados_alunos(alunos)
        elif opcao == "2":
            obter_dados_aluno()
        else: 
            print("sistema finalizado.")
            break
            
iniciar_sistema()