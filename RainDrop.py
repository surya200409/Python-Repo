import java.util.Scanner;

public class RainDrop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        
        StringBuilder result = new StringBuilder();

        // Check for factors
        if (number % 3 == 0) {
            result.append("Pling");
        }
        if (number % 5 == 0) {
            result.append("Plang");
        }
        if (number % 7 == 0) {
            result.append("Plong");
        }

        // If no factors were found, return the number as a string
        if (result.length() == 0) {
            result.append(number);
        }

        System.out.println(result.toString());
        scanner.close();
    }
}