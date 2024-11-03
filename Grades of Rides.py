import java.util.Scanner;

public class RideGradeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        
        int hurlFactor = Integer.parseInt(input[0]);
        int spinFactor = Integer.parseInt(input[1]);
        int speedFactor = Integer.parseInt(input[2]);

        boolean condition1 = hurlFactor > 50;
        boolean condition2 = spinFactor > 60;
        boolean condition3 = speedFactor > 100;

        int grade;

        if (condition1 && condition2 && condition3) {
            grade = 10;
        } else if (condition1 && condition2) {
            grade = 9;
        } else if (condition2 && condition3) {
            grade = 8;
        } else if (condition1 && condition3) {
            grade = 7;
        } else if (condition1 || condition2 || condition3) {
            grade = 6;
        } else {
            grade = 5;
        }

        System.out.println(grade);
        scanner.close();
    }
}