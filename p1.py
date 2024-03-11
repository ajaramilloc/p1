import sys
sys.setrecursionlimit(100000000)

def encontrar_i(T):
    for i in range(len(T)-1, -1, -1):
        if i == len(T) - 1:
            pass
        elif T[i] < T[i+1]:
            return i
    return -1

def encontrar_x(T, i):
    for x in range(i-1, -1, -1):
        if T[x] > 0:
            return x
    return -1

soluciones = []

def F(T, i, movs):
    i = encontrar_i(T)
    x = encontrar_x(T, i)
    new_movs = 0
    print(soluciones)

    if x < i-1:
        new_movs = (i-1)-x

    if i == -1:
        soluciones.append(movs)
        return movs
    
    elif soluciones and movs > min(soluciones):
        return float('inf')
    
    elif i == 0:
        return F([T[0]+1, T[1]-1]+T[2:], i, movs+1)
    
    elif i > 0 and F(T[:i] + [T[i]+1, T[i+1]-1] + T[i+2:], i, movs+1) <= F(T[:x] + [T[x]-1] + T[x+1:i] + [T[i]+1] + T[i+1:], i, movs + new_movs):
        return F(T[:i] + [T[i]+1, T[i+1]-1] + T[i+2:], i, movs+1)

    else:
        return F(T[:x] + [T[x]-1] + T[x+1:i] + [T[i]+1] + T[i+1:], i, movs + new_movs)
    

    

    



    
    

# Para utilizar la función, proporciona la lista inicial T y llama a F(T)
# Ejemplo:
# T = [cantidad de fichas en cada torre]
# print(F(T))

print(F([7, 0, 0, 0, 0, 0, 0, 1], 0, 0))
print("Fin")