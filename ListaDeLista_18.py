import curses
import os

#Laços de Repetição (1–15)
def exercicio1():
    print("Escreva um programa que imprima os números de 1 a 100 usando um laço for.")
    for i in range(100):
        print(i + 1)
        
def exercicio2():
    print("Faça um programa que exiba os múltiplos de 5 entre 0 e 100 usando while.")
    numero = 0
    while numero <= 100:
        numero += 1
        if numero % 5 == 0:
            print(numero)

def exercicio3():
    print("Solicite 10 números ao usuário e exiba a média aritmética.")
    caixinha = []

    for i in range(10):
        numero = int(input(f"Digite o {i + 1}º número: "))
        caixinha.append(numero)
        media = sum(caixinha) // len(caixinha)
    print(f"A média de {caixinha} é {media}.")

def exercicio4():
    print("Faça um programa que leia um número e exiba sua tabuada de multiplicação (1 a 10).")
    numero = int(input("Digite um número: "))
    for _ in range(10):
        print(f"{numero} X {_ + 1} = {numero * (_ + 1)}")

def exercicio5():
    print("Escreva um programa que conte quantos números entre 1 e 100 são pares.")
    caixinha = []

    for i in range(101):
        if i % 2 == 0 and i != 0:
            caixinha.append(i)
    print(len(caixinha))

def exercicio6():
    print("Crie um programa que leia vários números até que o usuário digite 0 e mostre a soma dos números lidos.")
    caixinha = []

    while True:
        numero = int(input("Digite um número: "))
        if numero != 0:
            caixinha.append(numero)
        elif numero == 0:
            break
    print(f"A soma dos números {caixinha} = {sum(caixinha)}")

def exercicio7():
    print("Faça um programa que exiba todos os números ímpares de 1 até um número informado pelo usuário.")
    entrada = int(input("Digite um número: "))
    for i in range(entrada + 1):
        if i % 2 != 0:
            print(i)

def exercicio8():
    print("Escreva um código que solicite nomes até que a palavra 'fim' "\
          "seja digitada, e depois exiba todos os nomes digitados.")
    nomes = []

    while True:
        nome = input("Digite uma palavra: ").lower().strip()
        if nome == 'fim':
            break
        elif not nome.isalpha():
            print("Digite um nome válido.")
        else:
            nomes.append(nome)
            
    print("\nNomes digitados: ")
    for nome in nomes:
        print(f"- {nome.capitalize()}")

def exercicio9():
    print("Crie um jogo de adivinhação: o computador escolhe um número de 1 a 100 e o usuário tenta adivinhar.")
    import random

    escolhaPC = random.randint(1,100)
    while True:
        entradaChute = int(input("Digite um número de 1 a 100: "))
        if entradaChute == 404:
            print(f"Você descobriu meu segredo. AAAAAAAAAAHHHHHHHHHHH@#%$#%&$¨$*#\nO número secreto é {escolhaPC}.")
        elif not (0 < entradaChute < 101):
            print("Só vale números de 1 a 100!")
        elif entradaChute != escolhaPC:
            print("Errou, tente novamente...")
        elif escolhaPC == entradaChute:
            print("Acertou!")
            break

def exercicio10():
    print("Escreva um programa que calcule o fatorial de um número usando laço for.")
    fatorial = 1

    entrada = int(input("Digite um número: "))
    for n in range(entrada, 0, -1):
        fatorial *= n 

    print(f"{entrada}! = {fatorial}.")

def exercicio11():
    print("Escreva um programa que exiba todos os divisores de um número fornecido pelo usuário.")
    caixinha = []

    entrada = int(input("Digite um número: "))
    for i in range(1,entrada + 1):
        if entrada % i == 0:
            caixinha.append(i)

    print(f"Divisível por = {caixinha}")

def exercicio12():
    print("Peça uma senha ao usuário até que ele digite a senha correta.")
    import random

    dicionario = { 0 : "ª",
                1 : "!",
                2 : "@",
                3 : "#",
                4 : "$",
                5 : "%",
                6 : "¨",
                7 : "&",
                8 : "*",
                9 : "("}
    
    senhaVersaoNumerica = ""
    concatenacaoSenha = ""

    for _ in range(6):  
        numeroAleatorio = random.randint(0,9)
        senhaVersaoNumerica += str(numeroAleatorio)
        concatenacaoSenha += dicionario[numeroAleatorio]

    while True:
        while True:
                entradaChute = input("Digite uma senha numérica de 6 caracteres: ")
                if entradaChute.isdigit() and len(entradaChute) == 6:
                    break
                else:
                    print("Digite uma senha numérica de 6 caracteres!")  
        if entradaChute == "000000":
            print(f"Você descobriu a charada, a senha é {senhaVersaoNumerica}")
            continue
        concatenacaoChute = ""
        for i in entradaChute:
            concatenacaoChute += dicionario[int(i)]
        if concatenacaoChute == concatenacaoSenha:
            print("Parabéns, senha correta")
            break
        else: 
            print("Senha incorreta, tente Novamente...")

def exercicio13():
    print("Simule uma contagem regressiva de 10 a 0.")
    import os
    import time

    print("Um ano novo está chegando!")

    os.system('pause')
    os.system('cls')

    for i in range(10,-1,-1):
        if i == 10:
            print(f"------- ⩇⩇:{i} -------")
        elif i == 0:
            print(f"------- ⩇⩇:⩇⩇ -------")
        else:
            print(f"------- ⩇⩇:⩇{i} -------")
        time.sleep(1)

    os.system('cls')

    print(f"*ੈ✩‧₊˚༘⋆ Feliz Ano Novo *ੈ✩‧₊˚༘⋆")

