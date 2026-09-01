package powercalculator;

import java.util.Scanner;

public class PowerCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("=== Electric Power Calculator ===");

        System.out.print("Enter the voltage (in volts): ");
        while (!input.hasNextDouble()) {
            System.out.print("Invalid input. Enter a numeric voltage: ");
            input.next();
        }
        double voltage = input.nextDouble();

        System.out.print("Enter the resistance (in ohms): ");
        while (!input.hasNextDouble()) {
            System.out.print("Invalid input. Enter a numeric resistance: ");
            input.next();
        }
        double resistance = input.nextDouble();

        if (resistance <= 0) {
            System.out.println("Error: Resistance must be greater than zero.");
        } else {
            double power = Math.pow(voltage, 2) / resistance;
            System.out.printf("The electric power is %.2f watts.%n", power);
        }

        input.close();
    }
}
