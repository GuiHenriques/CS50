n = 6
#operation = input()

matriz = [[i for i in range(n)] for i in range(n)]
for i in matriz: print(i)

"""
for l in range(n):
    for _ in range(n):
        matriz[l].append(float(input()))
"""
 
soma = qtd = 0
for i in range(n//2 - 1):
    for x in range(i+1, n-1-i):
        soma += matriz[i][x]
        #print(f" [{i}][{x}]")
        qtd += 1
print(soma)

"""
if operation == "S":
    print(round(soma, 1))
else: print(round(soma/qtd, 1))
"""