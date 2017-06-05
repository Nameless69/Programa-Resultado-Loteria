import time
import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup

now = datetime.now()

# PROXIMO UPDATE -------> O PROGRAMA IRA RODAR ATE O SITE FOR ATUALIZADO COM O RESULTADO, USAREMOS A BIBLIOTECA TIME

def base():
    url = "http://loterias.caixa.gov.br/wps/portal/loterias/landing"
    codebase = requests.get(url)
    if codebase.content is not None:
        print("#Pagina baixada")
    else:
        print("#Pagina nao baixada")
    soup = BeautifulSoup(codebase.content, 'html.parser')
    return soup

def data2(dat):
    calendar = {'janeiro':1,'fevereiro':2,'março':3,'abril':4,'maio':5,'junho':6,'julho':7,'agosto':8,'setembro':9,'outubro':10,'novembro':11,'dezembro':12}
    dia = dat[:2]
    dia = int(dia)
    if dia < 10:
        mes = dat[5:-8]
        dia = str(dia)
        dia = '0' + dia
    else:
        mes = dat[6:-8]
    mes1 = calendar[mes.lower()]
    if mes1 < 10:
        mes1 = str(mes1)
        mes1 = '0' + mes1
    ano = dat[-4:]
    data1 = str(dia) + '/' + mes1 + '/' + ano
    return data1

def passou(dat):
    dia = int(dat[:2])
    mes = int(dat[3:5])
    ano = int(dat[6:])
    if ano>now.year or (ano==now.year and mes>now.month) or (ano==now.year and mes==now.month and dia>now.day):
        return 0
    elif ano==now.year and mes==now.month and dia==now.day:
        return 1
    else:
        return 2
    
print('Bem vindo ao SOFTERY\n')
print('1 - Mega Sena')
print('2 - LotoFacil')
print('3 - Quina')
print('4 - Lotomonia')
print('5 - TimeMania')
print('6 - DuplaSena')

escolha = input('\nDigite qual jogo apostou: ')
escolha = int(escolha)

if(escolha==1):
    soup = base()
    listaNum = []
    listaAposta = []
    aux3=0
    aux4=0
    dataC = input("\nDigite a data da premiação(dd/mm/aaaa): ")
    passo = passou(dataC)
    if passo == 0:
        print("#Ainda nao chegamos na data " + dat)
    if passo == 2 or passo ==1:
        for link2 in soup.find_all("div", class_="product-column"):
            for link3 in link2.find_all("p", class_="description"):
                aux5 = re.search(r',(.+)',link3.text)
                aux4+=1
                if dataC == data2(link3.text[aux5.start()+2:aux5.end()]) and aux4==escolha:
                    aux3=1
                    for link in link2.find_all("ul", class_="resultado-loteria mega-sena"):
                        if link is not None:
                            for num in link.find_all("li"):
                                listaNum += [int(num.text)]                
                            print("\nDigite os 6 numeros que voce apostou: ")
                            for i in range(6):
                                aux2 = input()
                                listaAposta += [int(aux2)]
                            print("Os numeros sorteados foram ", end='')
                            print(listaNum)
                            print("Os numeros apostados foram ", end='')
                            print(listaAposta)
                            aux = 0
                            for i in range(6):
                                for j in range(6):
                                    if listaAposta[i] == listaNum[j]:
                                        aux+=1
                            if aux == 4:    
                                print("Voce fez uma Quadra(4 acertos) e foi premiado!!!")
                            elif aux == 5:    
                                print("Voce fez uma Quina(5 acertos) e foi premiado!!!")
                            elif aux == 6:    
                                print("Voce fez uma Sena(6 acertos) e foi premiado!!!")
                            else:
                                print("Infelizmente, voce nao foi premiado!")
            if aux3==1:
                break

