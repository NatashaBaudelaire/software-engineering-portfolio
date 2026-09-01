package MinutesAndSeconds;

import java.util.Scanner;

public class MinutesAndSeconds {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int hours = -1;


        while (hours < 0) {
            System.out.print("Enter the number of hours (non-negative): ");
            if (input.hasNextInt()) {
                hours = input.nextInt();
                if (hours < 0) {
                    System.out.println("Invalid input. Hours cannot be negative.");
                }
            } else {
                System.out.println("Invalid input. Please enter an integer.");
                input.next();
            }
        }

        int minutes = hours * 60;
        int seconds = hours * 3600;

        System.out.printf("%d hour(s) is equivalent to %d minute(s) and %d second(s).%n", hours, minutes, seconds);

        input.close();
    }
}
