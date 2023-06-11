
import math
class quaternion:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.theta = None
        self.axis = None

    @staticmethod
    def axisangle(vec, theta):
        a = quaternion(
            round(math.cos(theta/2), 10),
            round(math.sin(theta/2)*vec.x, 10),
            round(math.sin(theta/2)*vec.y, 10),
            round(math.sin(theta/2)*vec.z, 10),
        )
        a.theta = theta
        a.axis = vec
        return a
    
    def __str__(self):
        return f"{self.a} + {self.b}i + {self.c}j + {self.d}k"

    def __add__(self, b): return quaternion(self.a+b.a, self.b+b.b, self.c+b.c, self.d+b.d)
    def __sub__(self, b): return quaternion(self.a-b.a, self.b-b.b, self.c-b.c, self.d-b.d)
    def __mul__(self, b): return quaternion(self.a*b, self.b*b, self.c*b, self.d*b)
    def __truediv__(self, b): return quaternion(self.a/b, self.b/b, self.c/b, self.d/b)
    def __neg__(self): return quaternion(self.a, -self.b, -self.c, -self.d)
    

    #hamilton
    def __matmul__(self, b):
        return quaternion(
            round(self.a*b.a - self.b*b.b - self.c*b.c - self.d*b.d, 10),
            round(self.a*b.b + self.b*b.a + self.c*b.d - self.d*b.c, 10),
            round(self.a*b.c - self.b*b.d + self.c*b.a + self.d*b.b, 10),
            round(self.a*b.d + self.b*b.c - self.c*b.b + self.d*b.a, 10),
        )