def suma(A,B):
    C = [] 
    for i in range(len(A)):
        C.append([])   # agrega renglon vacio
        for j in range(len(B)):
            C[i].append(A[i][j]+B[i][j])
            
    return C

def resta(A,B):
    C = [] 
    for i in range(len(A)):
        C.append([])   # agrega renglon vacio
        for j in range(len(B)):
            C[i].append(A[i][j]-B[i][j])
            
    return C

def mul(A,B):
    C = [] 
    for i in range(len(A)):
        C.append([])   # agrega renglon vacio
        for j in range(len(B)):
            suma = 0
            for k in range(len(A)):
                suma += A[i][k]*B[k][j]
            C[i].append(suma)
    return C

# programa principal
#A = [[2,3,1,-1],[-2,0,-2,3],[2,3,1,2],[3,4,2,3]]
#B = [[2,1,3,2],[-1,2,-3,0],[1,0,2,0],[-1,0,2,0]]

#print(mul(A,B))