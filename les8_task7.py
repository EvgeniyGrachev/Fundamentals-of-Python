class Complex:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        x = self.x * other.x - self.y * other.y
        y = self.x * other.y + other.x * self.y
        return Complex(x, y)

    def __str__(self):
        return f'{self.x} + {self.y}i'


comp1 = Complex(6, 12)
comp2 = Complex(5, 3)
print(comp1 + comp2)
print(comp1 * comp2)
