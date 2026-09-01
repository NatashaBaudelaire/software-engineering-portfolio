package areacalculation;

import java.util.Scanner;

public class AreaCalculation {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int option = -1;

        while (option != 0) {
            System.out.println("----------------------------------------------- MENU OF OPTIONS -----------------------------------------------");
            System.out.println("Choose an option:");
            System.out.println("1 - Square");
            System.out.println("2 - Circle");
            System.out.println("3 - Triangle");
            System.out.println("0 - Exit");
            System.out.print("Option: ");

            option = input.nextInt();

            switch (option) {
                case 1:
                    System.out.print("Enter the length of the side of the square: ");
                    double side = input.nextDouble();

                    while (side <= 0) {
                        System.out.print("Invalid value! Enter a positive number: ");
                        side = input.nextDouble();
                    }

                    double areaSquare = side * side;
                    System.out.printf("The area of the square is: %.2f%n", areaSquare);
                    break;

                case 2:
                    System.out.print("Enter the radius of the circle: ");
                    double radius = input.nextDouble();

                    while (radius <= 0) {
                        System.out.print("Invalid value! Enter a positive number: ");
                        radius = input.nextDouble();
                    }

                    double areaCircle = Math.PI * radius * radius;
                    System.out.printf("The area of the circle is: %.2f%n", areaCircle);
                    break;

                case 3:
                    System.out.print("Enter the base of the triangle: ");
                    double baseTriangle = input.nextDouble();

                    while (baseTriangle <= 0) {
                        System.out.print("Invalid value! Enter a positive base: ");
                        baseTriangle = input.nextDouble();
                    }

                    System.out.print("Enter the height of the triangle: ");
                    double heightTriangle = input.nextDouble();

                    while (heightTriangle <= 0) {
                        System.out.print("Invalid value! Enter a positive height: ");
                        heightTriangle = input.nextDouble();
                    }

                    double areaTriangle = (baseTriangle * heightTriangle) / 2;
                    System.out.printf("The area of the triangle is: %.2f%n", areaTriangle);
                    break;

                case 0:
                    System.out.println("Exiting...");
                    break;

                default:
                    System.out.println("You have entered an invalid option!");
            }
        }

        input.close();
    }
}
