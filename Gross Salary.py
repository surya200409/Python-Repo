import java.util.Scanner;

public class GrossSalaryCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double basicSalary = scanner.nextDouble();
        double da = 0.0;
        double hra = 0.0;

        if (basicSalary <= 10000) {
            da = 0.80 * basicSalary;
            hra = 0.20 * basicSalary;
        } else if (basicSalary <= 20000) {
            da = 0.90 * basicSalary;
            hra = 0.25 * basicSalary;
        } else {
            da = 0.95 * basicSalary;
            hra = 0.30 * basicSalary;
        }

        double grossSalary = basicSalary + da + hra;
        System.out.printf("%.2f\n", grossSalary);

        scanner.close();
    }    
}