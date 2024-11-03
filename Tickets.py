import java.util.Scanner;

public class ConcertTickets {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the cost of a single ticket
        int X = scanner.nextInt();

        // Calculate the total cost for 4 friends
        int totalCost = 4 * X;

        // Check if the total cost is within the limit of 1000 rupees
        if (totalCost <= 1000) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        scanner.close();
    }
}