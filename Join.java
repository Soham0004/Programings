class MyThread implements Runnable
{
	public void run()
	{
		for(int i=1;i<=5;i++)
		{
			System.out.println(Thread.currentThread().getName()+i);
		
			try
			{
				Thread.sleep(500);
			}
			catch(InterruptedException ie){}
		}
	}
	public static void main(String args[])
	{	System.out.println(Thread.currentThread().getName());
		MyThread mt=new MyThread();
		Thread t1=new Thread(mt);
		Thread t2=new Thread(mt);
		Thread t3=new Thread(mt);
		t1.setName("RED");
		t2.setName("BLUE");
		t3.setName("GREEN");
		t1.start();
		try
		{
			t1.join();
		}
		catch(InterruptedException ie){}
		t2.start();
		try
		{
			t2.join();
		}
		catch(InterruptedException ie){}
		t3.start();
	}
}
