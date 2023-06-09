print("*************************************")
print("Ola, bem vindo ao jogo da adivinhação")
print("*************************************")

#variavel que ira definir o valor do numero secreto
numero_secreto = 10

#input para começar o jogo ou paralo
jogo = input("Deseja jogar o jogo?(S/N) ")
tentativas = 3
rodadas = 4
#atribui duas regras a variavel "jogo"
#.lower = pode utilizar tanto letra maiuscula quanto minuscula
#.strip = ignora se há um espaço na resposta, por exemplo " s"
jogo = jogo.lower().strip()

#Estrutura de repetição para que o jogo aconteça caso a resposta da variavel "jogo" for "s"
while (jogo == "s"):
    #outro while para caso o numero de tentativas for maior que 0    
    # while(tentativas > 0):
    #o for ira fazer um loop que nem o While, porem ja atribuindo +1 a variavel "rodadas"
    for rodadas in range(1,rodadas):
        #Ira mostrar o numero de tentativas que ainda restam, decaindo caso o jogador erre
        #{} e .format = uma maneira mais bonita de deixar o codigo, onde as "{}" irao mostrar o valor dentro do ".format(variavel)"
        print("tentativas restantes {}".format(tentativas))
        #input para atribuir um valor ao numero que sera "chutado" no jogo
        #int(input("Digite um numero: ")) = atribui o valor digitado a variavel, porem o "int" serve para esclarecer que o valor é um numero inteiro
        numero_digitado = int(input("Digite um numero entre 1 e 30: "))
        #atribui o valor INTEIRO do "numero_digitado" ao "chute"
        chute = int(numero_digitado)

        #se o valor do "chute" for menor que 1 e maior que 30, exibira a mensagem de aviso
        if(chute < 1 or chute > 30):
            print("O numero deve ser entre 1 e 30!!!")
            #continue = dara continuidade ao codigo, descontando uma tentativa mas invalidando o numero, assim não dizendo se ele e maior ou menor
            continue
        #variaveis que sao atribuidas o valor caso o "numero_digitado" seja menor(<), igual(==) ou maior(>) que o "numero_secreto"
        #bool = tem dois valores "true" e "false"
        acertou = numero_digitado == numero_secreto
        maior = numero_digitado > numero_secreto
        menor = numero_digitado < numero_secreto
        #outra estrutura de repetição para a resposta digitada
        #if = se o "numero_digitado" for igual(==) a "numero_secreto" mostrara a mensagem de vitoria
        if (acertou):
            print("Parabens, voce acertou o numero!!")
            #aqui sera quando a pessoa acertar o numero, onde ele perguntara se "gostaria de jogar novamente", reatribuindo um valor a variavel "jogo"
            # jogo = input("Deseja continuar jogando? ")
            #break = sera lido caso o usuario acerte o numero, interrompedo o resto do codigo e mostrando a mensagem final
            break
        #else = caso o "numero_digitado" for diferente de "numero_secreto", mostrara a mensagem de derrota e o deixara tentar novamente
        else:
            #(<) = menor que
            if (menor):
                print("Resposta errada! o numero digitado é menor que o numero secreto")
            #elif = tem a mesma função do else, mas ele adiciona um if junto, ficando
            #else:
            #   if
            #(>) = maior que
            elif(maior):
                print("Resposta errada! o numero digitado é maior que o numero secreto")
        #toda vez que ele errar, ira descontar 1 do valor do "tentativas"         
        tentativas = tentativas - 1
    #Essa é a mensagem que ira aparecer caso o numero de tentativas chegue a 0
    print("Fim de jogo, a resposta certa é {}".format(numero_secreto))
    #perguntara se o jogador deseja jogar novamente, e atribuira esse valor ao "jogo"
    jogo = input("Deseja jogar novamente?(S/N): ")       