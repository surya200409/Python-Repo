import java.util.Scanner;

public class RainFall {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the rainfall amount
        int x = scanner.nextInt();

        // Categorize the rainfall
        if (x < 3) {
            System.out.println("LIGHT");
        } else if (x >= 3 && x < 7) {
            System.out.println("MODERATE");
        } else {
            System.out.println("HEAVY");
        }

        scanner.close();
    }    
}