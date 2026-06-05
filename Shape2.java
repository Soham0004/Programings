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
public class Shape2{
}