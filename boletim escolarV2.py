print ("BOLETIM ESCOLAR")
nome = input ("nome:")
curso = input ("curso:")
semestre = input ("semestre:")
materia = input ("materia:")
nota1 = float (input("nota1:"))
nota2 = float (input("nota2:"))
media = ((nota1 + nota2)/2)

print ("\nNome:", nome)
print ("\nCurso:", curso)
print ("\nSemestre:", semestre)
print ("\nMateria:", materia)
print ("\nMedia:", media)
if media >=60:{
print ("aprovado!")
}
if media >=49 and media <60:{
    print ("esta de recuperação!")
}
elif media <49:{
    print ("reprovado!")
}