package ships;

public class bulkcarrierships extends ships {
    private int bulkType;

    public BulkCarrierShips(String name, int capacity, int bulkType) {
        super(name, capacity);
        this.bulkType = bulkType;
    }
}