def exercicio14():
    print("Conte quantos números digitados pelo usuário são positivos."\
          " O programa deve parar quando um número negativo for digitado.")
    entradas = []

    while True:
        try:
            entrada = int(input("Digite um número: "))
            if entrada < 0:
                break
            entradas.append(entrada)
            continue
        except ValueError:
            print("Digite um NÚMERO válido.")

    print(f"Você digitou {len(entradas)} positivos. São eles: ")

    for i, num in enumerate(entradas):
        if i == (len(entradas) - 1):
            print(f"- {num}.")
        else:
            print(f"- {num};")

def exercicio15():
    print("Gere os 20 primeiros números da sequência de Fibonacci.")
    fibonacci = []

    for i in range(20): 
        if i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci)

#Listas (16–30)
def exercicio16():
    print("Crie uma lista com 10 números digitados pelo usuário.")
    entradas = []

    for i in range(10):
        entrada = input("Digite algo: ")
        entradas.append(entrada)

    print(f"Lista = {entradas}")

def exercicio17():
    print("Some todos os valores de uma lista de números.")
    entradas = []
    for i in range(10):
        while True: 
            try:
                entrada = int(input("Digite um número: "))
                break
            except ValueError:
                print("Digite um NÚMERO.")
        entradas.append(entrada)
    print(f"Lista = {entradas}\nSoma = {sum(entradas)}")

    #Some todos os valores de uma lista de números.
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(f"Lista = {lista}\nSoma da Lista = {sum(lista)}")

def exercicio18():
    print("Encontre o maior e o menor número de uma lista.")
    entradas = []

    for i in range(10):
        while True: 
            try:
                entrada = int(input("Digite um número: "))
                break
            except ValueError:
                print("Digite um NÚMERO.")
        entradas.append(entrada)
        
    print(f"Lista = {entradas}\nSoma = {sum(entradas)}\nMaior Número = {max(entradas)}\nMenor Número = {min(entradas)}")

def exercicio19():
#Crie um programa que leia 5 nomes e armazene em uma lista. Depois, exiba-os em ordem alfabética.
    entradas = []

    for i in range(5):
        while True: 
            try:
                entrada = input("Digite um nome: ")
                if entrada.isalpha():
                    break
            except ValueError:
                print("Digite um NOME.")
        entradas.append(entrada)

    print(f"Nomes = {sorted(entradas)}")

def exercicio20():
    print("Leia uma lista de 10 números e exiba os números pares.")
    entradasPares = []

    for i in range(10):
        while True: 
            try:
                entrada = int(input("Digite um número: "))
                if entrada % 2 == 0:
                    entradasPares.append(entrada)
                break
            except ValueError:
                print("Digite um NÚMERO.")

    print(entradasPares)

def exercicio21():
    print("Faça um programa que leia 10 números e crie uma nova lista só com os que são maiores que 50.")
    entradasMaioresCinquenta = []

    for i in range(10):
        while True: 
            try:
                entrada = int(input("Digite um número: "))
                if entrada > 50:
                    entradasMaioresCinquenta.append(entrada)
                break
            except ValueError:
                print("Digite um NÚMERO.")

    print(f"Dos números digitados, os maiores do que 50 são: {entradasMaioresCinquenta}")

def exercicio22():
    print("Solicite ao usuário uma palavra e armazene cada letra em uma lista.")
    while True: 
        entrada = input("Digite uma palavra: ")
        if entrada.isalpha():
            break
        print("Digite uma PALAVRA.")

    listas = []

    for letra in entrada:
        listas.append([letra])

    for i, lista in enumerate(listas, start=1):
        print(f"Lista{i} = {lista}")

def exercicio23():
    print("Crie um programa que remova os elementos duplicados de uma lista.")
    entradas = []

    for _ in range(5):
        entrada = input("Digite algo: ")
        entradas.append(entrada)

    i = 0

    while i < len(entradas):
        if entradas.count(entradas[i]) > 1:
            entradas.pop(i)
        else:
            i += 1
    print(entradas)

def exercicio24():
    print("Crie uma lista com 10 números aleatórios entre 1 e 100 e ordene-a.")
    import random

    lista = []
    for i in range(10):
        lista.append(random.randint(1,100))
    print(sorted(lista))

def exercicio25():
    print("Faça um programa que leia os preços de 5 produtos e exiba a soma e a média.")
    import os

    listaValores = []

    for i in range(5):
        while True:
            try:
                entrada = float(input(f"Digite o valor do produto {i}: "))
                if entrada > 0:
                    listaValores.append(entrada)
                break
            except ValueError:
                print("Digite um VALOR válido.")

    somaValores = sum(listaValores)
    os.system('cls')
    print(f"Soma dos Valores = {somaValores}\nMédia dos Valores = {somaValores / len(listaValores)}")

def exercicio26():
    print("Receba 2 listas de 5 elementos cada e crie uma terceira com a soma dos elementos de mesma posição.")
    lista1 = [] 
    lista2 = []

    for _ in range(5):
        while True:
            try:
                entrada = int(input("Digite um número para lista 1: "))
                if entrada == entrada:
                    lista1.append(entrada)
                break
            except ValueError:
                print("Digite um NÚMERO.")
        while True:
            try:
                entrada = int(input("Digite um número para lista 2: "))
                if entrada == entrada:
                    lista2.append(entrada)
                break
            except ValueError:
                print("Digite um NÚMERO.")

    print("Resultado: ")

    listaResultadoSoma = []
    for indice in range(5):
        listaResultadoSoma.append((lista1[indice] + lista2[indice]))
        print(f"{lista1[indice]} + {lista2[indice]} = {listaResultadoSoma[indice]}")
    
