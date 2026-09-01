package comparewords;

import java.util.Scanner;

public class CompareWords {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the first word: ");
        String firstWord = input.nextLine().trim();

        System.out.print("Enter the second word: ");
        String secondWord = input.nextLine().trim();

        if (firstWord.equalsIgnoreCase(secondWord)) {
            System.out.println("✅ The words are the same (case-insensitive).");
        } else {
            System.out.println("❌ The words are different.");
        }

        input.close();
    }
}
