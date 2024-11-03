import java.util.Scanner;

public class PronicNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the input number
        int X = scanner.nextInt();

        // Check if the number is a Pronic number
        if (isPronic(X)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        scanner.close();
    }

    // Method to check if a number is a Pronic number
    private static boolean isPronic(int number) {
        for (int i = 0; i <= Math.sqrt(number); i++) {
            if (i * (i + 1) == number) {
                return true;
            }
        }
        return false;
    }
}