def exercicio27():
    print("Faça um programa que inverta a ordem dos elementos de uma lista.")
    listaTeste = ["Hello", "World", "Olá", "Mundo", "Hola", "Mundo"]
    print(f"Antiga = {listaTeste}")

    listaTeste.sort()
    print(f"Atual = {listaTeste}")

    listaTeste.sort(reverse=True)
    print(f"lautA (Invertida) = {listaTeste}")

def exercicio28():
    print("Leia uma lista de 10 nomes e remova um nome digitado pelo usuário.")
    paisesBruto = """Afeganistão (o)
    África do Sul (a)
    Albânia (a)
    Alemanha (a)
    Andorra
    Angola
    Antígua e Barbuda
    Arábia Saudita (a)
    Argélia (a)
    Argentina (a)
    Armênia (a)
    Austrália (a)
    Áustria (a)
    Azerbaijão (o)
    Bahamas (as)
    Bangladesh
    Barbados
    Barein (o)
    Belarus
    Bélgica (a)
    Belize
    Benim (o)
    Bolívia (a)
    Bósnia e Herzegovina (a)
    Botsuana
    Brasil (o)
    Brunei
    Bulgária (a)
    Burkina Fasso
    Burundi Butão (o)
    Cabo Verde
    Camarões
    Camboja (o)
    Canadá (o)
    Catar (o)
    Cazaquistão (o)
    Chade (o)
    Chile (o)
    China (a)
    Chipre (o)
    Colômbia (a)
    Comores (Ilhas Comores) (as)
    Congo (o)
    Coreia do Norte (a)
    Coreia do Sul (a)
    Costa do Marfim (a)
    Costa Rica (a)
    Croácia (a)
    Cuba
    Dinamarca (a)
    Djibuti (o)
    Dominica
    Egito (o)
    El Salvador
    Emirados Árabes Unidos (os)
    Equador (o)
    Eritreia (a)
    Eslováquia (a)
    Eslovênia (a)
    Espanha (a)
    Essuatíni (ex-Suazilândia)
    Estados Unidos (os)
    Estônia (a)
    Etiópia (a)
    Fiji
    Filipinas (as)
    Finlândia (a)
    França (a)
    Gabão (o)
    Gâmbia (a)
    Gana
    Geórgia (a)
    Granada
    Grécia (a)
    Guatemala (a)
    Guiana (a)
    Guiné (a)
    Guiné-Bissau (a)
    Guiné Equatorial (a)
    Haiti (o)
    Honduras
    Hungria (a)
    Iêmen (o)
    Ilhas Marshall (as)
    Ilhas Salomão (as)
    Índia (a)
    Indonésia (a)
    Irã (o)
    Iraque (o)
    Irlanda (a)
    Israel
    Itália (a)
    Jamaica (a)
    Japão (o)
    Jordânia (a)
    Kiribati (o)
    Kosovo (o)
    Kuwait (o)
    Laos (o)
    Lesoto (o)
    Letônia (a)
    Líbano (o)
    Libéria (a)
    Líbia (a)
    Liechtenstein
    Lituânia (a)
    Luxemburgo
    Macedônia do Norte (a)
    Madagascar
    Malásia (a)
    Malaui (o)
    Maldivas (as)
    Mali (o)
    Malta
    Marrocos
    Maurício
    Mauritânia (a)
    México (o)
    Mianmar
    Micronésia (a)
    Moçambique
    Moldávia (a)
    Mônaco
    Mongólia (a)
    Montenegro
    Namíbia (a)
    Nauru
    Nepal (o)
    Nicarágua (a)
    Níger (o)
    Nigéria (a)
    Noruega (a)
    Nova Zelândia (a)
    Omã
    Países Baixos¹
    Palau
    Panamá (o)
    Papua-Nova Guiné
    Paquistão (o)
    Paraguai (o)
    Peru (o)
    Polônia (a)
    Portugal
    Quênia (o)
    Quirguistão (o)
    Reino Unido (o)
    República Centro-Africana (a)
    República Dominicana (a)
    República Tcheca (a)
    Romênia (a)
    Ruanda
    Rússia (a)
    Samoa
    San Marino
    Santa Lúcia
    São Cristóvão e Névis
    São Tomé e Príncipe
    São Vicente e Granadinas
    Seicheles
    Senegal (o)
    Serra Leoa
    Sérvia (a)
    Singapura²
    Síria (a)
    Somália (a)
    Sri Lanka (o)
    Sudão (o)
    Sudão do Sul (o)
    Suécia (a)
    Suíça (a)
    Suriname (o)
    Tadjiquistão (o)
    Tailândia (a)
    Taiwan
    Tanzânia (a)
    Timor-Leste
    Togo (o)
    Tonga
    Trinidad e Tobago
    Tunísia (a)
    Turcomenistão (o)
    Turquia (a)
    Tuvalu
    Ucrânia (a)
    Uganda
    Uruguai (o)
    Uzbequistão (o)
    Vanuatu (o)
    Vaticano (o)
    Venezuela (a)
    Vietnã (o)
    Zâmbia (a)
    Zimbábue (o)"""

    paisesLista = []

    for linha in paisesBruto.split("\n"):
        pais = linha.split(' (')[0].strip()
        if pais:
            paisesLista.append(pais)

    print(paisesLista)

    listaPaisesEscolhidos = []

    print(f"Países = {paisesLista}")

    for i in range(10):
        while True:
            entrada = input("Digite o nome de um país: ").title()
            if entrada in paisesLista:
                if entrada in listaPaisesEscolhidos:
                    print("Esse país já foi escolhido.")
                else:
                    listaPaisesEscolhidos.append(entrada)
                    break
            else:
                print("Nenhum país com este nome encontrado.")

    print(listaPaisesEscolhidos)

    while True:
        escolha = input("Escolha um país para remover: ").title()
        try:
            if escolha in listaPaisesEscolhidos:
                listaPaisesEscolhidos.remove(escolha)
                print(f"{escolha} retirado.\nLista de países atualizada: {listaPaisesEscolhidos}.")
            break
        except ValueError:
            print("Escolha um país da lista!")

