A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

m = len(A)
n = len(A[0])
p = len(B[0])

# result matrix with zeros
C = [[0 for _ in range(p)] for _ in range(m)]

# matrix multiplication
for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

# print result
for row in C:
    print(row)
