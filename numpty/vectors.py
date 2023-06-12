import math
from matices import mat
from quaternions import quaternion




class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __len__(self): return math.sqrt(self.x**2+self.y**2)
    def __str__(self): return f"{self.x}x + {self.y}y"

    def __add__(self, b): return vec2(self.x+b.x, self.y+b.y)
    def __sub__(self, b): return vec2(self.x-b.x, self.y-b.y)
    def __mul__(self, b): return vec2(self.x*b, self.y*b)
    def __truediv__(self, b): return vec2(self.x/b, self.y/b)

    def dot(self, b): return self.x*b.x + self.y*b.y

    def asColumn(self): return mat.fromData([[self.x],[self.y]])
    def asRow(self): return mat.fromData([[self.x, self.y]])
    def astuple(self): return (self.x, self.y)

class vec3:
    def __init__(self, x: int|float, y: int|float, z: int|float):
        self.x = x
        self.y = y
        self.z = z
        self.i = None
        self.j = None
        self.k = None

    def set_basis(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    @staticmethod
    def i(): return vec3(1, 0, 0)
    def get_i(self):  return vec3.i() if self.i is None else self.i
    @staticmethod
    def j(): return vec3(0, 1, 0)
    def get_j(self):  return vec3.j() if self.j is None else self.j
    @staticmethod
    def k(): return vec3(0, 0, 1)
    def get_k(self):  return vec3.k() if self.k is None else self.k
    
    def get_global(self):
        if self.i is None:
            raise ValueError("this vector is global, idiot")
        return self.i*self.x + self.j*self.y + self.k*self.z

    def __len__(self): return math.sqrt(self.x**2+self.y**2+self.z**2)
    def __str__(self): return f"{self.x}x + {self.y}y + {self.z}z"
    def normalise(self): return self.__truediv__(self.__len__())

    def __add__(self, b): return vec3(self.x+b.x, self.y+b.y, self.z+b.z)
    def __sub__(self, b): return vec3(self.x-b.x, self.y-b.y, self.z-b.z)
    def __mul__(self, b): return vec3(self.x*b, self.y*b, self.z*b)
    def __truediv__(self, b): return vec3(self.x/b, self.y/b, self.z/b)

    def dot(self, b): return self.x*b.x + self.y*b.y + self.z*b.z

    def asColumn(self): return mat.fromData([[self.x],[self.y], [self.z]])
    def asRow(self): return mat.fromData([[self.x, self.y, self.z]])
    def astuple(self): return (self.x, self.y, self.z)
    def asquaternion(self): return quaternion(0, self.x, self.y, self.z)

class vecp:
    def __init__(self, r, d):
        self.r = r
        self.d = d

    def asCartesian(self): return vec2(math.cos(self.d)*self.r, math.cos(self.d)*self.r)
    