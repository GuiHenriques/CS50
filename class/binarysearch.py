def binary_search(sequence, item):
    start = 0
    end = len(sequence) - 1
    
    while start <= end:
        mid = (start + end)//2
        if sequence[mid] == x:
            return mid
        elif sequence[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return None


lista = [i for i in range(0, 25, 3)]
print(lista)
x = int(input("N: "))
print(binary_search(lista, x))

