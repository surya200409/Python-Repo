import java.util.Scanner;

public class AngleBetweenHands {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String time = scanner.nextLine();
        
        // Split the time into hours and minutes
        String[] parts = time.split(":");
        int hours = Integer.parseInt(parts[0]);
        int minutes = Integer.parseInt(parts[1]);
        
        // Adjust hours for 12-hour format if necessary
        if (hours >= 12) {
            hours -= 12;
        }
        
        // Calculate the positions of the hands
        double minuteAngle = minutes * 6; // Each minute is 6 degrees (360/60)
        double hourAngle = (hours * 30) + (minutes * 0.5); // Each hour is 30 degrees (360/12), plus half a degree per minute
        
        // Calculate the absolute difference between the two angles
        double angle = Math.abs(hourAngle - minuteAngle);
        
        // Ensure the angle is the smallest one (clockwise or anti-clockwise)
        angle = Math.min(angle, 360 - angle);
        
        // Output the result
        System.out.printf("%.1f\n", angle);
        scanner.close();
    }
}