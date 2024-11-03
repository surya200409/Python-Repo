import java.util.Scanner;

public class ColorNamePrinter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char colorCode = scanner.next().charAt(0);
        String colorName;

        switch (colorCode) {
            case 'V':
                colorName = "Violet";
                break;
            case 'I':
                colorName = "Indigo";
                break;
            case 'B':
                colorName = "Blue";
                break;
            case 'G':
                colorName = "Green";
                break;
            case 'Y':
                colorName = "Yellow";
                break;
            case 'O':
                colorName = "Orange";
                break;
            case 'R':
                colorName = "Red";
                break;
            default:
                colorName = "-1";
                break;
        }
System.out.println(colorName);
        scanner.close();
    }
}