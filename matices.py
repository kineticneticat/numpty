import math

class mat:
    def __init__(self, M, N):
        # for an MxN matrix
        self.M = M # y height
        self.N = N # x height
        self.data = [[0 for n in range(N)] for m in range(M)]

    @staticmethod
    def fromData(data):
        a = mat(len(data), len(data[0]))
        a.data = data
        return a
    
    def __str__(self):
        return str(self.data)
    
    def __add__(self, b): return mat.fromData([[self.data[m][n]+b.data[m][n] for n in range(self.N)] for m in range(self.M)])
    def __sub__(self, b): return mat.fromData([[self.data[m][n]-b.data[m][n] for n in range(self.N)] for m in range(self.M)])
    def __mul__(self, b): return mat.fromData([[self.data[m][n]*b for n in range(self.N)] for m in range(self.M)])
    def __truediv__(self, b): return mat.fromData([[self.data[m][n]/b for n in range(self.N)] for m in range(self.M)])
    def __matmul__(self, b):
        if self.N != b.M:
            raise ValueError
        a = mat(self.M, b.N)
        for m in range(a.M):
            for n in range(a.N):
                c=0
                for i in range(self.N):
                    c += self.data[m][i]*b.data[i][n]
                a.data[m][n] = c
        return a



    