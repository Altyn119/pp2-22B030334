package lab2;

public class Cube extends Shape {
	 private double sideLength;

	    public Cube(double sideLength) {
	        this.sideLength = sideLength;
	    }

	    @Override
	    public double volume() {
	        return Math.pow(sideLength, 3);
	    }

	    @Override
	    public double surfaceArea() {
	        return 6 * Math.pow(sideLength, 2);
	    }
}
