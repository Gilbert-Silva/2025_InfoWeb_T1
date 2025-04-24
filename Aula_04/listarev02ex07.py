print("Digite uma frase: ")
frase = input() + " "

while len(frase) > 0:
    print(frase)
    k = frase.index(" ")
    frase = frase[k+1:]



