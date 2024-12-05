class Shape{
    double length;
    double width;
    Shape(){
        length = 1.0;
        width = 1.0;
    }
    Shape(double length, double width){
        this.length = length;
        this.width = width;
    }
    public double getArea(){
        return length*width;
    }
}

class Rectangle extends Shape{
    Rectangle (double l, double w)
    {
        super(l,w);
    }
    public double getArea(){
        return length*width;
    }
}

public class Test{
    public static void main(String[] args){
        Rectangle rectangle = new Rectangle (7.0, 4.5);
        System.out.println("Area of the rectangle: " + rectangle.getArea() );
    }
}
