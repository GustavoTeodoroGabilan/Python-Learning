#Atribui uma função ao jogo inteiro, para que seja selecionado la no menu de seleção de jogos
def forca():
    print("*******************************")
    print("Ola, bem vindo ao jogo da forca")
    print("*******************************")

    print("Fim de jogo")

#Essa parte do codigo fara com que conseguimos executar esse arquivo tanto pelo "Jogos.py" quanto abrindo diretamente ele
#Essa variável "__name__", e ela é preenchida com o valor "__main__" caso o arquivo seja executado diretamente. 
if(__name__ == "__main__"):
    forca()  