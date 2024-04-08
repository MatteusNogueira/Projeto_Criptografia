import math
import random


def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1


def mod(n1, n2):
    n5 = n2
    n3 = 0
    n4 = 1

    while n1 > 1:
        divis = n1 // n2
        n2, n1 = n1 % n2, n2
        n3, n4 = n4 - divis * n3, n3
    return n4 + n5 if n4 < 0 else n4

def gerandoNumeros():
    validacao = True
    while validacao:
        divi = 0
        contador = 1
        num = random.getrandbits(8)
        while contador <= num:
            if num % contador == 0:

                divi += 1
            contador += 1
        if divi == 2:
            validacao = False
    return num

def criptografar(chvPublica, mensagem):
    chvPrinc, publi = chvPublica
    mensagem_encript = [str(pow(ord(char), publi, chvPrinc)) for char in mensagem]
    mensagem_encript_texto = ' '.join(mensagem_encript)
    return mensagem_encript_texto

def descriptar(chvPriva, mensagem_encript):
    chvPrinc, priva = chvPriva
    mensagem_encript = mensagem_encript.split()
    texto = [chr(pow(int(char), priva, chvPrinc)) for char in mensagem_encript]
    mensagem_decriptada = ''.join(texto)
    return mensagem_decriptada

def criarChvs():
  num1 = gerandoNumeros()
  num2 = gerandoNumeros()
  chvPrinc = num1 * num2
  chvValida = (num1 - 1) * (num2 - 1)

  publi = random.randrange(31, chvValida)
  while gcd(publi, chvValida) != 1:
      publi = random.randrange(31, chvValida)

  # Calculando priva
  priva = mod(publi, chvValida)

  # criação das chaves
  chvPublica = (chvPrinc, publi)
  chvPriva = (chvPrinc, priva)

  print(f"a chave publica é {chvPublica}")
  print(f"a chave privada é {chvPriva}")

  cripto(chvPublica)


def cripto(chvPublica):

  mensagem = input("Digite a mensagem que deseja criptografar: ")


  mensagem_encript = criptografar(chvPublica, mensagem)
  print("\nMensagem Criptografada: ", mensagem_encript)


def descrip():

  mensagem_encript = input("Digite a mensagem criptografada: ")


  mensagem_decriptada = descriptar(chvPriva, mensagem_encript)
  print("\nMensagem Descriptografada:", mensagem_decriptada)



while(True):
  print("------ Se que quiser finalizar digite 'Sair' ------")

  validacao = input("Deseja criptografar ou descriptografar (Digite Crip ou Descrip): ")

  validacao = validacao.lower()

  if(validacao == 'crip'):
    validacao  = input("Deseja criar novas chaves?? (Digite sim ou não): ")
    validacao = validacao.lower()

    while(True):
      if(validacao == 'sim'):
        criarChvs()
        break

      elif(validacao == 'não'):

        p1 = int(input("Digite a primeira parte da chave publica: "))
        p2 = int(input("Digite a segunda parte da chave publica: "))

        chvPublica = (p1, p2)

        cripto(chvPublica)
        break

      else:
        print("Entrada invalida \n")

        break

  elif (validacao == 'descrip'):

    p1 = int(input("Digite a primeira parte da chave privada: "))
    p2 = int(input("Digite a segunda parte da chave privada: "))

    chvPriva = (p1, p2)

    descrip()

  elif(validacao == 'sair'):
    break

  else:
    print("Entrada invalida \n")

    continue



