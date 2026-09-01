def add_matrices(A, B):
    N = len(A)
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            C[i][j] = A[i][j] + B[i][j]
    return C

def multiply_matrices(A, B):
    N = len(A)
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
    return C

N = int(input("Enter the size of the matrices: "))

matrix1 = [list(map(int, input().split())) for _ in range(N)]
matrix2 = [list(map(int, input().split())) for _ in range(N)]
operations = list(map(int, input("Enter the operations: ").split()))

for op in operations:
    if op == 0:
        matrix1 = add_matrices(matrix1, matrix2)
    elif op == 1:
        matrix2 = add_matrices(matrix2, matrix1)
    elif op == 2:
        matrix1 = multiply_matrices(matrix1, matrix2)
    elif op == 3:
        matrix2 = multiply_matrices(matrix2, matrix1)

result = matrix1 if operations[-1] in [0, 2] else matrix2

for row in result:
    print(" ".join(map(str, row)))
