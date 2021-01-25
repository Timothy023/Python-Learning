class Test:
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    
    def __str__(self) :
        return "In this vector: x = %d, y = %d." % (self.x, self.y)

    def __add__(self, other) :
        return Test(self.x + other.x, self.y + other.y)

    def __sub__(self, other) :
        return Test(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other) :
        return Test(self.x * other.x, self.y * other.y)
    
def test():
    a = Test(10, 20)
    b = Test(5, 10)
    print ("Test add: ", a + b)
    print ("Test sub: ", a - b)
    print ("Test mul: ", a * b)

test()