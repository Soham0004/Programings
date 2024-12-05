class Account{
    String account_number;
    String account_holder;
    double balance;
    Account(String account_number, String account_holder, double balance){
        this.account_number = account_number;
        this.account_holder = account_holder;
        this.balance = balance;
    }
    void show(){
        System.out.println("Account Number: "+account_number);
        System.out.println("Account Holder: "+account_holder);
        System.out.println("Account Balance: "+balance);
    }
}
class SavingsAccount extends Account{
    double interest;
    SavingsAccount(String accno, String name, double balance, double interest){
        super(accno, name, balance);
        this.interest=interest;
    }
    void show(){
        super.show();
        System.out.println("Interest: "+interest);
    }
}
class FixedAccount extends Account{
    double interest;
    int duration;
    FixedAccount(String accno, String name, double balance, double interest, int duration){
        super(accno, name, balance);
        this.interest = interest;
        this.duration = duration;
    }
    void show(){
        super.show();
        System.out.println("Interest: "+interest);
        System.out.println("Duration: "+duration);
    }
}
class Main2{
    public static void main(String args[]){
        SavingsAccount s1 = new SavingsAccount("AS123", "John", 100000.0, 6.5);
        s1.show();
        FixedAccount f1 = new FixedAccount("AF123", "Jack", 300000.0, 9.5, 3);
        f1.show();
        Account a1 = new Account("A123", "George", 50000.0);
        a1.show();
    }
}
