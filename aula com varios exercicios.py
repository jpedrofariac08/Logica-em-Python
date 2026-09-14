# PYTHON! #
#adição de 2 variaveis!

print("programa de soma de 2 variaveis!")
a = float (input("insira o numero a:"))
b = float (input("insira o numero b:"))
soma = (a + b)
print("o resultado da soma vale:", soma)

#subtracao de 2 variaveis!

print("programa de subtracao de 2 variaveis!")
a = float (input("insira o numero a:"))
b = float (input("insira o numero b:"))
subtracao = (a - b)
print(print("programa de multiplicacao de 2 variaveis!")

#multiplicacao de 2 variaveis!

a = float (input("insira o numero a:"))
b = float (input("insira o numero b:"))
multiplicacao = (a * b)
print("o resultado da multiplicacao vale:", multiplicacao)"o resultado da subtracao vale:", subtracao)

#divisao de 2 variaveis!

print("programa de divisao de 2 variaveis!")
a = float (input("insira o numero a:"))
b = float (input("insira o numero b:"))
divisao = (a / b)
print("o resultado da divisao vale:", divisao)

#dobro e triplo de um numero!

a = float(input("digite um numero:"))
dobro = (a * 2)
triplo = (a * 3)

print("\no dobro do numero inserido:", dobro)
print("\no triplo do numero inserido:", triplo)

#antecessor e sucessor de um numero!

a = float(input("digite um numero:"))
antecessor = (a - 1)
sucessor = (a + 1)

print('o antecessor do numero inserido é:', antecessor)
print('o sucessor do numero inserido é:', sucessor)

#par ou impar!

a = float(input("escreva um numero:"))
if (a % 2 == 0):
    print(a,"é par!")
else:
    print(a,"é impar!")

#positivo, negativo ou vale 0!

a = float(input("escreva um numero:"))
if (a > 0):
    print(a," é positivo!")
elif (a < 0):
    print(a," é negativo!")
else:
    print(a," vale 0!")

#maior entre dois numeros!

a = float(input("escreva o primeiro numero:"))
b = float(input("escreva o segundo numero:"))
if(a > b):
    print(a, " é maior que ",b)
else:
    print(b," é maior que ", a)

#maior entre tres numeros!

a = float(input("escreva o primeiro numero:"))
b = float(input("escreva o segundo numero:"))
c = float(input("escreva o terceiro numero:"))
if(a > b and a > c):
    print(a," é maior entre os 3 numeros!")
elif(b > a and b > c):
    print(b," é maior entre os 3!")
else:
    print(c," é maior entre os 3!")

#apto para dirigir!

habilitado = str(input("voce é habilitado? "))
if (habilitado == "sim"):
    print("voce esta apto para dirigir!")
else:
    print("voce nao esta apto para dirigir!")

#apto para votar

tituloELEITOR = str(input("voce tem titulo de eleitor? "))
if (tituloELEITOR == "sim"):
    print("voce esta apto para votar!")
else:
    print("voce nao esta apto para votar!")

#desconto para pagamento a vista

tipodepagamento = str(input("qual sera a forma de pagamento? "))
desconto = float
valor = float
valor = 100

if(tipodepagamento == ("a vista")):
    print("o valor do produto a vista com os 10 porcento de desconto sera", valor - (valor *0.10), "reais")
else:
    print("o valor do produto sem os 10 porcento de desconto sera", valor, "reais")

#quem pode votar com true or false!

print("quem pode votar?")

idade = float(input("quantos anos de idade voce tem?"))
tituloELEITOR = (input("voce tem titulo de eleitor?"))

if idade >= 16:
    idade = True
else:
    idade = False
if tituloELEITOR.lower() == "sim" and idade:
    print ("voce pode votar!")
else:
    print("voce não pode votar!")

#quem pode dirigir com true or false!

print("quem pode dirigir")

idade = float(input("quantos anos de idade voce tem?"))
habilitado = (input("voce é habilitado?"))

if idade >= 18:
    idade = True
else:
    idade = False
if habilitado.lower() == "sim" and idade:
    print ("voce pode dirigir!")
else:
    print("voce não pode dirigir!")

#salario for 2000 ou mais, recebe 15% de bonus!

salario = float(input("insira o valor do salario:"))

if salario >= 2000:
    print("o salario total com comissão é:  R$", (salario + (salario * 0.15)))
else:
    print("o salario total sem comissão é:  R$", salario)

#intervalo 10 - 50!

numero = float(input("insira um numero:"))
if(numero >= 10 and numero <= 50):
    print("o numero esta no intervalo!")
else:
    print("o numero nao esta no intervalo!")

#entrada em evento!

idade = float(input("qual a sua idade? "))
ingresso = (input("voce tem ingresso?"))
if (idade >= 18):
    idade = True
else:
    idade = False
if(ingresso.lower() == "sim" and idade):
     print("voce pode entrar!")
else:
    print("voce nao pode entrar!")

#senha correta, quando cadastro = autentificacao!

cadastro = float(input("faça seu cadastro, digite a senha que voce quer ultilizar: "))
print("CADASTRO REALIZADO!")
autentificacao = float(input("agora realize o login, digite a senha cadastrada: "))

if (cadastro == autentificacao):
    print("senha correta, login REALIZADO!")
else:
    print("senha incorreta, login não realizado!")

print("CALCULADORA SIMPLES!")
a = float(input("digite um primeiro numero:"))
b = float(input("digite um segundo numero:"))
conta = input("digite a operação desejada:")
soma = a + b 
subtracao = a - b 
divisao = a / b 
multiplicacao = a * b 