def exercicio29():
    print("Verifique se um número está presente em uma lista.")
    import random

    lista = []

    for i in range(100):
        lista.append(random.randint(1,1000))

    while True:
        try: 
            numeroEscolhido = int(input("Adivinhe um número da lista (de 1 a 1000): "))
            if 0 < numeroEscolhido < 1001:
                try:
                    temNumero = lista.index(numeroEscolhido)
                    print(f"A lista possui o número {numeroEscolhido} e está na posição {temNumero}.")
                    break
                except ValueError:
                    print(f"A lista não possui o número {numeroEscolhido}.")
        except ValueError:
            print("Digite um número válido!")

def exercicio30():
    print("Faça um programa que leia uma lista de números e exiba apenas os que estão entre 10 e 50.")
    import random

    lista = []

    for i in range(100):
        lista.append(random.randint(1,1000))
    listaExclusiva = []

    for num in lista:   
        if 10 <= num <= 50:
            listaExclusiva.append(num)

    print(listaExclusiva)

#Tuplas (31–40)
def exercicio31():
    print("Crie uma tupla com os 7 dias da semana e permita que o usuário escolha um número de 1 a 7 para exibir o dia correspondente.")
    tuplaDiasSemana = ("Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado")
    while True:
        entrada = int(input("Digite um número de 1 a 7: "))
        if 0 < entrada < 8:
            print(f"Dia da Semana correspondente: {tuplaDiasSemana[entrada - 1]}")
            break 
        else:
            print("Digite um número válido.")

def exercicio32():
    print("Faça um programa que leia 5 números e os armazene em uma tupla. Depois exiba-os em ordem crescente.")
    lista = []

    for i in range(5):
        while True:
            try: 
                entrada = int(input("Digite um número: "))
                if entrada == entrada: 
                    lista.append(entrada)
                    break
            except ValueError:
                print("Digite um valor válido!")

    tupla = tuple(lista)
    print(sorted(tupla))

def exercicio33():
    print("Crie uma tupla com os nomes de 4 frutas e mostre-as uma por linha.")
    tupla = ("Banana", "Morango", "Abacate", "Abacaxi", "Cereja")
    for i in tupla:
        print(i)

def exercicio34():
    print("Leia 3 nomes e armazene-os em uma tupla. Verifique se um nome específico está na tupla.")
    listaNomes = []

    for i in range(3):
        while True:
            entradaUsuario = input("Digite um nome: ")
            if entradaUsuario.isalpha():
                listaNomes.append(entradaUsuario.capitalize())
                break
            else:
                print("Digite um nome válido!")

    tuplaNomes = tuple(listaNomes)

    while True:
        print(f"Base de dados: {listaNomes}")
        temNome = input("Verificador de nomes, digite um: ")
        if temNome.capitalize() in tuplaNomes:
            print("Nome consta na base de dados!")
            break
        else:
            print("Nome não consta na base de dados.")
            break

def exercicio35():
    print("Faça um programa que receba 2 tuplas e crie uma nova tupla unindo ambas.")
    tupla1 = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
    tupla2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    tupla = tuple(tupla1 + tupla2)
    print(tupla)

def exercicio36():
    print("Crie uma tupla com 10 números e exiba a soma de todos os elementos.")
    tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f"Soma = {sum(tupla)}")

def exercico37():
    print("Leia uma tupla com 5 números e exiba a quantidade de números pares.")
    tupla = (1, 2, 3, 4, 5)
    lista = []
    for i in tupla:
        if i % 2 == 0:
            lista.append(i)
    print(f"Números pares: {lista}")

def exercicio38():
    print("Dada uma tupla com notas, calcule a média e informe se o aluno está aprovado (média >= 6).")
    tuplaNotasAlice = (10, 10, 9, 7.5, 8.9)
    media = sum(tuplaNotasAlice) / len(tuplaNotasAlice)
    if media >= 6:
        print(f"Aprovada! Média = {media}.")
    else:
        print(f"Reprovada! Média = {media}.")

def exercicio39():
    print("Peça ao usuário 5 letras e armazene em uma tupla. Depois exiba as vogais digitadas.")
    listaLetras = []

    for i in range(5):
        while True:
            entradaLetra = input("Digite uma letra: ")
            if entradaLetra.isalpha() and len(entradaLetra) == 1 and entradaLetra.upper() not in listaLetras:
                listaLetras.append(entradaLetra.upper())
                break
            else:
                print("Digite uma ÚNICA letra.")

    tupla = tuple(listaLetras)
    print(f"Letras: {tupla}")

