class MyThread implements Runnable
{
public void run()
{
for(int i=1;i<=5;i++)
{
	System.out.println(Thread.currentThread().getName()+i);
	}
}
public static void main(String args[])
{
	MyThread mt=new MyThread();
	MyThread t1=new MyThread(mt);
	MyThread t2=new MyThread(mt);
	MyThread t3=new MyThread(mt);
	t1.setName("Red");
	t2.setName("BLUE");
	t3.setName("GREEN");
	t1.start();
	t2.start();
	t3.start();
	}
}
