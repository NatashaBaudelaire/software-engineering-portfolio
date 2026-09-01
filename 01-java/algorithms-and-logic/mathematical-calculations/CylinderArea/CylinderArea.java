package CylinderArea;

import java.util.Scanner;

public class CylinderArea {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Provide the radius (r) of the base of the cylinder:");
        double radius = input.nextDouble();


        while (radius <= 0) {
            System.out.println("Invalid value! Radius must be greater than 0. Enter again:");
            radius = input.nextDouble();
        }

        System.out.println("Provide the height (h) of the cylinder:");
        double height = input.nextDouble();


        while (height <= 0) {
            System.out.println("Invalid value! Height must be greater than 0. Enter again:");
            height = input.nextDouble();
        }

        double volume = Math.PI * radius * radius * height;

        System.out.printf("The volume of the cylinder is: %.2f%n", volume);

        input.close();
    }
}