def exercicio40():
    print("Dada uma tupla com nomes, exiba todos os nomes que começam com a letra 'A'.")
    nomesBruto = """Anthony	Bento	Xavier	Benício
    Dante	Dom	Matteo	Milo
    Kalel	Kael	Lorenzo	Lucca
    Oliver	Ruan	Skyler	Arlo
    Sebastian	Vicente	Uriel	Yuri
    Benjamin	Bento	Dominic	Levi
    Noah	Otto	Otávio	Pietro
    Rian	Zyan	Valentino	Micah
    Dilan	Félix	Estevão	Yohan
    Kauã	Rael	Yohan	Adriel
    Ben	David	Levi	Anton
    Elias	Óscar	Bruno	Kalu
    Enrico	Isaac	Luciam	Martim
    Tadeu	Tobias	Vicent	Xavier
    Jordan	Jonas	Gaspar	Fausto
    Alice	Aurora	Alana	Alícia
    Bárbara	Bianca	Betânia	Bela
    Cecília	Catarina	Chloe	Camily
    Dandara	Daiane	Dalila	Ester
    Elisa	Evelyn	Emily	Fátima
    Flávia	Fernanda	Giulia	Gabrielle
    Glória	Helena	Hannah	Isadora
    Isabel	Janaína	Joice	Karina
    Letícia	Laura	Lorena	Manuela
    Marcela	Mirela	Natália	Naomi
    Natasha	Olívia	Olga	Olímpia
    Pricila	Pamela	Rebeca	Rafaela
    Sofia	Sara	Tainá	Vitória
    Brigite	Brenda	Celine	Sandra
    Celeste	Lavínia	Analu	Ellie"""

    nomes = []

    for linha in nomesBruto.split("\n"):
        nome = linha.split("\t")
        nomes.extend(nome)

    tupla = tuple(nomes)
    for _ in tupla:
        if _.startswith("A"):
            print(_)

#Dicionários (41–50)
def exercicio41():
    print("Crie um dicionário com os dados de uma pessoa: nome, idade e cidade.")
    usuario = {}

    import requests

    def get_estados(uf: str):
        try:
            resposta = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}")
            resposta.raise_for_status()
            data = resposta.json()
        except (requests.HTTPError, requests.RequestException, ValueError) as e:
            print(f"Erro: {e}")
            return None
        if not isinstance(data, dict):
            return None
        return data.get("sigla")

    def get_municipios(uf: str) -> list[dict]:
        try:
            resposta = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios")
            resposta.raise_for_status()
            return resposta.json()
        except (requests.HTTPError, requests.RequestException, ValueError) as e:
            print(f"Erro: {e}")
            return []

    while True:
        entradaNome = input("Digite seu nome: ")
        if entradaNome.isalpha():
            usuario["Nome"] = entradaNome
            break
        else:
            print("Digite um Nome válido!")

    while True:
        entradaEstado = input("Digite a sigla do seu Estado (Ex.: MT): ").upper()
        sigla = get_estados(entradaEstado)
        if sigla:
           usuario["Estado"] = entradaEstado
           break
        else:
            print("Digite um Estado válido!")

    while True:
        entradaCidade = input("Digite sua Cidade: ").strip().lower()
        cidade = get_municipios(entradaEstado)
        encontrada = any(
            isinstance(m, dict) and m.get("nome", "").lower() == entradaCidade
            for m in cidade)
        if encontrada:
            usuario["Cidade"] = entradaCidade.title()
            break
        else:
            print("Digite uma Cidade válida!")

    while True:
        try:
            entradaIdade = int(input("Digite sua idade: "))
            usuario["Idade"] = entradaIdade
            break
        except ValueError:
            print("Digite uma Idade válida!")
    print(f"\nUsuário Registrado:\n")
    for i, valor in usuario.items():
        print(f"{i}: {valor}")

def exercicio42():
    print("Crie um dicionário com 5 alunos e suas notas. Depois, exiba a média geral da turma.")
    import random

    notas = 0
    dicionario = {"Fulana": list(random.randint(1,10) for _ in range(5)),
                    "Fulano": list(random.randint(1,10) for _ in range(5)),
                    "Alice": list(random.randint(1,10) for _ in range(5)),
                    "Ciclano": list(random.randint(1,10) for _ in range(5)),
                    "Beltrana": list(random.randint(1,10) for _ in range(5))}

    sumMedia = 0

    for nome, notas in dicionario.items():
        media = sum(notas) / len(notas)
        print(f"{nome}, média anual = {media:.1f}.")
        sumMedia += media
    mediaTurma = sumMedia / len(dicionario)
    print(f"\nMédia da turma = {mediaTurma:.1f}.")

def exercicio43():
    print("Faça um programa que leia o nome de 3 produtos e seus preços, armazenando no dicionário.")
    dicionarioProdutos = {}
    for _ in range(1,4):
        while True:
            entradaNome = input(f"Digite nome do produto {_}: ").capitalize()
            if entradaNome.isalpha():
                break
            else:
                print("Digite um nome válido.")
        while True:
            entradaValor = float(input(f"Digite valor do produto {_}: "))
            if entradaValor > 0:
                break
            else:
                print("Digite um valor válido.")
        dicionarioProdutos[f'Produto{_}'] = {'nome': entradaNome, 'valor': entradaValor}

    print("\nProdutos Cadastrados:")
    for produto, dados in dicionarioProdutos.items():
        print(f"{dados['nome']} - R${dados['valor']:.2f}")

def exercicio44():
    print("Dado um dicionário com o nome e idade de várias pessoas, exiba apenas os maiores de idade.")
    import random
    dicionarioPessoas = {}

    for _ in range(1,11):
        while True:
            nome = input(f"Digite o {_}º nome: ")
            if nome.isalpha():
                break
            else: 
                print("Digite um nome válido.")   
        idade = random.randint(1,100)
        dicionarioPessoas[f'Pessoa {_}'] = {'nome': nome, 'idade': idade}

    print("\nPessoas maiores de Idade:")
    for i, dados in dicionarioPessoas.items():
        if dados['idade'] >= 18:
                print(f"{dados['nome']}: {dados['idade']} anos.")

