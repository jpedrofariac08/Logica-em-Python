print("boletim de notas")
nome = input ("insira o nome do aluno:")
disciplina = input ("insira o nome da disciplina:")
nota = float (input("nota obtida:"))

if nota >= 60:
    print ("esta aprovado!")

if nota >39 and nota <60:

    print ("esta de recuperação!")

if nota >0 and nota <40:

    print ("esta reprovado!")
