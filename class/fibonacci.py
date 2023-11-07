import sys
if len(sys.argv) == 2:
    n = int(sys.argv[1])
else:
    n = int(input("Number: "))

a = 1
b = 1
print(a, b, sep="\n")
for i in range(n-2):
    c = a + b
    a = b
    b = c
    print(c)
