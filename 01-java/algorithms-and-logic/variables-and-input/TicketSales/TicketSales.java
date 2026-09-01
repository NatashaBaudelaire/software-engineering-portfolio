package TicketSales;
import java.util.Scanner;

public class TicketSales {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the number of tickets available for sale: ");
        int ticketsAvailable = input.nextInt();

        System.out.print("Enter the number of tickets remaining after the sale: ");
        int ticketsLeft = input.nextInt();

        if (ticketsLeft > ticketsAvailable) {
            System.out.println("Error: Tickets remaining cannot be more than tickets available.");
            input.close();
            return;
        }

        System.out.print("Enter the ticket price: ");
        double ticketPrice = input.nextDouble();

        if (ticketPrice < 0) {
            System.out.println("Error: Ticket price cannot be negative.");
            input.close();
            return;
        }

        int ticketsSold = ticketsAvailable - ticketsLeft;
        double totalRevenue = ticketsSold * ticketPrice;
        
        System.out.println("Number of tickets sold: " + ticketsSold);
        System.out.printf("Revenue from ticket sales: £%.2f%n", totalRevenue);

        ticketsAvailable = ticketsLeft;

        System.out.println("Number of tickets available: " + ticketsAvailable);

        input.close();
    }
}