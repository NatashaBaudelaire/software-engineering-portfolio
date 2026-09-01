package ships;

public class shipsapp {
	public static void main(String[] args) {

        ContainerShips ship1 = new ContainerShips("Poseidon", 10000, 4, 6);
        System.out.println("2.1 " + ship1);

        BulkCarrierShips ship2 = new BulkCarrierShips("Titan", 15000, 5);
        System.out.println("2.2 " + ship2);

        Trips trip1 = new Trips("2025-06-01");
        System.out.println("2.3 " + trip1);

        boolean assigned = trip1.assignShipToTrip(ship1);
        System.out.println("2.4 Assigned? " + assigned);
        System.out.println("     " + trip1);

        ship1.startLoading();
        ship1.finishLoading();
        System.out.println("2.5 " + ship1);

        boolean started = trip1.startTrip();
        System.out.println("2.6 Trip started? " + started);
        System.out.println("     " + trip1);

        boolean finished = trip1.finishTrip();
        System.out.println("2.7 Finished? " + finished);
        System.out.println("     " + trip1);

        ship1.unload();
        System.out.println("2.8 " + ship1);

        finished = trip1.finishTrip();
        System.out.println("2.9 Finished? " + finished);
        System.out.println("     " + trip1);
    }
}
