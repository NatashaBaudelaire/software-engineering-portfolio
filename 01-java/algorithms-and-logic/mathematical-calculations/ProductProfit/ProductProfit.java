package ProductProfit;

import java.util.Scanner;

public class ProductProfit {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("=== Product Profit Calculator ===");

        System.out.print("Enter the cost price: ");
        while (!input.hasNextDouble()) {
            System.out.print("Invalid input. Enter a numeric value: ");
            input.next();
        }
        double costPrice = input.nextDouble();


        System.out.print("Enter the profit percentage: ");
        while (!input.hasNextDouble()) {
            System.out.print("Invalid input. Enter a numeric value: ");
            input.next();
        }
        double profitPercentage = input.nextDouble();

        double profitAmount = (costPrice * profitPercentage) / 100;
        double sellingPriceCash = costPrice + profitAmount;
        double sellingPriceInstallments = sellingPriceCash * 1.05;
        double cashTax = sellingPriceCash * 0.17;


        System.out.printf("Profit Amount: %.2f%n", profitAmount);
        System.out.printf("Cash Selling Price: %.2f%n", sellingPriceCash);
        System.out.printf("Installments Selling Price (+5%%): %.2f%n", sellingPriceInstallments);
        System.out.printf("Cash Tax (17%%): %.2f%n", cashTax);

        input.close();
    }
}
