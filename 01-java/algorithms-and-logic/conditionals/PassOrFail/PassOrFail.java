package PassOrFail;

import java.util.Scanner;

public class PassOrFail {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        System.out.println("Enter the indicator for the first assessment (A, B, or C): ");
        String firstAssessment = scanner.nextLine().toUpperCase();


        System.out.println("Enter the indicator for the second assessment (A, B, or C): ");
        String secondAssessment = scanner.nextLine().toUpperCase();

        System.out.println("Enter the attendance percentage: ");
        double attendancePercentage = scanner.nextDouble();

        if (attendancePercentage < 75) {
            System.out.println("FAILED (Insufficient attendance)");
        } 

        else if ((firstAssessment.equals("A") && secondAssessment.equals("A")) ||
                 (firstAssessment.equals("A") && secondAssessment.equals("B")) ||
                 (firstAssessment.equals("B") && secondAssessment.equals("A")) ||
                 (firstAssessment.equals("B") && secondAssessment.equals("B"))) {
            System.out.println("PASSED");
        } 

        else if (firstAssessment.equals("C") || secondAssessment.equals("C")) {
            scanner.nextLine();
            System.out.println("Enter the indicator for the final assessment (A, B, or C): ");
            String finalAssessment = scanner.nextLine().toUpperCase();

            if (finalAssessment.equals("A") || finalAssessment.equals("B")) {
                System.out.println("PASSED IN FINAL");
            } else {
                System.out.println("FAILED (Final assessment with indicator C)");
            }
        } 

        else {
            System.out.println("FAILED");
        }

        scanner.close();
    }
}
