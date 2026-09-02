package ship;

public class Trip {
    private static int idCounter = 1;

    public enum Situation {
        PLANNED,    
        ONGOING,    
        FINISHED    
    }

    private final int id;
    private String date;
    private Situation situation;
    private ContainerShip containerShip;
    private BulkCarrierShip bulkCarrierShip;

    public Trip(String date) {
        this.id = idCounter++;
        this.date = date;
        this.situation = Situation.PLANNED;
        this.containerShip = null;
        this.bulkCarrierShip = null;
    }

    public int getId() {
        return id;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public Situation getSituation() {
        return situation;
    }

    public ContainerShip getContainerShip() {
        return containerShip;
    }

    public BulkCarrierShip getBulkCarrierShip() {
        return bulkCarrierShip;
    }

    public boolean allocateContainerShip(ContainerShip ship) {
        if (ship.isAllocated()) return false;
        if (containerShip != null || bulkCarrierShip != null) return false;

        containerShip = ship;
        if (!ship.allocate()) {
            containerShip = null;
            return false;
        }
        return true;
    }

    public boolean allocateBulkCarrierShip(BulkCarrierShip ship) {
        if (ship.isAllocated()) return false;
        if (containerShip != null || bulkCarrierShip != null) return false;

        bulkCarrierShip = ship;
        if (!ship.allocate()) {
            bulkCarrierShip = null;
            return false;
        }
        return true;
    }

    public boolean startTrip() {
        Ship vessel = (containerShip != null) ? containerShip : bulkCarrierShip;
        if (vessel != null && vessel.getStatus() == Ship.Status.LOADED) {
            situation = Situation.ONGOING;
            return true;
        }
        return false;
    }

    public boolean finishTrip() {
        Ship vessel = (containerShip != null) ? containerShip : bulkCarrierShip;
        if (vessel != null && vessel.getStatus() == Ship.Status.VACANT) {
            situation = Situation.FINISHED;
            return true;
        }
        return false;
    }

    @Override
    public String toString() {
        String shipInfo = "No ship allocated";
        if (containerShip != null) {
            shipInfo = "Container Ship: " + containerShip.toString();
        } else if (bulkCarrierShip != null) {
            shipInfo = "Bulk Carrier Ship: " + bulkCarrierShip.toString();
        }
        return String.format("Trip[id=%d, date=%s, situation=%s, %s]", id, date, situation, shipInfo);
    }
}
