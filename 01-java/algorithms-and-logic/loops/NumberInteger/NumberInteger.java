package numberinteger;

import java.util.Scanner;

public class NumberInteger {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        System.out.print("Enter an integer: ");
        

        while (!input.hasNextInt()) {
            System.out.print("Invalid input! Enter a valid integer: ");
            input.next();
        }
        
        int number = input.nextInt();

        for (int i = 1; i <= number; i++) {
            System.out.println(i);
        }

        input.close();
    }
}
