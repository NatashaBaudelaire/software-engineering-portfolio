package remotework;

import java.util.Scanner;

public class RemoteWork {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int daysRemoteWork = 0;
        double totalReimbursementAmount = 0.0;

        for (int i = 0; i < 5; i++) {

            System.out.print("Enter the minimum expected temperature for day " + (i + 1) + ": ");

            while (!input.hasNextInt()) {
                System.out.print("Invalid input! Enter a valid integer temperature: ");
                input.next();
            }

            int minimumTemperature = input.nextInt();

            if (minimumTemperature < 0) {
                daysRemoteWork++;
                totalReimbursementAmount += 80 * 2.0;
            }
        }

        System.out.println("\nDays with remote work: " + daysRemoteWork);
        System.out.printf("Total reimbursement amount: R$ %.2f%n", totalReimbursementAmount);

        input.close();
    }
}
