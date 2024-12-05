class Arr{
    public static void main (String args[]){
        if(args.length==3){
            int dim1=Integer.parseInt(args[0]);
            int dim2=Integer.parseInt(args[1]);
            int dim3=Integer.parseInt(args[2]);
            int[][][]x=new int[dim1][dim2][dim3];
            int c=0;
            for(int i=0; i<x.length; i++){
                for(int j=0; j<x[i].length; j++){
                    for(int k=0; k<x[i][j].length; k++){
                        x[i][j][k]=c++;
                        System.out.print(x[i][j][k]+"");
                    }
                    System.out.println();
                }
                System.out.println();
                System.out.println();
            }
        }
        else{
            System.out.println("Incorrect number of arguments");
        }
    }
}
