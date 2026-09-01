package ships;

public class containerships extends ships {
	    private int rows;
	    private int columns;

	    public ContainerShips(String name, int capacity, int rows, int columns) {
	        super(name, capacity);
	        this.rows = rows;
	        this.columns = columns;
	    }

	    @Override
	    public String toString() {
	        return super.toString() + String.format(", Rows: %d, Columns: %d", rows, columns);
	    }
	}
