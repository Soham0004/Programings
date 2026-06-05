interface I1
{
    void m1();
}
interface I2
{
    void m2();
}
interface I extends I1, I2
{
    void m3();
}
class X implements I
{
    public void m1()
    {
        System.out.println("Inside m1()");
    }
    public void m2() 
    {
        System.out.println("Inside m2()");
    }
    public void m3() 
    {
        System.out.println("Inside m3()");
    }
    public void m4() 
    {
        System.out.println("Inside m4()");
    }
}
public class Interface 
{
    public static void main(String[] args) 
    {
        X obj = new X();
        I interfaceRef = obj;
        interfaceRef.m1();
        interfaceRef.m2();
        interfaceRef.m3();
        obj.m4();
    }
}
