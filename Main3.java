class Shape{
    protected double length;
    protected double width;
    public Shape(double length, double width){
        this.length = length;
        this.width = width;
    }
    public double calculateArea() {return 0.0;}
}
class Rectangle extends Shape{
    public Rectangle(double length, double width){
        super (length, width);
    }
    public double calculateArea(){
        return length*width;
    }
}
public class Main3{
    public static void main(String[] args){
        Shape S1 = new Shape(2,4);
        Rectangle rectangle1 = new Rectangle(5,4);
        Rectangle rectangle2 = new Rectangle(7, 3.5);
        System.out.println("Area of rectangle 1: " +rectangle1.calculateArea());
        System.out.println("Area of rectangle 2: " +rectangle2.calculateArea());
    }
}