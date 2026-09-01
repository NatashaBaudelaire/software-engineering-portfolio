package CheckReverse;

import java.util.Scanner;

public class CheckReverse {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the first word: ");
        String firstWord = input.nextLine().trim();

        System.out.print("Enter the second word: ");
        String secondWord = input.nextLine().trim();


        String reversedWord = new StringBuilder(firstWord).reverse().toString();

 
        if (reversedWord.equalsIgnoreCase(secondWord)) {
            System.out.println("✅ The second word is the reverse of the first.");
        } else {
            System.out.println("❌ The second word is NOT the reverse of the first.");
        }

        input.close();
    }
}
