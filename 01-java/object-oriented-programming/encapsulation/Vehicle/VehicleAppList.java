package Vehicle;

public class VehicleAppList {
    private static int counter = 1;
    private final int vehicleId;
    private String type;
    private int tankCapacity;
    private String model;
    private String acquisitionDate;
    private Manufacturer manufacturer;
    private double litresInTank;

    public VehicleAppList(String type, int tankCapacity, String model, String acquisitionDate, Manufacturer manufacturer) {
        this.vehicleId = counter++;
        this.type = type;
        this.tankCapacity = tankCapacity;
        this.model = model;
        this.acquisitionDate = acquisitionDate;
        this.manufacturer = manufacturer;
        this.litresInTank = 0;
    }

    public int getVehicleId() { return vehicleId; }
    public String getType() { return type; }
    public int getTankCapacity() { return tankCapacity; }
    public String getModel() { return model; }
    public String getAcquisitionDate() { return acquisitionDate; }
    public Manufacturer getManufacturer() { return manufacturer; }
    public double getLitresInTank() { return litresInTank; }

    public double fillTank() {
        double filled = tankCapacity - litresInTank;
        litresInTank = tankCapacity;
        return filled;
    }

    public boolean refuel(double litres) {
        if (litres <= 0 || litresInTank + litres > tankCapacity) return false;
        litresInTank += litres;
        return true;
    }

    public boolean registerConsumption(double litres) {
        if (litres <= 0 || litres > litresInTank) return false;
        litresInTank -= litres;
        return true;
    }

    @Override
    public String toString() {
        return model + " (" + type + ") - " + litresInTank + "/" + tankCapacity + " litres";
    }
}
