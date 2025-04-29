class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2 
    
# x é uma referência   Triangulo() cria um objeto (instância)
x = Triangulo()
x.b = 10
x.h = 20

y = Triangulo()
y.b = 30
y.h = 40

z = x
z.b = 50
z.h = 100

print(id(x))
print(id(y))
print(id(z))

print(x.b, x.h)
print(y.b, y.h)


