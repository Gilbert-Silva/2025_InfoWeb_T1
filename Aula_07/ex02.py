print("Digite três números inteiros separados por espaços")
#a = input()   # ler do teclado
#b = a.split() # divide e coloca numa lista
#x = int(b[0]) # passa cada valor para inteiro
#y = int(b[1])
#z = int(b[2])
x, y, z = map(int, input().split())
soma = 0
if x % 2 == 0: soma = soma + x
if y % 2 == 0: soma = soma + y
if z % 2 == 0: soma = soma + z
print("Soma dos pares:", soma)
