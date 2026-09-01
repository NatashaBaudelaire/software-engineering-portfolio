package prospecting;

import java.util.Scanner;

public class Prospecting {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int option = -1;

        while (option != 0) {

            System.out.println("\n-----------------------------------------------");
            System.out.println("                 MENU OF OPTIONS               ");
            System.out.println("-----------------------------------------------");
            System.out.println("1 - Arithmetic Mean");
            System.out.println("2 - Weighted Mean");
            System.out.println("0 - Exit");
            System.out.print("Option: ");


            while (!scanner.hasNextInt()) {
                System.out.print("Invalid input. Enter a valid option: ");
                scanner.next();
            }
            option = scanner.nextInt();

            switch (option) {
                case 1 -> {
                    System.out.print("Enter the first grade: ");
                    double n1 = readDouble(scanner);

                    System.out.print("Enter the second grade: ");
                    double n2 = readDouble(scanner);

                    double arithmeticMean = (n1 + n2) / 2;
                    System.out.printf("Arithmetic Mean: %.2f%n", arithmeticMean);
                }

                case 2 -> {
                    System.out.print("Enter the first grade: ");
                    double g1 = readDouble(scanner);

                    System.out.print("Enter the second grade: ");
                    double g2 = readDouble(scanner);

                    double weightedAverage = (g1 * 3 + g2 * 7) / 10;
                    System.out.printf("Weighted Average: %.2f%n", weightedAverage);
                }

                case 0 -> System.out.println("Exiting...");

                default -> System.out.println("You have entered an invalid option!");
            }
        }

        scanner.close();
    }


    private static double readDouble(Scanner scanner) {
        while (!scanner.hasNextDouble()) {
            System.out.print("Invalid input. Enter a valid number: ");
            scanner.next();
        }
        return scanner.nextDouble();
    }
}
