package glucoselevel;

import java.util.Scanner;

public class GlucoseLevelApp {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        GlucoseLevel test = new GlucoseLevel();

        System.out.print("Enter the test identifier: ");
        test.testId = input.nextInt();

        System.out.print("Enter glucose level (mg/dL): ");
        test.glucoseLevel = input.nextInt();

        System.out.println("\nTest ID: " + test.testId);
        System.out.println("Glucose level: " + test.glucoseLevel + " mg/dL");

        String diagnosis = test.getDiagnosis();
        System.out.println("Diagnosis: " + diagnosis);

        input.close();
    }
}
