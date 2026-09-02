package studenttype;

import java.util.Scanner;

public class StudentType {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);


        System.out.print("Enter the number of subjects failed: ");
        int failedSubjects = input.nextInt();

        while (failedSubjects < 0) {
            System.out.print("Invalid number! Enter a non-negative number: ");
            failedSubjects = input.nextInt();
        }


        System.out.print("Enter the type of student (N - normal / B - scholarship holder): ");
        String studentType = input.next().toUpperCase();

        while (!studentType.equals("N") && !studentType.equals("B")) {
            System.out.print("Invalid student type. Enter N or B: ");
            studentType = input.next().toUpperCase();
        }


        double monthlyFee = 600.0;
        double discount = 0.0;

        if (studentType.equals("B")) {

            discount = monthlyFee * 0.30;
        } else {

            discount = -(failedSubjects * 50.0);
        }

        double finalFee = monthlyFee - discount;


        System.out.printf("The final monthly fee is: R$ %.2f%n", finalFee);

        input.close();
    }
}
