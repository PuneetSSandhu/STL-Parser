"""
A face class to store the 3 points of a face as well as the normal vector
"""
class face:
    def __init__(self, p1, p2, p3, normal):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.normal = normal

    def get_normal(self):
        """
        Get the normal vector of the face
        """
        return self.normal

    def vertices(self):
        """
        Get the vertices of the face
        """
        return (self.p1.get_tuples(), self.p2.get_tuples(), self.p3.get_tuples())