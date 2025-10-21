try:
    a = int(input("Informe o dividendo: "))
    b = int(input("Informe o divisor: "))
    print(a/b)
except ZeroDivisionError:
    print("Informe um divisor não nulo")
except ValueError:
    print("Informe números inteiros")
