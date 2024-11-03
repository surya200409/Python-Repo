import java.util.Scanner;

public class PrettyNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the number of test cases
        int T = scanner.nextInt();
        
        // Process each test case
        for (int t = 0; t < T; t++) {
            int L = scanner.nextInt();
            int R = scanner.nextInt();
            int count = 0;
            
            // Iterate through the range from L to R
            for (int i = L; i <= R; i++) {
                int lastDigit = i % 10;
                
                // Check if the last digit is 2, 3, or 9
                if (lastDigit == 2 || lastDigit == 3 || lastDigit == 9) {
                    count++;
                }
            }
            
            // Output the count of pretty numbers
            System.out.println(count);
        }
        
        scanner.close();
    }
}
