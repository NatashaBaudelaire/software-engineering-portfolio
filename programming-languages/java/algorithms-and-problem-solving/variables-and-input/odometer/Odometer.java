package odometer;

import java.util.Scanner;

public class Odometer {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int initial = readNonNegativeInt(input, "Enter the initial odometer value (km): ");
        int finalPos;


        do {
            finalPos = readNonNegativeInt(input, "Enter the final odometer value (km): ");
            if (finalPos < initial) {
                System.out.println("Error: The final odometer value cannot be less than the initial value.");
            }
        } while (finalPos < initial);

        int traveledMinutes;
        do {
            traveledMinutes = readNonNegativeInt(input, "Enter the time traveled in minutes: ");
            if (traveledMinutes <= 0) {
                System.out.println("Error: Time traveled must be greater than zero.");
            }
        } while (traveledMinutes <= 0);

        double distanceTraveled = finalPos - initial;
        double hoursTraveled = traveledMinutes / 60.0;
        double averageSpeed = distanceTraveled / hoursTraveled;

        System.out.printf("Distance Traveled: %.2f km%n", distanceTraveled);
        System.out.printf("Time Traveled: %.2f hours%n", hoursTraveled);
        System.out.printf("Average Speed: %.2f km/h%n", averageSpeed);

        input.close();
    }

    private static int readNonNegativeInt(Scanner input, String message) {
        int value;
        while (true) {
            System.out.print(message);
            if (input.hasNextInt()) {
                value = input.nextInt();
                if (value >= 0) {
                    break;
                } else {
                    System.out.println("Invalid input. Please enter a non-negative integer.");
                }
            } else {
                System.out.println("Invalid input. Please enter an integer.");
                input.nextLine();
            }
        }
        return value;
    }
}
