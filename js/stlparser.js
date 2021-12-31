// import face and point classes
const point = require('./point.js');
const Face = require ('./face.js');
const fs = require("fs")

function parse_STL(filename) {
    // open file
    var file = fs.readFileSync(filename, "utf8");
    // read each line

    var lines = file.split("\n");
    var faces = [];

    for (var i = 0; i < lines.length; i++) {

        if (lines[i].startsWith("  facet normal")) {
            var nums = lines[i].split(" ").slice(4);
            // convert to floats
            nums = nums.map(function(x) {
                return parseFloat(x);
            });
            var normal = new point(nums[0], nums[1], nums[2]);
        } else if (lines[i].startsWith("      vertex")) {
            var nums = lines[i].split(" ").slice(7);
            nums = nums.map(function(x) {
                return parseFloat(x);
            });
            var p1 = new point(nums[0], nums[1], nums[2]);
            i = i + 1
            nums = lines[i].split(" ").slice(7);
            nums = nums.map(function(x) {
                return parseFloat(x);
            });
            var p2 = new point(nums[0], nums[1], nums[2]);
            i = i + 1
            nums = lines[i].split(" ").slice(7);
            nums = nums.map(function(x) {
                return parseFloat(x);
            });
            var p3 = new point(nums[0], nums[1], nums[2]);
            faces.push(new Face(p1, p2, p3, normal));

        }
    }
    return faces;
}

