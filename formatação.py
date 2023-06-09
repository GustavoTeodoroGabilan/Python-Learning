#Formatação de strings

#nesse caso ele ira alocar o 3 a primeira chave, e o 10 a segunda
print("numero {} de {}".format(3,10))

#agora ele ira alocar o 10 na primeira chave e o 3 na segunda, invertendo a ordem
print("numero {1} de {0}".format(3,10))

#----------------------------------------------------------------------------------
# Formatação de float
#nao e necessario identificar se é float
print("numero {}".format(4.15))

#o (:f) ira identificar que é um numero float e automaticamente preenchera o espaço em branco com zeros
print("numero {:f}".format(4.15))

#esse .1f serve para dizer quantas casas decimais devem ter depois do ".", caso tenha mais de um no format, ele arredondara para o numero mais proximo
print("numero {:.1f}".format(4.15))

#quando colocamos um numero antes do ponto, ele mostrara o tanto de casas que o numero pode ter
print("numero {:2.2f}".format(0003.14))

#---------------------------------------------------------------------------------
#Formatação de inteiro
#para a formatação de numero inteiro, utiliza-se a letra "d"
#nesse sera adicionado mais 6 zeros na frente do 4
print("numero {:07d}".format(4))
