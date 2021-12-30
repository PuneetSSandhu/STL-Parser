# import face and point from point.py and face.py
from point import point as p
from face import face as f
import sys

"""
Given a file name, parse the STL file and return a list of faces.
"""
def parse_stl(file_name):
    faces = []
    with open(file_name, 'r') as stl:
        line = stl.readline()
        while not line.startswith('endsolid'):
            if line.startswith('  facet normal'):
                nums = line.split()[2:]
                normal = p(nums[0], nums[1], nums[2])
            elif line.startswith('      vertex'):
                nums = line.split()[1:]
                p1 = p(nums[0], nums[1], nums[2])
                line = stl.readline()
                nums = line.split()[1:]
                p2 = p(nums[0], nums[1], nums[2])
                line = stl.readline()
                nums = line.split()[1:]
                p3 = p(nums[0], nums[1], nums[2])
                faces.append(f(p1, p2, p3, normal))
            line = stl.readline()
    return faces




if __name__ == '__main__':
    # take command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 stlParser.py <file_name>")
        exit(1)
    file_name = sys.argv[1]
    faces = parse_stl(file_name)