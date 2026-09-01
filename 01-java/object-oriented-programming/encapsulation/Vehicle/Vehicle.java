package Vehicle;

public class Vehicle {
    private static int idCounter = 1;

    private final int vehicleId;
    private String type;
    private int tankCapacity;
    private double litersInTank;
    private String model;
    private String acquisitionDate;
    private Manufacturer manufacturer;

    public Vehicle(String type, int tankCapacity, String model, String acquisitionDate, Manufacturer manufacturer) {
        this.vehicleId = idCounter++;
        this.type = type;
        this.tankCapacity = tankCapacity;
        this.litersInTank = 0;
        this.model = model;
        this.acquisitionDate = acquisitionDate;
        this.manufacturer = manufacturer;
    }

    public int getVehicleId() { return vehicleId; }
    public String getType() { return type; }
    public int getTankCapacity() { return tankCapacity; }
    public double getLitersInTank() { return litersInTank; }
    public String getModel() { return model; }
    public String getAcquisitionDate() { return acquisitionDate; }
    public Manufacturer getManufacturer() { return manufacturer; }

    public double fillTank() {
        double litersToFill = tankCapacity - litersInTank;
        litersInTank = tankCapacity;
        return litersToFill;
    }

    public boolean refuel(double liters) {
        if (litersInTank + liters <= tankCapacity) {
            litersInTank += liters;
            return true;
        }
        return false;
    }

    public boolean registerConsumption(double liters) {
        if (litersInTank >= liters) {
            litersInTank -= liters;
            return true;
        }
        return false;
    }

    @Override
    public String toString() {
        return String.format("ID: %d, Model: %s, Type: %s, Acquisition Date: %s, Manufacturer: %s, Country: %s, Tank Capacity: %d, Liters in Tank: %.2f",
            vehicleId, model, type, acquisitionDate,
            manufacturer.getCompanyName(), manufacturer.getCountry(),
            tankCapacity, litersInTank);
    }
}
