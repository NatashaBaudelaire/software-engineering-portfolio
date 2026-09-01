package TriangleArea;

import java.util.Scanner;

public class TriangleArea {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double base = readPositiveDouble(scanner, "Enter the base of the triangle: ");
        double height = readPositiveDouble(scanner, "Enter the height of the triangle: ");

        double area = (base * height) / 2;

        System.out.printf("The area of the triangle is: %.2f%n", area);

        scanner.close();
    }

    private static double readPositiveDouble(Scanner scanner, String message) {
        System.out.print(message);
        while (!scanner.hasNextDouble()) {
            System.out.print("Invalid input. Please enter a valid number: ");
            scanner.next();
        }
        double value = scanner.nextDouble();
        while (value <= 0) {
            System.out.print("Value must be greater than zero. Enter again: ");
            while (!scanner.hasNextDouble()) {
                System.out.print("Invalid input. Enter a valid number: ");
                scanner.next();
            }
            value = scanner.nextDouble();
        }
        return value;
    }
}
