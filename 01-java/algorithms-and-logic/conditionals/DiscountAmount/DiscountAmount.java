package DiscountAmount;

import java.util.Scanner;

public class DiscountAmount {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter the original amount:");
        double originalAmount = input.nextDouble();

        double discount;
        double finalAmount;

        if (originalAmount > 1000) {
            discount = originalAmount * 0.10;
            finalAmount = originalAmount - discount;
        } else {
            discount = 0;
            finalAmount = originalAmount;
        }

        System.out.printf("Discount amount: $%.2f%n", discount);
        System.out.printf("The discounted amount is: $%.2f%n", finalAmount);
        System.out.println("Thank you for your purchase!");

        input.close();
    }
}
