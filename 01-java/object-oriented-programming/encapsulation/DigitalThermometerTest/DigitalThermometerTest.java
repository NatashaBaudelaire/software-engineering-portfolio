package DigitalThermometerTest;

import java.util.Scanner;

public class DigitalThermometerTest {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Serial Number: ");
        String serialNumber = input.next();

        System.out.print("Type (single character): ");
        char type = input.next().charAt(0);

        System.out.print("Enter temperature: ");
        double temperature = input.nextDouble();


        DigitalThermometer dt = new DigitalThermometer(serialNumber, type);


        dt.setTemperature(temperature);


        System.out.println("Serial Number: " + dt.getSerialNumber());
        System.out.println("Type: " + dt.getType());
        System.out.println("Temperature: " + dt.getTemperature());
        System.out.println("Diagnosis: " + dt.getDiagnosis());


        System.out.print("Enter new temperature: ");
        double newTemperature = input.nextDouble();
        dt.setTemperature(newTemperature);
        System.out.println("Updated Diagnosis: " + dt.getDiagnosis());

        input.close();
    }
}
