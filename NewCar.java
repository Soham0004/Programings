import java.util.*;
class NewCar
{
    String make;
    String model;
    NewCar(String make, String model)
    {
        this.make=make;
        this.model=model;
    }
    void show()
    {
        System.out.println("MAKE: "+make);
        System.out.println("MODEL: "+model);
    }
    public static void main(String args[])
    {
        Car c1=new Car("Honda","City");
        Car c2=new Car("Hyundai","Alcazar");
        Car c3=new Car("Suzuki","Brezza");
        Car c4=new Car("Renault","Kwid");
        Car c5=new Car("Tata","Nexon");
        List l=new ArrayList();//List l=new LinkedList; Set l=new HashSet; Set l=new LinkedHashSet;
        l.add(c1);
        l.add(c2);
        l.add(c3);
        l.add(c4);
        l.add(c5);
        Iterator it=l.iterator();
        while(it.hasNext())
        {
            Car c=(Car)it.next();
            c.show();
        }
    }
}
