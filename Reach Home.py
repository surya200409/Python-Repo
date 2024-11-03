import java.util.Scanner;

public class ReachHome {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the amount of fuel in liters and the distance to home in kilometers
        int fuel = scanner.nextInt();
        int distance = scanner.nextInt();

        // Calculate the maximum distance that can be traveled with the given fuel
        int maxDistance = fuel * 5;

        // Check if the maximum distance is enough to reach home
        if (maxDistance >= distance) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

        scanner.close();
    }    
}