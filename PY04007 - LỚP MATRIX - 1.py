class Matrix:
    def __init__(self, n, m, data):
        self.n = n
        self.m = m
        self.data = data

    def transpose(self):
        transposed = []
        for j in range(self.m):
            row = []
            for i in range(self.n):
                row.append(self.data[i][j])
            transposed.append(row)
        return Matrix(self.m, self.n, transposed)

    def multiply(self, other):
        result = []
        for i in range(self.n):
            row = []
            for j in range(other.m):
                s = 0
                for k in range(self.m):
                    s += self.data[i][k] * other.data[k][j]
                row.append(s)
            result.append(row)
        return Matrix(self.n, other.m, result)

    def print(self):
        for row in self.data:
            print(' '.join(str(x) for x in row))


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    data = []
    for _ in range(n):
        row = list(map(int, input().split()))
        data.append(row)
    a = Matrix(n, m, data)
    b = a.transpose()
    product = a.multiply(b)
    product.print()
