x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}
y = x

x[5] = "Teste"

print(id(x))
print(id(y))

x["SP"] = "São Paulo"
print(y)

a = 5
b = a
print(id(a))
print(id(b))
a = 10
print(id(a))
print(id(b))