if(escolha==2):
    soup = base()
    listaNum = []
    listaAposta = []
    aux3=0
    aux4=0
    dataC = input("\nDigite a data da premiação(dd/mm/aaaa): ")
    passo = passou(dataC)
    if passo == 0:
        print("#Ainda nao chegamos na data " + dat)
    if passo == 2 or passo ==1:
        for link2 in soup.find_all("div", class_="product-column"):# link2 = div(product-column)
            for link3 in link2.find_all("p", class_="description"):# link3 = p(decription)
                aux5 = re.search(r',(.+)',link3.text)
                aux4+=1
                if dataC == data2(link3.text[aux5.start()+2:aux5.end()]) and aux4==escolha:
                    aux3=1
                    for link in link2.find_all("table", class_="simple-table lotofacil"):
                        if link is not None:
                            for num in link.find_all("td"):
                                listaNum += [int(num.text)]                
                            print("\nDigite os 15 numeros que voce apostou: ")
                            for i in range(15):
                                aux2 = input()
                                listaAposta += [int(aux2)]
                            print("Os numeros sorteados foram ", end='')
                            print(listaNum)
                            print("Os numeros apostados foram ", end='')
                            print(listaAposta)
                            aux = 0
                            for i in range(15):
                                for j in range(15):
                                    if listaAposta[i] == listaNum[j]:
                                        aux+=1
                            print("Voce acertou %d numeros" % (aux))
                            if aux>=11:
                                print("Voce foi premiado!!!")
                            else:
                                print("Infelizmente, voce nao foi premiado!")
            if aux3==1:
                break

if(escolha==3):
    soup = base()
    listaNum = []
    listaAposta = []
    aux3=0
    aux4=0
    dataC = input("\nDigite a data da premiação(dd/mm/aaaa): ")
    passo = passou(dataC)
    if passo == 0:
        print("#Ainda nao chegamos na data " + dat)
    if passo == 2 or passo ==1:
        for link2 in soup.find_all("div", class_="product-column"):
            for link3 in link2.find_all("p", class_="description"):
                aux5 = re.search(r',(.+)',link3.text)
                aux4+=1
                if dataC == data2(link3.text[aux5.start()+2:aux5.end()]) and aux4==escolha:
                    aux3=1
                    for link in link2.find_all("ul", class_="resultado-loteria quina"):
                        if link is not None:
                            for num in link.find_all("li"):
                                listaNum += [int(num.text)]                
                            print("\nDigite os 5 numeros que voce apostou: ")
                            for i in range(5):
                                aux2 = input()
                                listaAposta += [int(aux2)]
                            print("Os numeros sorteados foram ", end='')
                            print(listaNum)
                            print("Os numeros apostados foram ", end='')
                            print(listaAposta)
                            aux = 0
                            for i in range(5):
                                for j in range(5):
                                    if listaAposta[i] == listaNum[j]:
                                        aux+=1
                            if aux == 2:    
                                print("Voce fez um Duque(2 acertos) e foi premiado!!!")
                            elif aux == 3:    
                                print("Voce fez um Terno(3 acertos) e foi premiado!!!")
                            elif aux == 4:    
                                print("Voce fez uma Quadra(4 acertos) e foi premiado!!!")
                            elif aux == 5:    
                                print("Voce fez uma Quina(5 acertos) e foi premiado!!!")
                            else:
                                print("Infelizmente, voce nao foi premiado!")
            if aux3==1:
                break

if(escolha==4):
    soup = base()
    listaNum = []
    listaAposta = []
    aux3=0
    aux4=0
    dataC = input("\nDigite a data da premiação(dd/mm/aaaa): ")
    passo = passou(dataC)
    if passo == 0:
        print("#Ainda nao chegamos na data " + dat)
    if passo == 2 or passo ==1:
        for link2 in soup.find_all("div", class_="product-column"):
            for link3 in link2.find_all("p", class_="description"):
                aux5 = re.search(r',(.+)',link3.text)
                aux4+=1
                if dataC == data2(link3.text[aux5.start()+2:aux5.end()]) and aux4==escolha:
                    aux3=1
                    for link in link2.find_all("table", class_="simple-table lotomania"):
                        if link is not None:
                            for num in link.find_all("td"):
                                listaNum += [int(num.text)]                
                            print("\nDigite os 20 numeros que voce apostou: ")
                            for i in range(20):
                                aux2 = input()
                                listaAposta += [int(aux2)]
                            print("Os numeros sorteados foram ", end='')
                            print(listaNum)
                            print("Os numeros apostados foram ", end='')
                            print(listaAposta)
                            aux = 0
                            for i in range(20):
                                for j in range(20):
                                    if listaAposta[i] == listaNum[j]:
                                        aux+=1
                            if aux>=15 or aux==0:
                                print("Voce foi premiado com %d acertos!!!" % (aux))
                            else:
                                print("Voce acertou %d mas infelizmente nao foi premiado!" % (aux))
            if aux3==1:
                break
