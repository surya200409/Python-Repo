import java.util.Scanner;

public class GradesCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] marksInput = scanner.nextLine().split(" ");
        
        int totalMarks = 0;
        for (String mark : marksInput) {
            totalMarks += Integer.parseInt(mark);
        }

        double percentage = (totalMarks / 5.0);
        
        String grade;
        if (percentage >= 90) {
            grade = "Grade A";
        } else if (percentage >= 80) {
            grade = "Grade B";
        } else if (percentage >= 70) {
            grade = "Grade C";
        } else if (percentage >= 60) {
            grade = "Grade D";
        } else if (percentage >= 40) {
            grade = "Grade E";
        } else {
            grade = "Grade F";
        }

        System.out.println(grade);
        scanner.close();
    }
}