def exercicio45():
    print("Permita ao usuário buscar uma chave no dicionário e exibir o valor correspondente.")
    dicionarioAcontecimentos = {
        1500: [
            {
                "evento": "Descobrimento do Brasil",
                "descricao": "O navegador português Pedro Álvares Cabral chegou ao Brasil, marcando o início da colonização portuguesa."
            }
        ],
        1776: [
            {
                "evento": "Independência dos Estados Unidos",
                "descricao": "As treze colônias americanas proclamaram sua independência do Império Britânico, estabelecendo os Estados Unidos da América."
            }
        ],
        1789: [
            {
                "evento": "Revolução Francesa",
                "descricao": "A Revolução Francesa foi um período de grandes mudanças políticas e sociais na França, que levou à queda da monarquia e ao estabelecimento da República."
            }
        ],
        1914: [
            {
                "evento": "Início da Primeira Guerra Mundial",
                "descricao": "A Primeira Guerra Mundial começou com o assassinato do arquiduque Francisco Ferdinando da Áustria e se espalhou rapidamente pela Europa e pelo mundo."
            }
        ],
        1939: [
            {
                "evento": "Início da Segunda Guerra Mundial",
                "descricao": "A Segunda Guerra Mundial começou com a invasão da Polônia pela Alemanha, marcando o início de um conflito global."
            }
        ],
        1969: [
            {
                "evento": "Homem na Lua",
                "descricao": "O astronauta Neil Armstrong foi o primeiro ser humano a caminhar na Lua, durante a missão Apollo 11 da NASA."
            }
        ],
        1989: [
            {
                "evento": "Queda do Muro de Berlim",
                "descricao": "O Muro de Berlim, que separava a Alemanha Oriental e Ocidental, foi derrubado, simbolizando o fim da Guerra Fria e a reunificação da Alemanha."
            }
        ],
        1888: [
            {
                "evento": "Abolição da Escravidão no Brasil",
                "descricao": "A Princesa Isabel assinou a Lei Áurea, abolindo a escravidão no Brasil, que foi o último país das Américas a fazê-lo."
            }
        ]
    }

    def buscaPorAno():
        while True:
            buscaUsuario = int(input("Busque no dicionario de Acontecimentos Históricos (ou '0'): "))
            if buscaUsuario in dicionarioAcontecimentos:
                for evento in dicionarioAcontecimentos[buscaUsuario]:
                    print(f"- {evento['evento']}: {evento['descricao']}\n")
            elif buscaUsuario == 0:
                sair()
            else:
                print("Nada consta.")

    def buscaPorNome():
        while True:
            buscaUsuario = input("Busque no dicionario de Acontecimentos Históricos (ou 'sair'): ").lower()
            if buscaUsuario == 'sair':
                sair()
                encontrou = False

            for ano, eventos in dicionarioAcontecimentos.items():
                for evento in eventos:
                    if buscaUsuario in evento["evento"].lower():
                        print(f"- {evento['evento']} ({ano}): {evento['descricao']}\n")
                        encontrou = True

            if not encontrou:
                print("Nada consta.")


    def sair():
        exit()

    print("\nEscolha uma opção:")
    print("1. Buscar evento por ano.")
    print("2. Buscar evento por nome.")
    print("3. Sair.")
    opcao = input("Escolha um número: ")

    if opcao == "1":
        buscaPorAno()
    elif opcao == "2":
        buscaPorNome()
    else:
        sair()

def exercicio46():
    print("Crie um dicionário com países e capitais. Deixe o usuário digitar o país e exiba a capital.\n")

    import requests

    def get_paises() -> dict:   
        try:
            resposta = requests.get("https://restcountries.com/v3.1/all")
            resposta.raise_for_status()
            data = resposta.json()
        except (requests.HTTPError, requests.RequestException, ValueError) as e:
            print(f"Erro: {e}")
            return {}

        capitalPaises = {}
        for pais in data:
            nomePT = pais.get('translations', {}).get('por', {}).get('common')
            capitais = pais.get('capital', [])
            if nomePT and capitais:
                capitalPaises[nomePT.lower()] = capitais[0]  # Agora: país → capital

        return capitalPaises

    paises = get_paises()

    while True:
        entradaUsuario = input("Digite o nome de um país (ou 'sair'): ").strip().lower()
        if entradaUsuario == 'sair':
            break
        capital = paises.get(entradaUsuario)
        if capital:
            print(f"A capital de {entradaUsuario.title()} é {capital}.\n")
        else:
            print("País não encontrado. Tente novamente.\n")

def exercicio47():
    print("Altere a idade de uma pessoa em um dicionário a partir de uma entrada do usuário.")
    print("CADASTRO: ")

    import os

    dicionarioUsuarios = {}
    while True:
            cadastroContinuar = False
            cadastroAtualizar = False
            while True:
                entradaContinuar = input("Deseja cadastrar um novo usuário? Digite (S) ou (N): ").upper()
                try:
                    if entradaContinuar == "S":
                        cadastroContinuar = True
                        break
                    elif entradaContinuar == "N":
                        cadastroContinuar = False
                        os.system('cls')
                        querAtualizar = input("Deseja atualizar algum cadastro? Digite (S) ou (N): ").upper()
                        if querAtualizar == "S":
                            cadastroAtualizar = True
                            break
                        else:
                            os.system('cls')
                            exit()
                except ValueError:
                    print("Digite (S) ou (N).")
        
            while cadastroContinuar:
                entradaUsuarioNome = input("Digite seu nome: ").capitalize()
                if entradaUsuarioNome.isalpha():
                    if entradaUsuarioNome in dicionarioUsuarios:
                        print("Usuário já cadastrado!")
                    else:
                        try:
                            entradaUsuarioIdade = int(input("Digite sua idade: "))
                            if entradaUsuarioIdade > 0:
                                dicionarioUsuarios[entradaUsuarioNome] = entradaUsuarioIdade
                        except ValueError: 
                            print("Digite uma idade válida!")
                else: 
                    print("Digite Novamente...")
                
                continuarOutrosCadastros = input("Deseja continuar cadastrando? Digite (S) ou (N): ").upper()
                if continuarOutrosCadastros != "S":
                    cadastroContinuar = False
                    os.system('cls')

            while cadastroAtualizar:    
                entradaUsuarioNome = input("Pesquise seu nome: ")
                if entradaUsuarioNome.isalpha():
                    if entradaUsuarioNome in dicionarioUsuarios:
                        entradaUsuarioIdade = int(input("Digite a nova idade: "))
                        if entradaUsuarioIdade > 0:
                            dicionarioUsuarios[entradaUsuarioNome] = entradaUsuarioIdade
                            print(f"{entradaUsuarioNome} sua idade foi atualizada.")
                        else:
                            print("Digite uma idade válida.")
                    else:
                        print("Usuário não cadastrado.")
                else:
                    print("Digite Novamente...")  

                continuar = input("Deseja Atualizar outros Cadastros? Digite (S) ou (N): ").upper()
                if continuar != "S":
                    cadastroAtualizar = False
                    os.system('cls')

