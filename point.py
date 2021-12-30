"""
3D point class to represent a point in 3D space.
"""
class point:
    def __init__ (self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __str__ (self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __add__ (self, other):
        return point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__ (self, other):
        return point(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__ (self, other):
        return point(self.x * other, self.y * other, self.z * other)

    def __truediv__ (self, other):
        return point(self.x / other, self.y / other, self.z / other)

    def __eq__ (self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__ (self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z
    
    def __neg__ (self):
        return point(-self.x, -self.y, -self.z)