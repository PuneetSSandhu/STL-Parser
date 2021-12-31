import face from './face.js';
import point from './point.js';

function parse_STL(filename) {
    // open file
    var file = new File(filename);
    file.open("r");
    // read each line

    var lines = file.readAll();
    var faces = [];

    for (var i = 0; i < lines.length; i++) {

        while (!lines[i].startswith("endsolid")) {
            if (lines[i].startswith("  facet normal")) {
                var nums = lines[i].split(" ").slice(2);
                var normal = new face(new point(nums[0], nums[1], nums[2]));
            } else if (lines[i].startswith("      vertex")) {
                var nums = lines[i].split(" ").slice(1);
                var p1 = new point(nums[0], nums[1], nums[2]);
                i = i + 1
                nums = lines[i].split(" ").slice(1);
                var p2 = new point(nums[0], nums[1], nums[2]);
                i = i + 1
                nums = lines[i].split(" ").slice(1);
                var p3 = new point(nums[0], nums[1], nums[2]);
                faces.push(new face(p1, p2, p3, normal));
            }
        }
    }
    return faces;
}

// test code
var faces = parse_STL("../VoxelCat.STL");
for (var i = 0; i < faces.length; i++) {
    print(faces[i].toString());
}