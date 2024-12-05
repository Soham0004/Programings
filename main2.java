class Outer
{
    class Inner1
    {
        private String message;   
        Inner1(String message) 
        {
            this.message = message;
        }
        void m1() 
        {
            System.out.println(message);
        }
    }
    static class Inner2 
    {
        private String message;    
        Inner2(String message) 
        {
            this.message = message;
        }
        void m2()
        {
            System.out.println(message);
        }
    }
    public static void main(String[] args)
    {
        Outer o = new Outer();
        Outer.Inner1 i1 = o.new Inner1("Method of Non-static Inner class is called...");
        i1.m1();    
        Outer.Inner2 i2 = new Outer.Inner2("Method of Static Inner class is called...");
        i2.m2();
    }
}
