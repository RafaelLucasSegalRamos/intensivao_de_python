x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
fim = len(x) - 1
sx = 0
y = list()
print(x[::-1])

for i, pos in enumerate(x):
    y.append(x[len(x) - pos])
print(y)

for a in range(len(x)//2):
    aux = x[a]
    x[a] = x[fim]
    x[fim] = aux
    fim -= 1

print(x)