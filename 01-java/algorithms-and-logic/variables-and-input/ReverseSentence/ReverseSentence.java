package reversesentence;

import java.util.Scanner;

public class ReverseSentence {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a sentence: ");
        String sentence = input.nextLine().trim();


        String[] words = sentence.split("\\s+");


        StringBuilder reversedWords = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            reversedWords.append(words[i]);
            if (i != 0) {
                reversedWords.append(" ");
            }
        }

        System.out.println("Reversed sentence: " + reversedWords);

        input.close();
    }
}
