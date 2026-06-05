import java.io.*;
class Car2 implements Serializable
{
    String make;
    String model;
    Car2(String make,String model)
    {
        this.make=make;
        this.model=model;
    }
    void show()
    {
        System.out.println("Make: "+make);
        System.out.println("Model: "+model);
    }
    public static void main(String args[])
    {
        try
        {
            Car2 c1=new Car2("Honda","City");
            File f=new File("C.txt");
            FileOutputStream fos=new FileOutputStream(f);
            ObjectOutputStream oos=new ObjectOutputStream(fos);
            oos.writeObject(c1);
            oos.close();
            FileInputStream fis=new FileInputStream(f);
            ObjectInputStream ois=new ObjectInputStream(fis);
            Car2 cc=(Car2)ois.readObject();
            cc.show();
        }
        catch(Exception ioe){System.out.println(ioe);}
    }
}
