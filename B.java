class B{
    static int x;
    int y;
    static {
        System.out.println("In static block"+(x++));
    }
    {
        System.out.println("In non-static block.");
    }
    B(){
        System.out.println("In default constructor.");
    }
    public static void main(String[] args){
        System.out.println("In main method.");
        B a1 = new B();
        B a2 = new B();
    }
}
