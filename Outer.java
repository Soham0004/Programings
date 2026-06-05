class Outer{
    class Inner1{
        void m1(){
            System.out.println("Method of Non-static Inner class is called.");
        }
    }
    static class Inner2{
        static void m2(){
            System.out.println("Method of Static Inner class is called.");
        }
    }
    public static void main(String []args){
        Outer o=new Outer();
        Outer.Inner1 i1=o.new Inner1();
        i1.m1();
        Outer.Inner2.m2();
    } 
}