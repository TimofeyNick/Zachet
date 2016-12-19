class Vector:
    def __init__(self, A):
        self.x = float(A[0])
        self.y = float(A[2])

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

    def __lt__(self, other):
        return self.x < self.y or (self.x==other.x and self.y<other.x)

    def __str__(self):
        return '(%d,%d)'%(self.x,self.y)


# B = Vector(3,4)
# if A < B:
#     print('True')
