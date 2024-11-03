import java.util.Scanner;

public class DigitCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the input number
        int number = scanner.nextInt();

        // Initialize digit count to 0
        int digitCount = 0;

        // Count the digits using a loop
        while (number > 0) {
            number /= 10;
            digitCount++;
        }

        // Print the digit count
        System.out.println(digitCount);

        scanner.close();
    }
}