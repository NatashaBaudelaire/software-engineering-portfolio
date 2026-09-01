package ships;

import ships.Ships;

public class Trips {
    private String date;
    private Ships ships;
    private boolean started;
    private boolean finished;

    public Trips(String date) {
        this.date = date;
        this.ships = null;
        this.started = false;
        this.finished = false;
    }

    public boolean assignShipToTrip(Ships ship) {
        if (this.ships == null) {
            this.ships = ship;
            return true;
        }
        return false;
    }

    public boolean startTrip() {
        if (ships != null && ships.isLoaded() && !started) {
            started = true;
            return true;
        }
        return false;
    }

    public boolean finishTrip() {
        if (started && ships != null && ships.isUnloaded() && !finished) {
            finished = true;
            return true;
	        }
	        return false;
	    }

	    @Override
	    public String toString() {
	        return String.format("Trip [Date: %s, Ship: %s, Started: %b, Finished: %b]",
	                date,
	                (ships == null ? "None" : ships.name),
	                started,
	                finished);
	    }
	}