#calculadora simples!

print("CALCULADORA SIMPLES!")
a = float(input("digite um primeiro numero:"))
b = float(input("digite um segundo numero:"))
conta = input("digite a operação desejada:")
soma = a + b 
subtracao = a - b 
divisao = a / b 
multiplicacao = a * b 

if (conta == "+"):
    print("o resultado da operação é: ", soma)
elif (conta == "-"):
    print("o resultado da operação é: ", subtracao)
elif (conta == "/"):
    if(a!=0 and b!=0):
        print("o resultado da operação é: ", divisao) 
    else:
        print("operação invalida!")
elif (conta == "*"):
    print("o resultado da operação é: ", multiplicacao) 
else:
    print("operação invalida!")

#praticar esportes 12-18 anos + autorização!

print("praticar esportes 12-18 anos + autorização!")
idade = float(input("qual a sua idade? "))
if (idade >=12 and idade <= 18):
    autorizacao = input("voce tem autorizacao?")
if autorizacao == "sim":
    print("voce pode praticar esportes!")
else:
    print("voce não pode praticar esportes!")

#praticar esportes 12-18 anos + autorização.v2!

print("Praticar esportes 12-18 anos + autorização!")

idade = int(input("Qual a sua idade? "))

idadevalida = idade >= 12 and idade <= 18

autorizacao = input("Você tem autorização? ").lower()

if autorizacao == "sim":
    autorizacao_valida = True
else:
    autorizacao_valida = False

if idadevalida and autorizacao_valida:
    print("Você pode praticar esportes!")
else:
    print("Você não pode praticar!")

#esta chovendo?

chuva = input("esta chovendo? ")
print("-----------^------------")
if chuva =="sim":
    chuva = True
if chuva == True:
    print("voce nao pode sair de casa, se nao vai se molhar!")
else:
    print("pode sair de casa e ir jogar um futebol!")

#opções de pagamento!

print("----------MENU DE PAGAMENTO----------")
print("-dinheiro\n-credito\n-debito\n-pix\n-boleto")
forma_pagamento = input("qual sera sua forma de pagamento? ")

if forma_pagamento == "dinheiro":
    print("Você escolheu dinheiro.")
elif forma_pagamento == "credito":
    print("Você escolheu crédito.")
elif forma_pagamento == "debito":
    print("Você escolheu débito.")
elif forma_pagamento == "pix":
    print("Você escolheu Pix.")
elif forma_pagamento == "boleto":
    print("Você escolheu boleto.")
else:
    print("Opção inválida.")

#Desconto a partir de 100(10%), 300(15%), 500(20%)

valor_da_compra = float(input("o valor  da compra foi:"))
if (valor_da_compra >= 100 and valor_da_compra < 300):
    print("o valor total da compra com desconto foi:R$", valor_da_compra -(valor_da_compra * 0.10))
elif (valor_da_compra >= 300 and valor_da_compra < 500):
    print("o valor total da compra com desconto foi:R$", valor_da_compra -(valor_da_compra * 0.15))
elif (valor_da_compra >= 500):
    print("o valor total da compra com desconto foi:R$", valor_da_compra -(valor_da_compra * 0.20))
else:
    print("sua compra nao tem desconto, logo o valor da compra fica:R$", valor_da_compra)

#classificação do triangulo!

print("Classificação do triângulo: equilátero, isósceles e escaleno")
lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))

if lado1 == lado2 and lado1 == lado3:
  print("É um triângulo equilátero!")
elif (lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2) or (lado2 == lado3 and lado2 != lado1):
  print("É um triângulo isósceles!")
else:
  print("É um triângulo escaleno!")

#classificação de fase da vida de acordo com a idade!

print("Classificação de fase da vida: criança, adulto e idoso")
idade = float(input("qual é a sua idade?"))

if idade > 0 and idade < 18:
    print("voce e uma crianca!")
elif idade >= 18 and idade < 60:
    print("voce e adulto!")
elif idade >= 60:
    print("voce e idoso")
else:
    print("idade invalida digite novamente")

#menu de pagamento V2!

print("---ESCOLHA DE PAGAMENTO---")

def main ():

  print("1 - Dinheiro")
  print("2 - Cartão de Crédito")
  print("3 - Cartão de Débito")
  print("4 - PIX")
  print("5 - Boleto")

  opcao = int (input ("Escolha a forma de pagamento: "))

  pagamento = escolhapagamento (opcao)

  print("Forma de pagamento escolhido: ",pagamento)

def escolhapagamento (opcao):

  match opcao:
    case 1:
      return "Dinheiro"
    case 2:
      return "Cartão de Crédito"
    case 3:
      return "Cartão de Débito"
    case 4:
      return "PIX"
    case 5:
      return "Boleto"
    case 6:
      return "Opção inválida"
  
main()

#desconto progressivo V2!

print("---DESCONTO DA COMPRA---")

def main():

  valor_da_compra = float(input("O valor da compra foi: R$ "))

  valor_total = escolha_desconto(valor_da_compra)

  print("O valor total da compra foi: R$", valor_total)

def escolha_desconto(valor_da_compra):

  if valor_da_compra >= 100 and valor_da_compra < 300:
    return valor_da_compra - (valor_da_compra * 0.10)
  elif valor_da_compra >= 300 and valor_da_compra < 500:
    return valor_da_compra - (valor_da_compra * 0.15)
  elif valor_da_compra >= 500:
    return valor_da_compra - (valor_da_compra * 0.20)
  else:
    return valor_da_compra

main()
