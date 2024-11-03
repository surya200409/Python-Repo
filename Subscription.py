import java.util.Scanner;

public class Subscription {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the duration of the meeting
        int X = scanner.nextInt();

        // Determine if a subscription is needed
        if (X > 40) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        scanner.close();
    }    
}