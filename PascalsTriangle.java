import java.util.Scanner;
public class PascalsTriangle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of rows for Pascal's triangle: ");
        int numRows = scanner.nextInt();
    
        int[][] triangle = new int[numRows][numRows];
        
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i)
                    triangle[i][j] = 1;
                else
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
        }
        System.out.println("Pascal's Triangle:");
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(triangle[i][j] + " ");
            }
            System.out.println();
        }
    }
}
