class SEQUENCE{
    static int x;
    int y;
    static {
        System.out.println("In static block"+(x++));
    }
    {
        System.out.println("In non-static block.");
    }
    SEQUENCE(){
        System.out.println("In default constructor.");
    }
    public static void main(String[] args){
        System.out.println("In main method.");
        SEQUENCE a1 = new SEQUENCE();
        SEQUENCE a2 = new SEQUENCE();
    }
}
