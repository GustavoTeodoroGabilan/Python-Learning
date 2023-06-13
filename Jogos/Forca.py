#Atribui uma função ao jogo inteiro, para que seja selecionado la no menu de seleção de jogos
def forca():
    print("*******************************")
    print("Ola, bem vindo ao jogo da forca")
    print("*******************************")

    palavra_secreta = "banana"
    #Atribui o valor FALSO para o enforcou
    enforcou = False
    #Atribui o valor FALSO para o acertou
    acertou = False
    rodadas = 3
    tentativas = 10
    #enquanto o jogador não acertar e não ter enforcado, o jogo continuara
    while(not acertou and not enforcou):
        print("Jogando...")
        
        #Variavel de chute para cada letra escrita
        chute = input("Digite uma letra: ")
        #Strip ira retirar o ignorar o espaçamento no inicio e no fim
        chute = chute.strip()

        #Posição da letra
        posicao = 0
        #PARA letra DENTRO DE palavra_secreta
        for letra in palavra_secreta:
            #se chute for igual a letra
            #.upper() para que ele considere caso seja escrito em maiusculo
            if(chute.upper() == letra.upper()):
                #Mostra a letra e a sua posição dentro da palavra
                print("Encontrei a letra {} na posição {}".format(letra, posicao))
            posicao = posicao + 1    

    print("Fim de jogo")

#Essa parte do codigo fara com que conseguimos executar esse arquivo tanto pelo "Jogos.py" quanto abrindo diretamente ele
#Essa variável "__name__", e ela é preenchida com o valor "__main__" caso o arquivo seja executado diretamente. 
if(__name__ == "__main__"):
    forca()  
