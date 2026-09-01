package TicketsSold;

import java.util.Scanner;

public class TicketsSold {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int ticketsAvailable = readNonNegativeInt(input, "Enter the number of tickets available for sale: ");
        int ticketsLeft;


        do {
            ticketsLeft = readNonNegativeInt(input, "Enter the number of tickets remaining after the sale: ");
            if (ticketsLeft > ticketsAvailable) {
                System.out.println("Error: Tickets remaining cannot be more than tickets available.");
            }
        } while (ticketsLeft > ticketsAvailable);

        double ticketPrice = readNonNegativeDouble(input, "Enter the ticket price: ");

        int ticketsSold = ticketsAvailable - ticketsLeft;
        double totalRevenue = ticketsSold * ticketPrice;

        System.out.println("\n--- Sales Report ---");
        System.out.println("Number of tickets sold: " + ticketsSold);
        System.out.printf("Revenue from ticket sales: R$ %.2f%n", totalRevenue);
        System.out.println("Number of tickets available after sale: " + ticketsLeft);

        input.close();
    }

    private static int readNonNegativeInt(Scanner input, String message) {
        int value;
        while (true) {
            System.out.print(message);
            if (input.hasNextInt()) {
                value = input.nextInt();
                if (value >= 0) break;
                else System.out.println("Invalid input. Enter a non-negative integer.");
            } else {
                System.out.println("Invalid input. Enter an integer.");
                input.next();
            }
        }
        return value;
    }

    private static double readNonNegativeDouble(Scanner input, String message) {
        double value;
        while (true) {
            System.out.print(message);
            if (input.hasNextDouble()) {
                value = input.nextDouble();
                if (value >= 0) break;
                else System.out.println("Invalid input. Enter a non-negative number.");
            } else {
                System.out.println("Invalid input. Enter a number.");
                input.next();
            }
        }
        return value;
    }
}
