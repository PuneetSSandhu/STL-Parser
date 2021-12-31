class point {
    constructor(x, y, z) {

        this.x = x;
        this.y = y;
        this.z = z;
    }

    getPoint() {
        return {
            x: this.x,
            y: this.y,
            z: this.z
        };
    }
}