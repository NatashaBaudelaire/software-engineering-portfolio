package Vehicle;

public class VehicleApp {

    public static void main(String[] args) {

        Manufacturer[] manufacturers = new Manufacturer[2];
        manufacturers[0] = new Manufacturer("Volkswagen AG", "Germany");
        manufacturers[1] = new Manufacturer("Toyota Motor Corporation", "Japan");

        VehicleAppList[] vehicles = new VehicleAppList[4];
        vehicles[0] = new VehicleAppList("P", 50, "Golf", "2022-01-15", manufacturers[0]);
        vehicles[1] = new VehicleAppList("U", 80, "Transporter", "2021-06-30", manufacturers[0]);
        vehicles[2] = new VehicleAppList("P", 45, "Corolla", "2023-02-10", manufacturers[1]);
        vehicles[3] = new VehicleAppList("U", 90, "Hilux", "2022-11-05", manufacturers[1]);
        System.out.println("Registered Vehicles:");
        for (VehicleAppList v : vehicles) {
            System.out.printf("ID: %d, Model: %s, Type: %s, Acquisition Date: %s, Manufacturer: %s, Country: %s%n",
                v.getVehicleId(), v.getModel(), v.getType(), v.getAcquisitionDate(),
                v.getManufacturer().getCompanyName(), v.getManufacturer().getCountry());
        }

        VehicleAppList firstVehicle = vehicles[0];
        double litersUsed = firstVehicle.fillTank();
        System.out.printf("%nFilled the first vehicle’s tank with %.2f liters.%n", litersUsed);
        System.out.printf("ID: %d, Model: %s, Tank Capacity: %d, Liters in Tank: %.2f%n",
            firstVehicle.getVehicleId(), firstVehicle.getModel(),
            firstVehicle.getTankCapacity(), firstVehicle.getLitresInTank());

        Vehicle thirdVehicle = vehicles[2];
        boolean refuelSuccess = thirdVehicle.refuel(20);
        System.out.printf("%nAttempt to refuel 20 liters in third vehicle: %s%n", refuelSuccess ? "Success" : "Failed");
        System.out.printf("ID: %d, Model: %s, Tank Capacity: %d, Liters in Tank: %.2f%n",
            thirdVehicle.getVehicleId(), thirdVehicle.getModel(),
            thirdVehicle.getTankCapacity(), thirdVehicle.getLitersInTank());

        boolean consumptionRegistered = thirdVehicle.registerConsumption(10);
        System.out.printf("%nRegister consumption of 10 liters on third vehicle: %s%n", consumptionRegistered ? "Success" : "Failed");
        System.out.printf("ID: %d, Model: %s, Tank Capacity: %d, Liters in Tank: %.2f%n",
            thirdVehicle.getVehicleId(), thirdVehicle.getModel(),
            thirdVehicle.getTankCapacity(), thirdVehicle.getLitersInTank());
    }
}
