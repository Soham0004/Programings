import java.util.Scanner;

public class BlueFactorialCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("\033[34mWelcome to Blue Factorial Calculator!\033[0m");
        System.out.print("Enter a non-negative integer: ");
        
        int number = scanner.nextInt();
        scanner.close();
        
        int factorial = calculateFactorial(number);
        
        System.out.println("\033[34mThe factorial of " + number + " is: " + factorial + "\033[0m");
    }

    public static int calculateFactorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * calculateFactorial(n - 1);
        }
    }
}
