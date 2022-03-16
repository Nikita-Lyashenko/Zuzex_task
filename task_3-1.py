A = []
try:
    file = open("input.txt")
    A = file.read().split()
    file.close()
except IOError:
    print("Error!")

def Sort(A):
    if len(A) > 1:
        X = A[:len(A)//2]
        Y = A[len(A)//2:]
        X = Sort(X)
        Y = Sort(Y)
        i = 0
        j = 0
        len_x = len(X)
        len_y = len(Y)
        M = []
        while True:
            if (X[i] + Y[j]) > (Y[j] + X[i]):
                M.append(X[i])
                i += 1
            else:
                M.append(Y[j])
                j += 1
        
            if (i >= len_x):
                M += Y[j:] 
                break
            if (j >= len_y):
                M += X[i:]
                break
        return M     
    else:
        return A

B = Sort(A)
print("".join(B))

