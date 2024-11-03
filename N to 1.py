import java.util.Scanner;

public class NToOne {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read an integer N from input
        int N = scanner.nextInt();
        
        // Print numbers from N to 1, separated by spaces
        for (int i = N; i >= 1; i--) {
            System.out.print(i + " ");
        }
        
        scanner.close();
    }
}