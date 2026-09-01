package Ship;

public class Ship {
    private static int idCounter = 101;

    public enum Status {
        VACANT,      
        LOADING,     
        LOADED       
    }

    protected final int id;
    protected String name;
    protected double cargoCapacity;
    protected boolean allocated;
    protected Status status;
    protected int cranesQuantity;
    protected int layersQuantity;
    protected int hatchesQuantity;

    public Ship(String name, double cargoCapacity, int cranes, int layers, int hatches) {
        this.id = idCounter++;
        this.name = name;
        this.cargoCapacity = cargoCapacity;
        this.allocated = false;
        this.status = Status.VACANT;
        this.cranesQuantity = cranes;
        this.layersQuantity = layers;
        this.hatchesQuantity = hatches;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getCargoCapacity() {
        return cargoCapacity;
    }

    public void setCargoCapacity(double cargoCapacity) {
        this.cargoCapacity = cargoCapacity;
    }

    public boolean isAllocated() {
        return allocated;
    }

    public Status getStatus() {
        return status;
    }

    public int getCranesQuantity() {
        return cranesQuantity;
    }

    public void setCranesQuantity(int cranesQuantity) {
        this.cranesQuantity = cranesQuantity;
    }

    public int getLayersQuantity() {
        return layersQuantity;
    }

    public void setLayersQuantity(int layersQuantity) {
        this.layersQuantity = layersQuantity;
    }

    public int getHatchesQuantity() {
        return hatchesQuantity;
    }

    public void setHatchesQuantity(int hatchesQuantity) {
        this.hatchesQuantity = hatchesQuantity;
    }


    public boolean allocate() {
        if (!allocated && status == Status.VACANT) {
            allocated = true;
            return true;
        }
        return false;
    }


    public boolean startLoading() {
        if (allocated && status == Status.VACANT) {
            status = Status.LOADING;
            return true;
        }
        return false;
    }


    public boolean finishLoading() {
        if (status == Status.LOADING) {
            status = Status.LOADED;
            return true;
        }
        return false;
    }


    public boolean unload() {
        if (status == Status.LOADED) {
            status = Status.VACANT;
            allocated = false;
            return true;
        }
        return false;
    }

    @Override
    public String toString() {
        return String.format(
            "Ship[id=%d, name=%s, cargoCapacity=%.2f, allocated=%b, status=%s, cranes=%d, layers=%d, hatches=%d]",
            id, name, cargoCapacity, allocated, status, cranesQuantity, layersQuantity, hatchesQuantity
        );
    }
}
