package BillAmount;

import java.util.Scanner;

public class BillAmount {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("What is the bill amount? $");
        double BillAmount = input.nextDouble();

        System.out.print("How many adult men? ");
        int numAdultMen = input.nextInt();

        System.out.print("How many adult women? ");
        int numAdultWomen = input.nextInt();

        System.out.print("How many children? ");
        int numChildren = input.nextInt();

        int weightAdultMan = 4;
        int weightAdultWoman = 3;
        int weightChild = 5;

        int totalWeight = (numAdultMen * weightAdultMan)
                        + (numAdultWomen * weightAdultWoman)
                        + (numChildren * weightChild);

        double costPerWeight = billamount / totalWeight;

        double totalAdultMen = costPerWeight * numAdultMen * weightAdultMan;
        double totalAdultWomen = costPerWeight * numAdultWomen * weightAdultWoman;
        double totalChildren = costPerWeight * numChildren * weightChild;

        double subtotal = totalAdultMen + totalAdultWomen + totalChildren;

        System.out.printf("Total Bill Amount: $%.2f%n", billamount);
        System.out.printf("Subtotal for Adult Men: $%.2f%n", totalAdultMen);
        System.out.printf("Subtotal for Adult Women: $%.2f%n", totalAdultWomen);
        System.out.printf("Subtotal for Children: $%.2f%n", totalChildren);
        System.out.printf("Subtotal sum check: $%.2f%n", subtotal);

        input.close();
    }
}
