class MyThread1 implements Runnable
{
    public void run()
    {
        for(int i=1;i<=5;i++)
        {
            System.out.println(Thread.currentThread().getName()+i);
            //Thread.yield();
            try
            {
                         Thread.sleep(2000);
            }
            catch(InterruptedException ie){}
        }
    }
    public static void main(String args[])
    {
    MyThread1 mt=new MyThread1();
    Thread t1=new Thread(mt);
    Thread t2=new Thread(mt);
    Thread t3=new Thread(mt);
    t1.setName("Red");
    t2.setName("BLUE");
    t3.setName("GREEN");
    /*t1.setPriority(8);
    t2.setPriority(3);
    t3.setPriority(8);*/
    t1.start();
    t2.start();
    t3.start();
    }
}
