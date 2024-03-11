def encontrar_i(T):
    for i in range(len(T) - 1, -1, -1):
        if T[i] < T[0] + 1:
            return i
    return -1

def encontrar_x(T, i):
    for x in range(i - 1, -1, -1):
        if T[x] > 0:
            return x
    return -1

soluciones = []

def F(T, i=None, movs=0):
    if i is None:
        i = encontrar_i(T)
    
    if i == -1:
        soluciones.append(movs)
        return movs
    
    elif soluciones and movs > min(soluciones):
        return float('inf')
    
    elif i == 0:
        return F([T[0] + 1, T[1] - 1] + T[2:], None, movs + 1)
    
    x = encontrar_x(T, i)
    
    if x == -1: # No se encontró x, no se pueden hacer movimientos
        return float('inf')
    
    new_moves = 2 * (i - x - 1) if x < i - 1 else 1
    
    # Verifica si i + 1 está dentro del rango antes de proceder
    if i + 1 < len(T):
        op1 = F(T[:i] + [T[i] + 1, T[i + 1] - 1] + T[i + 2:], None, movs + 1)
    
    if x < i - 1:
        op2 = F(T[:x] + [T[x]-1] + T[x+1:i] + [T[i]+1] + T[i+1:], None, movs + new_moves)
    else:
        op2 = float('inf')  # O alguna otra lógica que se adecue al problema
    
    if op1 <= op2:
        return op1
    else:
        return op2

# Para utilizar la función, proporciona la lista inicial T y llama a F(T)
# Ejemplo:
# T = [cantidad de fichas en cada torre]
# print(F(T))

print(F([3,2,2,4]))