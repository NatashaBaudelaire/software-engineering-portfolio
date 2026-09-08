package vehicle;

public class VehicleApp {

    public static void main(String[] args) {

        Manufacturer[] manufacturers = new Manufacturer[2];
        manufacturers[0] = new Manufacturer("Volkswagen AG", "Germany");
        manufacturers[1] = new Manufacturer("Toyota Motor Corporation", "Japan");

        Vehicle[] vehicles = new Vehicle[4];
        vehicles[0] = new Vehicle("P", 50, "Golf", "2022-01-15", manufacturers[0]);
        vehicles[1] = new Vehicle("U", 80, "Transporter", "2021-06-30", manufacturers[0]);
        vehicles[2] = new Vehicle("P", 45, "Corolla", "2023-02-10", manufacturers[1]);
        vehicles[3] = new Vehicle("U", 90, "Hilux", "2022-11-05", manufacturers[1]);
        System.out.println("Registered Vehicles:");
        for (Vehicle v : vehicles) {
            System.out.println(v.toString());
        }

        Vehicle firstVehicle = vehicles[0];
        double litersUsed = firstVehicle.fillTank();
        System.out.printf("\nFilled the first vehicle's tank with %.2f liters.%n", litersUsed);
        System.out.println(firstVehicle.toString());

        Vehicle thirdVehicle = vehicles[2];
        boolean refuelSuccess = thirdVehicle.refuel(20);
        System.out.printf("\nAttempt to refuel 20 liters in third vehicle: %s%n", refuelSuccess ? "Success" : "Failed");
        System.out.println(thirdVehicle.toString());

        boolean consumptionRegistered = thirdVehicle.registerConsumption(10);
        System.out.printf("\nRegister consumption of 10 liters on third vehicle: %s%n", consumptionRegistered ? "Success" : "Failed");
        System.out.println(thirdVehicle.toString());
    }
}
