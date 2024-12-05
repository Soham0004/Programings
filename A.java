class A{
    public static void main(String args[])
    {
        int[][]x = new int[4][];
        x[0] = new int [3];
        x[1] = new int [2];
        x[2] = new int [1];
        x[3] = new int [4];
        
        int c=0;
        for(int i=0; i<x.length; i++)
        {
            for(int j=0; j<x[i].length; j++)
            {
                c+=2;
                x[i][j]=c;
                System.out.print(x[i][j]+"");
            }
        System.out.println();
        }
    }
}
