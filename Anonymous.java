public class Anonymous
{
    public static void main(String[] args)
    {
        Runnable runnable = new Runnable()
        {
            public void run()
            {
                System.out.println("This is inside the anonymous class implementation of Runnable.");
            }
        };
        runnable.run();
    }
}
