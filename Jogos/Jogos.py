#Esse arquivo sera o menu, onde sera possivel fazer a seleção dos jogos feitos, abrindo-os assim que forem selecionados
import Forca
import Adivinhação

def jogos():
    print("*******************************")
    print("Ola, por favor selecione o jogo")
    print("*******************************")

    print("(1) Forca / (2) Adivinhação")
    jogo = int(input("Qual jogo voce escolhe?"))

    if (jogo == 1):
        print("Jogando Forca")
        #"Nome do arquivo.py"."Variavel definida para o arquivo"
        Forca.forca()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        #"Nome do arquivo.py"."Variavel definida para o arquivo"
        Adivinhação.adivinhacao()
    else:
        print("Desculpe, mas essa opção não existe")

if(__name__ == "__main__"):
    jogos()