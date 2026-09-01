package characters;

import java.util.Scanner;

public class Characters {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String characters;


        do {
            System.out.print("Enter exactly eight characters: ");
            characters = input.nextLine();
            if (characters.length() != 8) {
                System.out.println("Invalid input. You must enter exactly 8 characters.");
            }
        } while (characters.length() != 8);

        int vowels = 0;
        int consonants = 0;
        int digits = 0;
        int others = 0;

        for (int i = 0; i < characters.length(); i++) {
            char ch = characters.charAt(i);

            if ("aeiouAEIOU".indexOf(ch) != -1) {
                vowels++;
            } else if (Character.isLetter(ch)) {
                consonants++;
            } else if (Character.isDigit(ch)) {
                digits++;
            } else {
                others++;
            }
        }

        System.out.println("\nCharacter Analysis:");
        System.out.println("Number of vowels: " + vowels);
        System.out.println("Number of consonants: " + consonants);
        System.out.println("Number of digits: " + digits);
        System.out.println("Number of other characters: " + others);

        input.close();
    }
}
