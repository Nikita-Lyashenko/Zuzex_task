from functools import cmp_to_key
A = []

try:
    file = open("input.txt")
    A = file.read().split()
    file.close()
except IOError:
    print("Error!")

def Compare(x,y):
    if int(x+y) > int(y+x):
        return -1
    else:
        return 1

B = sorted(A, key=cmp_to_key(Compare))

print("".join(B))
