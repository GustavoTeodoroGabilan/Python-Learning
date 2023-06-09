def tabuada(n):
    resultado = ""
    for numero in range(n, n * 101, n):
        resultado += str(numero) + "\n"
    return resultado

n = int(input("Digite um número: "))
tabuada_str = tabuada(n)

with open("arquivo.txt", "w") as arquivo:
    arquivo.write(tabuada_str)