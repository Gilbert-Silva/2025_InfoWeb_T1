x = [1, 2, 10, 5, 8]
print(type(x))
print(x[3])
#print(x[10])

x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}
print(type(x))
print(x["RN"])
x["AM"] = "Manaus"
print(x)
#print(x["SP"])
for item in x.items(): 
    print(item)

y = (1, 10, 5)
z = [1, 10, 5]
print(type(y))
print(max(y))
print(y[2])
z[0] = 5
print(z)
#y[0] = 5

for key in x: print(key)
for key in x.keys(): print(key)
for value in x.values(): print(value)

y = x

