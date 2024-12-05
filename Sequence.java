class A{
    static int x;
    int y;
    static {
        System.out.println("In static block"+(x++));
    }
    {
        System.out.println("In non-static block.");
    }
    A(){
        System.out.println("In default constructor.");
    }
    public static void main(String[] args){
        System.out.println("In main method.");
        A a1 = new A();
        A a2 = new A();
    }
}
