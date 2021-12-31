class Face {
    constructor(p1, p2, p3, normal) {
        this.p1 = p1;
        this.p2 = p2;
        this.p3 = p3;
        this.normal = normal;
    }

    getNormal() {
        return this.normal;
    }

    toString() {
        return this.p1.toString() + " " + this.p2.toString() + " " + this.p3.toString() + " " + this.normal.toString();
    }
}