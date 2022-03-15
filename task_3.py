A = []
try:
    file = open("input.txt")
    A = file.read().split()
    file.close()
except IOError:
    print("Файл не найден!")

def Compare(x,y):
    if int(x+y) > int(y+x):
        return -1
    else:
        return 1

from functools import cmp_to_key
B = sorted(A, key=cmp_to_key(Compare))

print("".join(B))