def exercicio48():
    print("Remova um item de um dicionário com base em uma chave digitada pelo usuário.")

    import os

    docesDicionario = {
        "Brigadeiro": "Brasil",
        "Pastel de Nata": "Portugal",
        "Tiramisu": "Itália",
        "Churros": "Espanha",
        "Mochi": "Japão",
        "Baklava": "Turquia",
        "Macaron": "França",
        "Pavê": "Brasil",
        "Halva": "Oriente Médio",
        "Doce de Leite": "América Latina"
    }

    def listaCarrinho():
        print("Itens Carrinho:")
        for doce in docesDicionario:
            print(f"- {doce}")

    print("Bem vindo ao APP Doce Bão!")
    listaCarrinho()

    while True:
        entrada = input("Deseja remover algum item? Digite (S) ou (N): ").upper()
        listaCarrinho()
        if entrada == "S":
            escolhaChave = input("Digite o nome do produto: ").title()
            if escolhaChave in docesDicionario:
                del docesDicionario[escolhaChave]
                print("Produto Removido!")
                os.system('pause')
                os.system('cls')
            else:
                print("Produto não encontrado!")
                os.system('pause')
                os.system('cls')
        else:
            os.system('cls')
            print("Ok, compra finalizada! ;)")
            exit()

def exercicio49():
    print("Faça um programa que conte a frequência de letras em uma palavra usando um dicionário.")

    dicionarioContador = {}

    while True:
        entradaUsuario = input("Digite uma palavra: ")
        if entradaUsuario.isalpha():
            for i in entradaUsuario:
                if i in dicionarioContador:
                    dicionarioContador[i] += 1    
                else:
                    dicionarioContador[i] = 1
            break     
        else:
            print("Uma PALAVRA por favor.")
    print(dicionarioContador)

def exercicio50():
    print("Crie um dicionário com nomes de alunos e uma lista de 3 notas. Exiba a média de cada um")

    import random
    import os
    dicionario = {}

    while True:
        try:
            entrada = int(input("Digite quantos alunos sua turma possui: "))
            if entrada > 0:
                os.system('cls')
                break
        except ValueError:
                print("Digite um número válido!")

    for i in range(entrada):
        while True:
            entradaNomes = input(f"Digite o nome do {i + 1}º aluno: ").strip().title()
            if entradaNomes.isalpha():
                notas = []
                for _ in range(3): 
                    notas.append(random.randint(1,10))
                dicionario[entradaNomes] =  notas
                os.system('cls')
                break
            else: 
                print("Digite um nome válido.")

    print("Notas Alunos:\n")
    for nome, notas in dicionario.items():
        print(f"- {nome}: {sum(notas) / len(notas):.2f}")

