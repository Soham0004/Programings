class MyThread extends java.lang.Thread
{
    public void run()
    {
        for(int i=1;i<=10;i++)
        {
            System.out.println(this.getName() + " " + i);
        }
    }
    public static void main(String args[])
    {
        MyThread t1=new MyThread();
        MyThread t2=new MyThread();
        MyThread t3=new MyThread();
        t1.setName("Red");
        t2.setName("BLUE");
        t3.setName("GREEN");
        t1.start();
        t2.start();
        t3.start();
    }
}