if(escolha==5):
    soup = base()
    listaNum = []
    listaAposta = []
    aux3=0
    aux4=0
    dataC = input("\nDigite a data da premiação(dd/mm/aaaa): ")
    passo = passou(dataC)
    if passo == 0:
        print("#Ainda nao chegamos na data " + dat)
    if passo == 2 or passo ==1:
        for link2 in soup.find_all("div", class_="product-column"):
            for link3 in link2.find_all("p", class_="description"):
                aux5 = re.search(r',(.+)',link3.text)
                aux4+=1
                if dataC == data2(link3.text[aux5.start()+2:aux5.end()]) and aux4==escolha:
                    aux3=1
                    for link in link2.find_all("ul", class_="resultado-loteria timemania"):
                        if link is not None:
                            for num in link.find_all("li"):
                                listaNum += [int(num.text)]                
                            print("\nDigite os 7 numeros que voce apostou: ")
                            for i in range(7):
                                aux2 = input()
                                listaAposta += [int(aux2)]
                            print("Os numeros sorteados foram ", end='')
                            print(listaNum)
                            print("Os numeros apostados foram ", end='')
                            print(listaAposta)
                            aux = 0
                            for i in range(7):
                                for j in range(7):
                                    if listaAposta[i] == listaNum[j]:
                                        aux+=1
                            if aux >=3:    
                                print("Voce foi premiado com %d acertos!!!" % (aux))
            if aux3==1:
                break

if(escolha==6):
    soup = base()
    listaNum = []
    listaAposta = []
    aux3=0
    aux4=0
    aux6=0
    dataC = input("\nDigite a data da premiação(dd/mm/aaaa): ")
    passo = passou(dataC)
    if passo == 0:
        print("#Ainda nao chegamos na data " + dat)
    if passo == 2 or passo ==1:
        for link2 in soup.find_all("div", class_="product-column"):
            for link3 in link2.find_all("p", class_="description"):
                aux5 = re.search(r',(.+)',link3.text)
                aux4+=1
                if dataC == data2(link3.text[aux5.start()+2:aux5.end()]) and aux4==escolha:
                    aux3=1
                    for link in link2.find_all("ul", class_="resultado-loteria duplasena"):
                        aux6+=1
                        if link is not None:
                            listaNum = []
                            for num in link.find_all("li"):
                                listaNum += [int(num.text)]
                            listaAposta = []
                            print("\nDigite os 6 numeros que voce apostou no %dº sorteio: " % (aux6))
                            for i in range(6):
                                aux2 = input()
                                listaAposta += [int(aux2)]
                            print("Os numeros sorteados foram ", end='')
                            print(listaNum)
                            print("Os numeros apostados foram ", end='')
                            print(listaAposta)
                            aux = 0
                            for i in range(6):
                                for j in range(6):
                                    if listaAposta[i] == listaNum[j]:
                                        aux+=1
                            if aux == 3:    
                                print("Voce fez um Terno(3 acertos) e foi premiado no %dº sorteio!!!" % (aux6))
                            elif aux == 4:    
                                print("Voce fez uma Quadra(4 acertos) e foi premiado no %dº sorteio!!!" % (aux6))
                            elif aux == 5:    
                                print("Voce fez uma Quina(5 acertos) e foi premiado no %dº sorteio!!!" % (aux6))
                            elif aux == 6:    
                                print("Voce fez uma Sena(6 acertos) e foi premiado no %dº sorteio!!!" % (aux6))
                            else:
                                print("Infelizmente, voce nao foi premiado!")
            if aux3==1:
                break