enunciados = {
  1: 'Escreva um programa que imprima os números de 1 a 100 usando um laço for.',
  2: 'Faça um programa que exiba os múltiplos de 5 entre 0 e 100 usando while.',
  3: 'Solicite 10 números ao usuário e exiba a média aritmética.',
  4: 'Faça um programa que leia um número e exiba sua tabuada de multiplicação (1 a 10).',
  5: 'Escreva um programa que conte quantos números entre 1 e 100 são pares.',
  6: 'Crie um programa que leia vários números até que o usuário digite 0 e mostre a soma dos números lidos.',
  7: 'Faça um programa que exiba todos os números ímpares de 1 até um número informado pelo usuário.',
  8: 'Escreva um código que solicite nomes até que a palavra "fim" seja digitada, e depois exiba todos os nomes digitados.',
  9: 'Crie um jogo de adivinhação: o computador escolhe um número de 1 a 100 e o usuário tenta adivinhar.',
  10: 'Escreva um programa que calcule o fatorial de um número usando laço for.',
  11: 'Escreva um programa que exiba todos os divisores de um número fornecido pelo usuário.',
  12: 'Peça uma senha ao usuário até que ele digite a senha correta.',
  13: 'Simule uma contagem regressiva de 10 a 0.',
  14: 'Conte quantos números digitados pelo usuário são positivos. O programa deve parar quando um número negativo for digitado.',
  15: 'Gere os 20 primeiros números da sequência de Fibonacci.',
  16: 'Crie uma lista com 10 números digitados pelo usuário.',
  17: 'Some todos os valores de uma lista de números.',
  18: 'Encontre o maior e o menor número de uma lista.',
  19: 'Crie um programa que leia 5 nomes e armazene em uma lista. Depois, exiba-os em ordem alfabética.',
  20: 'Leia uma lista de 10 números e exiba os números pares.',
  21: 'Faça um programa que leia 10 números e crie uma nova lista só com os que são maiores que 50.',
  22: 'Solicite ao usuário uma palavra e armazene cada letra em uma lista.',
  23: 'Crie um programa que remova os elementos duplicados de uma lista.',
  24: 'Crie uma lista com 10 números aleatórios entre 1 e 100 e ordene-a.',
  25: 'Faça um programa que leia os preços de 5 produtos e exiba a soma e a média.',
  26: 'Receba 2 listas de 5 elementos cada e crie uma terceira com a soma dos elementos de mesma posição.',
  27: 'Faça um programa que inverta a ordem dos elementos de uma lista.',
  28: 'Leia uma lista de 10 nomes e remova um nome digitado pelo usuário.',
  29: 'Verifique se um número está presente em uma lista.',
  30: 'Faça um programa que leia uma lista de números e exiba apenas os que estão entre 10 e 50.',
  31: 'Crie uma tupla com os 7 dias da semana e permita que o usuário escolha um número de 1 a 7 para exibir o dia correspondente.',
  32: 'Faça um programa que leia 5 números e os armazene em uma tupla. Depois exiba-os em ordem crescente.',
  33: 'Crie uma tupla com os nomes de 4 frutas e mostre-as uma por linha.',
  34: 'Leia 3 nomes e armazene-os em uma tupla. Verifique se um nome específico está na tupla.',
  35: 'Faça um programa que receba 2 tuplas e crie uma nova tupla unindo ambas.',
  36: 'Crie uma tupla com 10 números e exiba a soma de todos os elementos.',
  37: 'Leia uma tupla com 5 números e exiba a quantidade de números pares.',
  38: 'Dada uma tupla com notas, calcule a média e informe se o aluno está aprovado (média >= 6).',
  39: 'Peça ao usuário 5 letras e armazene em uma tupla. Depois exiba as vogais digitadas.',
  40: 'Dada uma tupla com nomes, exiba todos os nomes que começam com a letra "A".',
  41: 'Crie um dicionário com os dados de uma pessoa: nome, idade e cidade.',
  42: 'Crie um dicionário com 5 alunos e suas notas. Depois, exiba a média geral da turma.',
  43: 'Faça um programa que leia o nome de 3 produtos e seus preços, armazenando no dicionário.',
  44: 'Dado um dicionário com o nome e idade de várias pessoas, exiba apenas os maiores de idade.',
  45: 'Permita ao usuário buscar uma chave no dicionário e exibir o valor correspondente.',
  46: 'Crie um dicionário com países e capitais. Deixe o usuário digitar o país e exiba a capital.',
  47: 'Altere a idade de uma pessoa em um dicionário a partir de uma entrada do usuário.',
  48: 'Remova um item de um dicionário com base em uma chave digitada pelo usuário.',
  49: 'Faça um programa que conte a frequência de letras em uma palavra usando um dicionário.',
  50: 'Crie um dicionário com nomes de alunos e uma lista de 3 notas. Exiba a média de cada um.'
}

menus = {
    "Laços de Repetição": list(range(1, 16)),
    "Listas": list(range(16, 31)),
    "Tuplas": list(range(31, 41)),
    "Dicionários": list(range(41, 51))
}

def exibirMenu(stdscr, titulo, opcoes, is_submenu=False):
    opcao = 0
    while True:
        stdscr.clear()
        stdscr.addstr(f"{titulo}\nUse ↑ ↓ para navegar. Enter para selecionar. ESC para voltar.\n\n")
        for i, item in enumerate(opcoes):
            prefixo = "→ " if i == opcao else "   "
            linha = f"{prefixo}"
            if is_submenu:
                num = item
                linha += f"Exercício {num}: {enunciados.get(num, '[Enunciado não encontrado]')}"
            else:
                linha += item

            if i == opcao:
                stdscr.addstr(linha + "\n", curses.A_REVERSE)
            else:
                stdscr.addstr(linha + "\n")

        tecla = stdscr.getch()
        if tecla == curses.KEY_UP:
            opcao = (opcao - 1) % len(opcoes)
        elif tecla == curses.KEY_DOWN:
            opcao = (opcao + 1) % len(opcoes)
        elif tecla == 27:
            return None
        elif tecla in [curses.KEY_ENTER, 10, 13]:
            return opcoes[opcao]

def main(stdscr):
    curses.curs_set(0)
    while True:
        escolha_menu = exibirMenu(stdscr, "MENU PRINCIPAL", list(menus.keys()))
        if escolha_menu is None:
            break

        submenu = menus[escolha_menu]

        while True:
            escolha_exercicio = exibirMenu(stdscr, f"{escolha_menu} - Exercícios", submenu, is_submenu=True)
            if escolha_exercicio is None:
                break  # Volta ao menu principal

            numero = escolha_exercicio

            while True:
                
                descricao = enunciados.get(numero, "[Enunciado não encontrado]")
                stdscr.addstr(f"Executando Exercício {numero}\n", curses.A_BOLD)
                stdscr.addstr(f"{descricao}\n\n")
                stdscr.addstr("Pressione ESC para voltar ou ENTER para repetir após a execução...\n")
                stdscr.refresh()

                curses.endwin()
                try:
                    os.system('cls')
                    globals()[f"exercicio{numero}"]()
                except KeyError:
                    print(f"Função exercicio{numero}() não encontrada.")
                input("\nPressione Enter para continuar...\n")

                # Retoma curses
                stdscr.clear()
                stdscr.addstr("Deseja repetir o exercício? (ENTER = repetir / ESC = voltar)\n")
                stdscr.refresh()
                key = stdscr.getch()
                if key == 27:  # ESC
                    break
                elif key in [10, 13]:  # ENTER
                    continue
                else:
                    break

if __name__ == "__main__":
    print("Olá, seja bem-vindo(a) à\nLista de Exercícios - Laços de Repetição, Listas, Tuplas e Dicionários.")
    os.system('pause')
    print()
    curses.wrapper(main)