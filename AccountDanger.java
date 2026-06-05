public class AccountDanger implements Runnable
{
    private Account acct=new Account();
    public static void main(String args[])
    {
        AccountDanger r=new AccountDanger();
        java.lang.Thread one=new java.lang.Thread(r);
        java.lang.Thread two=new java.lang.Thread(r);
        one.setName("Fred");
        two.setName("Lucy");
        one.start();
        two.start();
    }
    public void run()
    {
        for(int x=0;x<5;x++)
        {
            makeWithdrawal(10);
            if(acct.getBalance()<0)
            {
                System.out.println("Account is Overdrawn!");
            }
        }
    }
    private /*synchronized*/ void makeWithdrawal(int amt)
    {
        if(acct.getBalance()>=amt)
        {
            System.out.println(java.lang.Thread.currentThread().getName()+"is going to withdraw");
            try
            {
                java.lang.Thread.sleep(500);
            }
            catch(InterruptedException ex){}
            acct.withdraw(amt);
            System.out.println(java.lang.Thread.currentThread().getName()+" completes the withdrawal");
            
        }
        else
        {
            System.out.println("Not enough money in account for"+java.lang.Thread.currentThread().getName()+" to withdraw"+acct.getBalance());
        }
    }
}

class Account
{
    private int balance=50;
    public int getBalance()
    {
        return balance;
    }
    public void withdraw(int amount)
    {
        balance=balance-amount;
    }
}
