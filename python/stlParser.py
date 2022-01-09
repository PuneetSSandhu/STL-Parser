# import face and point from point.py and face.py
from point import point as p
from face import face as f
import sys
import struct


def get_file_type(file_name):
    with open(file_name, 'rb') as stl:
        line = stl.read(80)
        if line.startswith(b'solid'):
            return 'ascii'
        else:
            return 'binary'
    return None
    
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

# binary STL file format
# 80 bytes of header
# 4 bytes of number of triangles
# 50 bytes of triangle data

def bin_parser_stl(file_name):
    faces = []
    with open(file_name, 'rb') as stl:
        header = stl.read(80)
        num_triangles = stl.read(4)
        num_triangles = int.from_bytes(num_triangles, byteorder='little')
        for i in range(num_triangles):
            normal =  struct.unpack('3f', stl.read(12))
            p1 = struct.unpack('3f', stl.read(12))
            p2 =  struct.unpack('3f', stl.read(12))
            p3 =  struct.unpack('3f', stl.read(12))
            stl.read(2)

            faces.append(f(p(p1[0], p1[1], p1[2]), p(p2[0], p2[1], p2[2]), p(p3[0], p3[1], p3[2]), p(normal[0], normal[1], normal[2])))
    return faces

def extract_faces(file_name):
    if get_file_type(file_name) == 'ascii':
        return parse_stl(file_name)
    elif get_file_type(file_name) == 'binary':
        return bin_parser_stl(file_name)
    else:
        print('Unknown file type')
        return None


if __name__ == '__main__':
    # take command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 stlParser.py <file_name>")
        exit(1)
    file_name = sys.argv[1]
    file_type = get_file_type(file_name);
    
    if file_type == 'ascii':
        faces = parse_stl(file_name)
    elif file_type == 'binary':
        faces = bin_parser_stl(file_name)
    else:
        print("Unknown file type")
        exit(1)